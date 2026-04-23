"""Stage 5 — Chain-of-thought judge.

A second LLM pass scores each sample on correctness / realism / distinctiveness.
Off by default in M1 (Free-tier behavior from spec). Fails open — parse errors
and timeouts default to PASS so a flaky judge doesn't throw away good data.
"""

from __future__ import annotations

import asyncio
import json
import time
from dataclasses import dataclass

from ..config import JobConfig, JudgeConfig
from ..debug import DebugWriter, _fence, _json
from ..providers.base import LLMProvider

_SYSTEM = """You are a strict quality judge for synthetic training data.
First write one sentence of reasoning, then output JSON with integer scores.
Output format: one reasoning sentence, newline, then JSON only."""

_USER_TEMPLATE = """Score this generated example:

DOMAIN: {domain}
DATASET PURPOSE: {purpose}

{speaker_block}

LABEL DEFINITIONS (use these when judging correctness):
{label_definitions}

EXAMPLE:
{sample}

Score 1-10 on each axis:
- CORRECTNESS: Does the text actually match the label/fields per the LABEL DEFINITIONS?
  A text from an OUT-OF-SCOPE speaker, or mislabeled per the definitions, gets <=3.
- REALISM: Would a real in-scope speaker produce this naturally?
- DISTINCTIVENESS: Is it meaningfully different from generic examples?

Return:
Reasoning: <one sentence>
{{"correctness": <int>, "realism": <int>, "distinctiveness": <int>}}"""


@dataclass
class JudgeStats:
    judged: int = 0
    passed: int = 0
    failed: int = 0
    unparseable: int = 0


async def judge_samples(
    samples: list[dict],
    cfg: JobConfig,
    *,
    provider: LLMProvider,
    jcfg: JudgeConfig | None = None,
    concurrency: int = 5,
    debug: DebugWriter | None = None,
) -> tuple[list[dict], JudgeStats]:
    jcfg = jcfg or cfg.judge
    stats = JudgeStats()
    if not jcfg.enabled or not samples:
        return samples, stats

    sem = asyncio.Semaphore(concurrency)
    kept: list[tuple[int, dict]] = []
    judge_logs: list[tuple[int, str]] = []  # (original_index, log_entry)

    speaker_block = cfg.project.speakers.as_prompt_block() or "SPEAKERS: (not constrained)"
    label_definitions = _format_label_definitions(cfg)

    async def _judge_one(i: int, sample: dict) -> None:
        async with sem:
            user = _USER_TEMPLATE.format(
                domain=cfg.project.domain_brief,
                purpose=cfg.dataset.brief,
                speaker_block=speaker_block,
                label_definitions=label_definitions,
                sample=json.dumps(sample, ensure_ascii=False, indent=2),
            )
            t0 = time.monotonic()
            resp = await provider.generate_text(_SYSTEM, user, max_retries=2)
            elapsed = time.monotonic() - t0
            stats.judged += 1

            scores = _extract_scores(resp.raw_text)
            if scores is None:
                stats.unparseable += 1
                kept.append((i, sample))
                if debug:
                    judge_logs.append((i, _judge_entry(i + 1, sample, resp, elapsed, None, "UNPARSEABLE (fail-open)")))
                return

            passed = (
                scores["correctness"] >= jcfg.min_correctness
                and scores["realism"] >= jcfg.min_realism
                and scores["distinctiveness"] >= jcfg.min_distinctiveness
            )
            if passed:
                stats.passed += 1
                kept.append((i, sample))
            else:
                stats.failed += 1

            if debug:
                result = "PASS" if passed else f"FAIL (min: correctness≥{jcfg.min_correctness}, realism≥{jcfg.min_realism}, distinctiveness≥{jcfg.min_distinctiveness})"
                judge_logs.append((i, _judge_entry(i + 1, sample, resp, elapsed, scores, result)))

    await asyncio.gather(*[_judge_one(i, s) for i, s in enumerate(samples)])
    kept.sort(key=lambda t: t[0])

    if debug:
        judge_logs.sort(key=lambda t: t[0])
        table_rows = "\n".join(
            f"| {i+1} | {s.get('text', '')[:60]}... | — |"
            for i, s in enumerate(samples)
        )
        header = (
            f"# Stage 5 — CoT Judge\n\n"
            f"## Thresholds\n"
            f"- Correctness ≥ {jcfg.min_correctness}\n"
            f"- Realism ≥ {jcfg.min_realism}\n"
            f"- Distinctiveness ≥ {jcfg.min_distinctiveness}\n\n"
            f"## Summary\n"
            f"- Judged: {stats.judged}\n"
            f"- Passed: {stats.passed}\n"
            f"- Failed: {stats.failed}\n"
            f"- Unparseable (fail-open): {stats.unparseable}\n\n"
            f"---\n\n"
        )
        debug.write("06_judge.md", header + "\n\n---\n\n".join(entry for _, entry in judge_logs))

    return [s for _, s in kept], stats


def _judge_entry(num: int, sample: dict, resp, elapsed: float, scores: dict | None, result: str) -> str:
    scores_block = ""
    if scores:
        scores_block = (
            f"\n### Scores\n"
            f"- Correctness: **{scores['correctness']}**\n"
            f"- Realism: **{scores['realism']}**\n"
            f"- Distinctiveness: **{scores['distinctiveness']}**\n"
        )
    return (
        f"## Sample {num} — **{result}**\n\n"
        f"### Input Sample\n{_fence(_json(sample), 'json')}\n\n"
        f"### Judge Response ({elapsed:.1f}s)\n{_fence(resp.raw_text)}"
        f"{scores_block}\n"
    )


def _format_label_definitions(cfg: JobConfig) -> str:
    """Render every enum field's value definitions for the judge."""
    blocks: list[str] = []
    for f in cfg.dataset_schema.fields:
        if f.type != "enum":
            continue
        blocks.append(f'{f.name} ({f.description or "enum field"}):')
        for ev in f.values or []:
            if ev.description:
                blocks.append(f'  - "{ev.name}": {ev.description}')
            else:
                blocks.append(f'  - "{ev.name}"')
    return "\n".join(blocks) or "(no enum fields)"


def _extract_scores(text: str) -> dict | None:
    if not text:
        return None
    start = text.find("{")
    end = text.rfind("}")
    if start < 0 or end <= start:
        return None
    try:
        data = json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        return None
    try:
        return {
            "correctness": int(data["correctness"]),
            "realism": int(data["realism"]),
            "distinctiveness": int(data["distinctiveness"]),
        }
    except (KeyError, ValueError, TypeError):
        return None

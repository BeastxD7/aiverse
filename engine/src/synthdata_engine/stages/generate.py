"""Stage 4 — Parallel generation.

Fire bounded-concurrency LLM calls per plan row, validate each response against
the user's schema, issue one corrective retry on schema failure, log refusals
as combination-level skips.
"""

from __future__ import annotations

import asyncio
import json
import random
import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field

from ..config import JobConfig
from ..debug import DebugWriter, _fence, _json
from ..providers.base import LLMProvider
from ..schema import DatasetSchema
from .compose import compose_prompt
from .plan import AllocationPlan, PlanRow


@dataclass
class GenStats:
    attempted: int = 0
    succeeded: int = 0
    schema_failed: int = 0
    refusals: int = 0
    errors: int = 0
    retries: int = 0
    skipped_combinations: list[str] = field(default_factory=list)


ProgressCb = Callable[[dict], Awaitable[None] | None]
SampleCb = Callable[[dict], Awaitable[None] | None]


async def generate_all(
    plan: AllocationPlan,
    cfg: JobConfig,
    *,
    schema: DatasetSchema,
    personas: list[str],
    provider: LLMProvider,
    on_progress: ProgressCb | None = None,
    on_sample: SampleCb | None = None,
    debug: DebugWriter | None = None,
) -> GenStats:
    stats = GenStats()
    sem = asyncio.Semaphore(cfg.provider.concurrency)
    rng = random.Random()
    sample_logs: list[str] = []  # collected across concurrent tasks (asyncio = single-thread, safe)
    sample_counter = [0]

    async def _emit(event: dict) -> None:
        if on_progress is None:
            return
        res = on_progress(event)
        if asyncio.iscoroutine(res):
            await res

    speaker_block = cfg.project.speakers.as_prompt_block()

    async def _one_call(row: PlanRow) -> None:
        async with sem:
            system, user = compose_prompt(
                row.combination,
                schema=schema,
                seeds=cfg.seeds,
                anti_seeds=cfg.anti_seeds,
                personas=personas,
                speaker_block=speaker_block,
                rng=rng,
                diversity=cfg.dataset.diversity,
            )
            stats.attempted += 1
            t0 = time.monotonic()
            resp = await provider.generate_json(system, user, max_retries=2)
            elapsed = time.monotonic() - t0
            stats.retries += max(0, resp.attempts - 1)

            combo_label = ", ".join(f"{k}={v}" for k, v in row.combination.items())

            if resp.outcome == "refusal":
                stats.refusals += 1
                if row.combination_id not in stats.skipped_combinations:
                    stats.skipped_combinations.append(row.combination_id)
                row.status = "failed"
                if debug:
                    sample_logs.append(_gen_entry(combo_label, user, resp, elapsed, "REFUSAL", None, None))
                await _emit({"type": "refusal", "combination_id": row.combination_id})
                return

            retry_note = ""
            if resp.outcome != "success" or not isinstance(resp.parsed, dict):
                err_hint = resp.error or "invalid JSON"
                correction = user + (
                    f"\n\nYour previous response failed validation: {err_hint}. "
                    "Return valid JSON that matches the schema exactly."
                )
                first_raw = resp.raw_text
                resp = await provider.generate_json(system, correction, max_retries=1)
                stats.retries += 1
                retry_note = f"\n\n> **Corrective retry triggered** — first response: {_fence(first_raw)}"
                if resp.outcome != "success" or not isinstance(resp.parsed, dict):
                    stats.errors += 1
                    if debug:
                        sample_logs.append(_gen_entry(combo_label, user, resp, elapsed, "ERROR", retry_note, None))
                    await _emit({"type": "error", "error": resp.error})
                    return

            ok, errs = schema.validate_row(resp.parsed)
            if not ok:
                correction = user + (
                    f"\n\nYour previous response failed schema validation: {errs}. "
                    "Fix ONLY the flagged fields and return valid JSON."
                )
                first_raw = resp.raw_text
                resp2 = await provider.generate_json(system, correction, max_retries=1)
                stats.retries += 1
                retry_note += f"\n\n> **Schema retry triggered** — errors: {errs}. First response: {_fence(first_raw)}"
                if resp2.outcome != "success" or not isinstance(resp2.parsed, dict):
                    stats.schema_failed += 1
                    if debug:
                        sample_logs.append(_gen_entry(combo_label, user, resp2, elapsed, "SCHEMA FAIL", retry_note, errs))
                    await _emit({"type": "schema_fail", "errors": errs})
                    return
                ok2, errs2 = schema.validate_row(resp2.parsed)
                if not ok2:
                    stats.schema_failed += 1
                    if debug:
                        sample_logs.append(_gen_entry(combo_label, user, resp2, elapsed, "SCHEMA FAIL", retry_note, errs2))
                    await _emit({"type": "schema_fail", "errors": errs2})
                    return
                resp = resp2

            # Combination is ground truth for schema fields it pins.
            # Override any mislabeled values so required-balanced classes
            # are never suppressed by LLM label drift.
            schema_field_names = {f.name for f in schema.fields}
            for key, pinned_val in row.combination.items():
                if key in schema_field_names and key in resp.parsed:
                    resp.parsed[key] = pinned_val

            row.samples.append(resp.parsed)
            row.produced += 1
            stats.succeeded += 1
            sample_counter[0] += 1
            if on_sample:
                res = on_sample(resp.parsed)
                if asyncio.iscoroutine(res):
                    await res
            if debug:
                sample_logs.append(_gen_entry(combo_label, user, resp, elapsed, "PASS", retry_note, None, resp.parsed, sample_counter[0]))
            await _emit(
                {
                    "type": "sample",
                    "combination_id": row.combination_id,
                    "total_succeeded": stats.succeeded,
                }
            )

    tasks: list[asyncio.Task] = []
    for row in plan.rows:
        row.status = "running"
        for _ in range(row.target):
            tasks.append(asyncio.create_task(_one_call(row)))

    await asyncio.gather(*tasks, return_exceptions=False)

    for row in plan.rows:
        if row.status == "running":
            row.status = "complete" if row.produced else "failed"

    if debug:
        header = (
            f"# Stage 4 — Generation\n\n"
            f"## Stats\n"
            f"- Attempted: {stats.attempted}\n"
            f"- Succeeded: {stats.succeeded}\n"
            f"- Schema failed: {stats.schema_failed}\n"
            f"- Refusals: {stats.refusals}\n"
            f"- Errors: {stats.errors}\n"
            f"- Retries: {stats.retries}\n\n"
            f"---\n\n"
        )
        debug.write("05_generation.md", header + "\n\n---\n\n".join(sample_logs))

    return stats


def _gen_entry(
    combo: str,
    user_prompt: str,
    resp,
    elapsed: float,
    status: str,
    retry_note: str | None,
    schema_errors,
    parsed: dict | None = None,
    sample_num: int | None = None,
) -> str:
    label = f"Sample {sample_num}" if sample_num else "Attempt"
    errs_line = f"\n**Schema errors:** {schema_errors}" if schema_errors else ""
    parsed_block = f"\n### Parsed Output\n{_fence(_json(parsed), 'json')}" if parsed else ""
    retry_block = retry_note or ""
    return (
        f"## {label} — `{combo}` — **{status}**\n\n"
        f"### User Prompt\n{_fence(user_prompt)}\n\n"
        f"### Raw LLM Response ({elapsed:.1f}s)\n{_fence(resp.raw_text)}"
        f"{errs_line}{retry_block}{parsed_block}\n"
    )


def flatten_samples(plan: AllocationPlan) -> list[dict]:
    out: list[dict] = []
    for row in plan.rows:
        out.extend(row.samples)
    return out

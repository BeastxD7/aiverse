"""Stage 1.5 — Logic filter.

Cartesian-product all axes, then ask the LLM (in batches) which combinations
are actually plausible to write an example for. Drop the nonsensical ones
before we waste generation calls on them.
"""

from __future__ import annotations

import itertools
import json
import time

from ..debug import DebugWriter, _fence, _json
from ..providers.base import LLMProvider

Combination = dict[str, str]

_SYSTEM = """You are filtering synthetic-data combinations for plausibility.
Output strict JSON only."""

_USER_TEMPLATE = """I have a list of axis-combinations below. For each one,
judge whether a realistic example could naturally exist with that combination.

DOMAIN BRIEF:
{domain_brief}

DATASET PURPOSE:
{dataset_brief}

Mark a combination as IMPLAUSIBLE only if it's contradictory, absurd, or
socially/emotionally incoherent (e.g. "report_harassment intent with cheerful tone").
When in doubt, keep it — we prefer variety over aggressive filtering.

Combinations (numbered):
{combos}

Return JSON of the form:
{{
  "keep": [<list of indices to KEEP>]
}}

JSON only."""


def cartesian(axes: dict[str, list[str]]) -> list[Combination]:
    names = list(axes.keys())
    rows: list[Combination] = []
    for values in itertools.product(*[axes[n] for n in names]):
        rows.append({n: v for n, v in zip(names, values, strict=True)})
    return rows


async def filter_combinations(
    combos: list[Combination],
    *,
    domain_brief: str,
    dataset_brief: str,
    provider: LLMProvider,
    batch_size: int = 25,
    debug: DebugWriter | None = None,
) -> list[Combination]:
    if not combos:
        return []

    kept: list[Combination] = []
    log_sections: list[str] = [
        f"# Stage 1.5 — Logic Filter\n\n"
        f"## Input\n- Total combinations: {len(combos)}\n"
        f"- Batch size: {batch_size}\n"
        f"- Batches: {(len(combos) + batch_size - 1) // batch_size}\n"
    ]

    for start in range(0, len(combos), batch_size):
        batch = combos[start : start + batch_size]
        batch_num = start // batch_size + 1
        numbered = "\n".join(
            f"{i}. {json.dumps(combo, ensure_ascii=False)}" for i, combo in enumerate(batch)
        )
        user = _USER_TEMPLATE.format(
            domain_brief=domain_brief,
            dataset_brief=dataset_brief,
            combos=numbered,
        )
        t0 = time.monotonic()
        resp = await provider.generate_json(_SYSTEM, user, max_retries=2)
        elapsed = time.monotonic() - t0

        batch_kept: list[Combination] = []
        batch_removed: list[Combination] = []

        if resp.outcome != "success" or not isinstance(resp.parsed, dict):
            batch_kept = list(batch)
        else:
            keep_idx = resp.parsed.get("keep")
            if not isinstance(keep_idx, list):
                batch_kept = list(batch)
            else:
                valid_idx = {int(i) for i in keep_idx if isinstance(i, int) or (isinstance(i, str) and i.isdigit())}
                for i, combo in enumerate(batch):
                    if i in valid_idx:
                        batch_kept.append(combo)
                    else:
                        batch_removed.append(combo)

        kept.extend(batch_kept)

        if debug:
            removed_lines = "\n".join(f"  - {_json(c)}" for c in batch_removed) or "  _(none)_"
            log_sections.append(
                f"\n## Batch {batch_num} (combos {start}–{start + len(batch) - 1})\n\n"
                f"### User Prompt\n{_fence(user)}\n\n"
                f"### Raw LLM Response\n{_fence(resp.raw_text)}\n\n"
                f"### Result\n"
                f"- Outcome: {resp.outcome} ({elapsed:.1f}s)\n"
                f"- Kept: {len(batch_kept)}/{len(batch)}\n"
                f"- Removed:\n{removed_lines}\n"
            )

    result = kept or combos
    if debug:
        log_sections.append(
            f"\n## Summary\n"
            f"- Input: {len(combos)} combinations\n"
            f"- Kept: {len(result)} combinations\n"
            f"- Removed: {len(combos) - len(result)} combinations\n"
        )
        debug.write("02_logic_filter.md", "\n".join(log_sections))

    return result

"""Stage 2 — Allocation planner.

Decide how many examples to generate per (valid) combination, honoring the
sweet spot rule (5-20 per combo) and the target count.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from uuid import uuid4

from ..debug import DebugWriter
from .logic_filter import Combination

SWEET_MIN = 5
SWEET_MAX = 20


@dataclass
class PlanRow:
    combination_id: str
    combination: Combination
    target: int
    status: str = "pending"  # pending | running | complete | failed
    retries: int = 0
    produced: int = 0
    samples: list[dict] = field(default_factory=list)


@dataclass
class AllocationPlan:
    target_count: int
    rows: list[PlanRow]
    overshoot_multiplier: float

    @property
    def total_target(self) -> int:
        return sum(r.target for r in self.rows)


def build_plan(
    combinations: list[Combination],
    target_count: int,
    *,
    overshoot: float = 1.1,
    rng: random.Random | None = None,
    debug: DebugWriter | None = None,
) -> AllocationPlan:
    """Split the target across combinations.

    Overshoot by ~10% up front so dedup losses don't force a backfill round.
    """
    if not combinations:
        raise ValueError("no combinations to plan from")

    rng = rng or random.Random()
    adjusted_target = int(target_count * overshoot)

    n = len(combinations)
    per = max(1, adjusted_target // n)

    if per > SWEET_MAX and n < 200:
        # Too few combinations for the target — cap per-combo at sweet max;
        # the caller can request axis expansion if still short. We still fire
        # what we have; overshoot handles the small residual.
        per = SWEET_MAX

    if per < SWEET_MIN and n > adjusted_target // SWEET_MIN:
        # Too many combinations — randomly sample down to something sensible.
        keep = max(1, adjusted_target // SWEET_MIN)
        combinations = rng.sample(combinations, keep)
        n = len(combinations)
        per = max(1, adjusted_target // n)

    rows = [
        PlanRow(
            combination_id=uuid4().hex[:12],
            combination=combo,
            target=per,
        )
        for combo in combinations
    ]

    # Distribute the remainder so we actually hit adjusted_target — but never
    # exceed SWEET_MAX per combo (that's the whole point of the cap).
    remainder = adjusted_target - per * n
    if per < SWEET_MAX:
        headroom_per_row = SWEET_MAX - per
        max_distributable = headroom_per_row * n
        remainder = min(remainder, max_distributable)
        for i in range(remainder):
            rows[i % n].target += 1

    plan = AllocationPlan(
        target_count=target_count,
        rows=rows,
        overshoot_multiplier=overshoot,
    )

    if debug:
        rows_md = "\n".join(
            f"| `{r.combination_id}` | {', '.join(f'{k}={v}' for k, v in r.combination.items())} | {r.target} |"
            for r in rows
        )
        debug.write(
            "03_allocation_plan.md",
            f"# Stage 2 — Allocation Plan\n\n"
            f"## Input\n"
            f"- Valid combinations: {len(combinations)}\n"
            f"- Target count: {target_count}\n"
            f"- Overshoot multiplier: {overshoot}×\n"
            f"- Adjusted target: {adjusted_target}\n\n"
            f"## Per-combination allocation\n\n"
            f"| ID | Combination | Target |\n"
            f"|---|---|---|\n"
            f"{rows_md}\n\n"
            f"## Total planned: {plan.total_target} samples across {len(rows)} combinations\n",
        )

    return plan

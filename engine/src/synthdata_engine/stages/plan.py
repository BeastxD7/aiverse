"""Stage 2 — Allocation planner.

Decide how many examples to generate per (valid) combination, honouring the
sweet-spot rule and the target count.  At small scale SWEET_MAX=20 keeps each
combination varied.  At large scale (100K+) the effective ceiling rises
proportionally so the target stays achievable regardless of how many
combinations exist.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from uuid import uuid4

from ..debug import DebugWriter
from .logic_filter import Combination

SWEET_MIN = 5
SWEET_MAX = 20          # ideal upper bound for small datasets; scaled up dynamically
MAX_PER_COMBO = 5_000   # hard sanity cap — dedup/judge handle diversity above this


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
    combination_capped: bool = False

    @property
    def total_target(self) -> int:
        return sum(r.target for r in self.rows)

    @property
    def undershoot_risk(self) -> bool:
        """True when the hard MAX_PER_COMBO cap prevents reaching the target."""
        return self.combination_capped and self.total_target < self.target_count


def build_plan(
    combinations: list[Combination],
    target_count: int,
    *,
    overshoot: float = 1.1,
    rng: random.Random | None = None,
    debug: DebugWriter | None = None,
) -> AllocationPlan:
    """Split the target across combinations.

    Overshoot by ~10% up front so judge/dedup losses rarely force a backfill.
    """
    if not combinations:
        raise ValueError("no combinations to plan from")

    rng = rng or random.Random()
    adjusted_target = int(target_count * overshoot)
    n = len(combinations)
    per = max(1, adjusted_target // n)

    # Effective ceiling: honour SWEET_MAX when combos are plentiful enough to
    # reach the target at that cap.  Otherwise raise it proportionally so large
    # targets (100K+) remain achievable.  Never exceed MAX_PER_COMBO.
    effective_max = max(SWEET_MAX, math.ceil(adjusted_target / max(n, 1)))
    effective_max = min(effective_max, MAX_PER_COMBO)

    combination_capped = per > effective_max
    if combination_capped:
        per = effective_max

    # Too many combinations for a small target — sample down so per >= SWEET_MIN.
    if per < SWEET_MIN and n > adjusted_target // SWEET_MIN:
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

    # Distribute remainder up to effective_max so we precisely hit adjusted_target.
    remainder = adjusted_target - per * n
    headroom = effective_max - per
    if headroom > 0 and remainder > 0:
        max_distributable = headroom * n
        remainder = min(remainder, max_distributable)
        for i in range(remainder):
            rows[i % n].target += 1

    plan = AllocationPlan(
        target_count=target_count,
        rows=rows,
        overshoot_multiplier=overshoot,
        combination_capped=combination_capped,
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
            f"- Adjusted target: {adjusted_target}\n"
            f"- Effective max per combo: {effective_max}\n\n"
            f"## Per-combination allocation\n\n"
            f"| ID | Combination | Target |\n"
            f"|---|---|---|\n"
            f"{rows_md}\n\n"
            f"## Total planned: {plan.total_target} samples across {len(rows)} combinations\n",
        )

    return plan

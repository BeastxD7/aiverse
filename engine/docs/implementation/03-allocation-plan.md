# Stage 2 — Allocation Plan

## Purpose

Distribute the requested `target_count` samples across valid combinations, producing a `PlanRow` per combination with a concrete sample target. Overshoots by ~10% so judge/dedup losses rarely require a backfill round.

## Constants

| Constant | Value | Role |
|---|---|---|
| `SWEET_MIN` | 5 | Minimum samples per combination. Combos below this floor are dropped to avoid thin, low-signal rows. |
| `SWEET_MAX` | 20 | Ideal upper bound for small datasets. Honoured when you have enough combinations to hit the target at this cap. |
| `MAX_PER_COMBO` | 5 000 | Hard sanity cap per combination regardless of scale. Only triggered when a single combination would need >5 000 samples (e.g. 1 combo at 1M target). |

## Scale-aware effective ceiling

`SWEET_MAX=20` is a diversity hint, not a hard wall. At 100K+ targets with few combinations there isn't enough room to reach the target at 20/combo. The planner resolves this with a dynamic effective ceiling:

```
effective_max = max(SWEET_MAX, ceil(adjusted_target / n_combos))
effective_max = min(effective_max, MAX_PER_COMBO)
```

Examples:
| Scenario | Combos | Target | effective_max | Per-combo |
|---|---|---|---|---|
| Small dataset | 100 | 500 | 20 | 5 |
| Medium dataset | 50 | 500 | 20 | 11 |
| Large (100K, rich axes) | 500 | 100 000 | 200 | 200 |
| Large (100K, sparse axes) | 30 | 100 000 | 3 334 | 3 334 |
| Extreme (hard cap) | 1 | 1 000 000 | 5 000 | 5 000 — capped |

When `effective_max` had to be raised above `SWEET_MAX`, diversity is protected by the judge and dedup stages downstream, not by the per-combo ceiling.

## Algorithm

1. `adjusted_target = floor(target_count × overshoot)` (default overshoot = 1.1×)
2. `per = max(1, adjusted_target // n_combos)`
3. Compute `effective_max` as above. Cap `per` if it exceeds `effective_max` (sets `combination_capped = True`).
4. If `per < SWEET_MIN` and there are too many combinations, randomly sample combos down to `adjusted_target // SWEET_MIN` so every kept row has at least `SWEET_MIN` samples.
5. Distribute the remainder (samples not covered by `per × n`) across the first N rows, up to `effective_max` per row.

## `undershoot_risk`

`True` only when `combination_capped = True` AND `total_target < target_count` — meaning even the hard `MAX_PER_COMBO` cap prevents reaching the requested count. In practice this only fires at absurd scale (single combination, millions of samples). The pipeline warns and runs multiple backfill passes to compensate.

## Output

`AllocationPlan` with `list[PlanRow]`, each row containing: `combination_id`, `combination`, `target`, `status`, `samples`.

## File

`src/synthdata_engine/stages/plan.py`

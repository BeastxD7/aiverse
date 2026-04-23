# Stage 2 — Allocation Plan

## Purpose

Distribute the requested `target_count` samples across valid combinations, respecting SWEET_MIN and SWEET_MAX bounds per combination.

## Constants

- `SWEET_MIN = 5` — minimum samples per combination (below this, a combination is too thin)
- `SWEET_MAX = 20` — maximum samples per combination (above this, diversity within a combo collapses)

## Algorithm

1. Compute `per = target_count // len(valid_combinations)`, clamped to `[SWEET_MIN, SWEET_MAX]`
2. If `per == SWEET_MIN`, not all combos can be used — keep only the first `target_count // SWEET_MIN` combinations
3. Apply 10% overshoot: each combination targets `ceil(per * 1.1)` to absorb schema failures and refusals
4. Distribute remainder: if `per < SWEET_MAX`, add 1 extra to the first N combinations until target is reached, capped by `SWEET_MAX` per row

## Output

`AllocationPlan` with `list[PlanRow]`, each row containing: `combination`, `target`, `status`, `samples`

## Why overshoot?

Generation fails silently — JSON parse errors, schema mismatches, LLM refusals all discard samples. The 10% overshoot ensures we hit `target_count` even with a failure rate up to ~9%.

## File

`engine/src/synthdata_engine/stages/plan.py`

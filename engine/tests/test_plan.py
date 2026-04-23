import random

from synthdata_engine.stages.plan import SWEET_MAX, SWEET_MIN, build_plan


def test_plan_hits_adjusted_target():
    combos = [{"a": str(i)} for i in range(50)]
    plan = build_plan(combos, target_count=500, overshoot=1.1)
    assert plan.total_target == int(500 * 1.1)


def test_sweet_spot_cap_when_few_combinations():
    combos = [{"a": str(i)} for i in range(4)]
    plan = build_plan(combos, target_count=500, overshoot=1.0)
    # 4 combos * 20 (SWEET_MAX) = 80 samples, not 500, since we cap per-combo.
    # Each row should be at SWEET_MAX.
    assert all(r.target <= SWEET_MAX for r in plan.rows)


def test_sampling_when_too_many_combinations():
    combos = [{"a": str(i)} for i in range(500)]
    plan = build_plan(
        combos,
        target_count=100,
        overshoot=1.0,
        rng=random.Random(42),
    )
    # Should sample down so per-combo >= SWEET_MIN when possible.
    assert all(r.target >= 1 for r in plan.rows)
    # Number of rows should shrink to fit sweet min.
    assert len(plan.rows) <= 100 // SWEET_MIN + 5  # small slack for rounding


def test_unique_combination_ids():
    combos = [{"a": str(i)} for i in range(10)]
    plan = build_plan(combos, target_count=50)
    ids = {r.combination_id for r in plan.rows}
    assert len(ids) == len(plan.rows)

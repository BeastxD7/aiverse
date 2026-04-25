import random

from synthdata_engine.stages.plan import MAX_PER_COMBO, SWEET_MAX, SWEET_MIN, build_plan


def test_plan_hits_adjusted_target():
    combos = [{"a": str(i)} for i in range(50)]
    plan = build_plan(combos, target_count=500, overshoot=1.1)
    assert plan.total_target == int(500 * 1.1)


def test_plan_scales_per_combo_when_combos_are_sparse():
    """With few combos and a large target, per-combo rises above SWEET_MAX to hit the target."""
    combos = [{"a": str(i)} for i in range(4)]
    plan = build_plan(combos, target_count=500, overshoot=1.0)
    # 4 combos must collectively cover 500 samples — effective_max raises above 20.
    assert plan.total_target == 500
    assert all(r.target > SWEET_MAX for r in plan.rows)


def test_plan_100k_with_few_combos():
    """30 combos at 100K target: total must reach 100K, each combo handles ~3333."""
    combos = [{"a": str(i)} for i in range(30)]
    plan = build_plan(combos, target_count=100_000, overshoot=1.0)
    assert plan.total_target == 100_000
    assert all(r.target >= 3_000 for r in plan.rows)


def test_plan_100k_with_many_combos():
    """500 combos at 100K target: total must reach 100K, each combo handles ~200."""
    combos = [{"a": str(i)} for i in range(500)]
    plan = build_plan(combos, target_count=100_000, overshoot=1.0)
    assert plan.total_target == 100_000
    assert all(r.target >= 150 for r in plan.rows)


def test_plan_respects_hard_cap():
    """Even at extreme scale, no combo exceeds MAX_PER_COMBO."""
    combos = [{"a": "only_one"}]
    plan = build_plan(combos, target_count=1_000_000, overshoot=1.0)
    assert all(r.target <= MAX_PER_COMBO for r in plan.rows)
    assert plan.combination_capped
    assert plan.undershoot_risk


def test_sampling_when_too_many_combinations():
    combos = [{"a": str(i)} for i in range(500)]
    plan = build_plan(
        combos,
        target_count=100,
        overshoot=1.0,
        rng=random.Random(42),
    )
    assert all(r.target >= 1 for r in plan.rows)
    assert len(plan.rows) <= 100 // SWEET_MIN + 5


def test_unique_combination_ids():
    combos = [{"a": str(i)} for i in range(10)]
    plan = build_plan(combos, target_count=50)
    ids = {r.combination_id for r in plan.rows}
    assert len(ids) == len(plan.rows)


def test_plan_overshoot_scales_total():
    """Total planned = floor(target * overshoot), not just target."""
    combos = [{"a": str(i)} for i in range(20)]
    plan = build_plan(combos, target_count=200, overshoot=1.2)
    assert plan.total_target == int(200 * 1.2)


def test_plan_sweet_max_respected_when_combos_plentiful():
    """When n * SWEET_MAX >= target, per-combo stays at or below SWEET_MAX."""
    combos = [{"a": str(i)} for i in range(100)]
    plan = build_plan(combos, target_count=500, overshoot=1.0)
    # 100 combos * 20 = 2000 >= 500, so SWEET_MAX ceiling applies.
    assert all(r.target <= SWEET_MAX for r in plan.rows)

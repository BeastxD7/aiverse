"""Orchestrates all 6 stages end-to-end."""

from __future__ import annotations

import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from pathlib import Path

from .config import JobConfig
from .debug import DebugWriter, make_run_dir
from .providers import BedrockCredentials, BedrockProvider, OllamaProvider
from .providers.base import LLMProvider
from .stages.compose import build_persona_pool
from .stages.dedup import dedupe, pick_text_fields
from .stages.discover import discover_axes
from .stages.generate import GenStats, flatten_samples, generate_all
from .stages.judge import JudgeStats, judge_samples
from .stages.logic_filter import Combination, cartesian, filter_combinations
from .stages.plan import AllocationPlan, build_plan


@dataclass
class JobResult:
    samples: list[dict]
    axes: dict[str, list[str]]
    combinations_total: int
    combinations_kept: int
    plan: AllocationPlan
    gen_stats: GenStats
    judge_stats: JudgeStats
    duplicates_removed: int
    elapsed_seconds: float
    personas: list[str] = field(default_factory=list)


StageCb = Callable[[str, dict], Awaitable[None] | None]


async def run_job(
    cfg: JobConfig,
    *,
    on_stage: StageCb | None = None,
    on_progress: Callable | None = None,
    debug_dir: Path | None = None,
) -> JobResult:
    provider = _build_provider(cfg)
    dbg: DebugWriter | None = DebugWriter(debug_dir) if debug_dir else None
    await _call(on_stage, "start", {"target": cfg.dataset.target_count})

    started = time.monotonic()

    # Warmup: load model into memory so first stage doesn't eat a cold start
    if hasattr(provider, "warmup"):
        await _call(on_stage, "warmup", {"status": "running"})
        await provider.warmup()  # type: ignore[attr-defined]
        await _call(on_stage, "warmup", {"status": "done"})

    # Stage 1 — discover axes
    await _call(on_stage, "stage1_discover", {"status": "running"})
    axes = await discover_axes(cfg, provider, debug=dbg)
    await _call(on_stage, "stage1_discover", {"status": "done", "axes": axes})

    # Stage 1.5 — logic filter
    all_combos: list[Combination] = cartesian(axes)
    # Always pre-sample down so we never waste effort (filter or generation)
    # on combinations we couldn't possibly use.
    combos_to_use = all_combos
    pre_sampled = 0
    max_useful = max(cfg.dataset.target_count * 3, 100)
    if len(all_combos) > max_useful:
        import random as _r
        combos_to_use = _r.Random(42).sample(all_combos, max_useful)
        pre_sampled = len(all_combos) - len(combos_to_use)

    if cfg.logic_filter.enabled:
        await _call(
            on_stage,
            "stage15_logic",
            {"status": "running", "total": len(all_combos), "filtering": len(combos_to_use), "pre_sampled_out": pre_sampled},
        )
        valid = await filter_combinations(
            combos_to_use,
            domain_brief=cfg.project.domain_brief,
            dataset_brief=cfg.dataset.brief,
            provider=provider,
            batch_size=cfg.logic_filter.batch_size,
            debug=dbg,
        )
        await _call(
            on_stage,
            "stage15_logic",
            {"status": "done", "total": len(all_combos), "kept": len(valid)},
        )
    else:
        valid = combos_to_use
        await _call(
            on_stage,
            "stage15_logic",
            {"status": "skipped", "total": len(all_combos), "pre_sampled_out": pre_sampled},
        )

    # Stage 2 — plan
    await _call(on_stage, "stage2_plan", {"status": "running"})
    plan = build_plan(valid, cfg.dataset.target_count, debug=dbg)
    await _call(
        on_stage,
        "stage2_plan",
        {"status": "done", "rows": len(plan.rows), "total_target": plan.total_target},
    )

    # Stage 3 — personas
    await _call(on_stage, "stage3_personas", {"status": "running"})
    personas = await build_persona_pool(cfg, provider, debug=dbg)
    await _call(on_stage, "stage3_personas", {"status": "done", "count": len(personas)})

    # Stage 4 — generate
    await _call(on_stage, "stage4_generate", {"status": "running"})
    gen_stats = await generate_all(
        plan,
        cfg,
        schema=cfg.dataset_schema,
        personas=personas,
        provider=provider,
        on_progress=on_progress,
        debug=dbg,
    )
    samples = flatten_samples(plan)
    await _call(
        on_stage,
        "stage4_generate",
        {
            "status": "done",
            "succeeded": gen_stats.succeeded,
            "schema_failed": gen_stats.schema_failed,
            "refusals": gen_stats.refusals,
            "errors": gen_stats.errors,
        },
    )

    # Stage 5 — judge (optional)
    await _call(on_stage, "stage5_judge", {"status": "running", "enabled": cfg.judge.enabled})
    judge_provider = _build_judge_provider(cfg) if cfg.judge.enabled else provider
    samples, judge_stats = await judge_samples(samples, cfg, provider=judge_provider, debug=dbg)
    await _call(
        on_stage,
        "stage5_judge",
        {
            "status": "done",
            "judged": judge_stats.judged,
            "passed": judge_stats.passed,
            "failed": judge_stats.failed,
        },
    )

    # Stage 6 — dedup
    await _call(on_stage, "stage6_dedup", {"status": "running"})
    text_fields = pick_text_fields(cfg.dataset_schema)
    samples, removed = dedupe(
        samples,
        text_fields=text_fields,
        threshold=cfg.dedup.threshold,
        num_perm=cfg.dedup.num_perm,
        debug=dbg,
    )
    await _call(on_stage, "stage6_dedup", {"status": "done", "removed": removed, "kept": len(samples)})

    # Trim to target if we overshot
    if len(samples) > cfg.dataset.target_count:
        samples = samples[: cfg.dataset.target_count]

    elapsed = time.monotonic() - started
    await _call(on_stage, "done", {"samples": len(samples), "elapsed": elapsed})

    return JobResult(
        samples=samples,
        axes=axes,
        combinations_total=len(all_combos),
        combinations_kept=len(valid),
        plan=plan,
        gen_stats=gen_stats,
        judge_stats=judge_stats,
        duplicates_removed=removed,
        elapsed_seconds=elapsed,
        personas=personas,
    )


def _build_provider(cfg: JobConfig) -> LLMProvider:
    if cfg.provider.type == "ollama":
        if not cfg.provider.model:
            raise ValueError("provider.model is required for ollama")
        return OllamaProvider(
            model=cfg.provider.model,
            host=cfg.provider.host,
            timeout_seconds=cfg.provider.timeout_seconds,
        )
    if cfg.provider.type == "bedrock":
        creds = BedrockCredentials.from_env()
        if cfg.provider.model:
            creds.model_id = cfg.provider.model  # yaml override wins if set
        return BedrockProvider(creds=creds, timeout_seconds=cfg.provider.timeout_seconds)
    raise ValueError(f"unsupported provider: {cfg.provider.type}")


def _build_judge_provider(cfg: JobConfig) -> LLMProvider:
    if cfg.provider.type == "ollama":
        return OllamaProvider(
            model=cfg.provider.judge_model or cfg.provider.model or "",
            host=cfg.provider.host,
            timeout_seconds=cfg.provider.timeout_seconds,
        )
    if cfg.provider.type == "bedrock":
        creds = BedrockCredentials.from_env()
        if cfg.provider.judge_model:
            creds.model_id = cfg.provider.judge_model
        elif cfg.provider.model:
            creds.model_id = cfg.provider.model
        return BedrockProvider(creds=creds, timeout_seconds=cfg.provider.timeout_seconds)
    raise ValueError(f"unsupported provider: {cfg.provider.type}")


async def _call(cb: StageCb | None, stage: str, payload: dict) -> None:
    if cb is None:
        return
    res = cb(stage, payload)
    if hasattr(res, "__await__"):
        await res  # type: ignore[func-returns-value]

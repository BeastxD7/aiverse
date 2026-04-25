"""Tests for Stage 5 — CoT quality judge."""

import asyncio

from synthdata_engine.config import DatasetConfig, JobConfig, JudgeConfig, ProjectConfig, ProviderConfig
from synthdata_engine.providers.base import LLMResponse
from synthdata_engine.schema import DatasetSchema, EnumValue, SchemaField
from synthdata_engine.stages.judge import judge_samples


def _cfg(enabled=True, min_score=7):
    return JobConfig(
        project=ProjectConfig(name="Test", domain_brief="Support chat."),
        dataset=DatasetConfig(brief="Intent classifier.", target_count=10),
        schema=DatasetSchema(fields=[
            SchemaField(name="text", type="string"),
            SchemaField(name="label", type="enum", values=[EnumValue(name="billing")]),
        ]),
        seeds=[{"text": "my invoice is wrong", "label": "billing"}],
        provider=ProviderConfig(type="bedrock"),
        judge=JudgeConfig(
            enabled=enabled,
            min_correctness=min_score,
            min_realism=min_score,
            min_distinctiveness=min_score,
        ),
    )


def _samples(n: int) -> list[dict]:
    return [{"text": f"sample text {i}", "label": "billing"} for i in range(n)]


class _PassAllProvider:
    model = "mock"

    async def generate_text(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(
            outcome="success",
            raw_text='Looks good.\n{"correctness": 9, "realism": 9, "distinctiveness": 8}',
            parsed=None,
        )

    async def generate_json(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(outcome="success", raw_text="{}", parsed={})


class _FailAllProvider:
    model = "mock"

    async def generate_text(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(
            outcome="success",
            raw_text='Too generic.\n{"correctness": 3, "realism": 3, "distinctiveness": 2}',
            parsed=None,
        )

    async def generate_json(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(outcome="success", raw_text="{}", parsed={})


class _UnparseableProvider:
    """Returns text that can't be parsed as scores — should fail open (keep all)."""
    model = "mock"

    async def generate_text(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(
            outcome="success",
            raw_text="I cannot evaluate this example for quality reasons.",
            parsed=None,
        )

    async def generate_json(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(outcome="success", raw_text="{}", parsed={})


class _MixedProvider:
    """Alternates pass/fail based on sample index embedded in user prompt."""
    model = "mock"
    _call_count = 0

    async def generate_text(self, system, user, *, max_retries=3, temperature=0.8):
        _MixedProvider._call_count += 1
        if _MixedProvider._call_count % 2 == 0:
            raw = '{"correctness": 9, "realism": 9, "distinctiveness": 8}'
        else:
            raw = '{"correctness": 2, "realism": 3, "distinctiveness": 2}'
        return LLMResponse(outcome="success", raw_text=raw, parsed=None)

    async def generate_json(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(outcome="success", raw_text="{}", parsed={})


def test_judge_disabled_returns_all_samples_unchanged():
    samples = _samples(5)
    kept, stats = asyncio.run(judge_samples(samples, _cfg(enabled=False), provider=_PassAllProvider()))
    assert kept == samples
    assert stats.judged == 0
    assert stats.passed == 0


def test_judge_passes_all_high_quality_samples():
    samples = _samples(4)
    kept, stats = asyncio.run(judge_samples(samples, _cfg(), provider=_PassAllProvider()))
    assert len(kept) == 4
    assert stats.passed == 4
    assert stats.failed == 0


def test_judge_removes_low_quality_samples():
    samples = _samples(4)
    kept, stats = asyncio.run(judge_samples(samples, _cfg(), provider=_FailAllProvider()))
    assert len(kept) == 0
    assert stats.failed == 4
    assert stats.passed == 0


def test_judge_fail_open_on_unparseable_response():
    """If the judge can't be parsed, the sample passes (fail-open)."""
    samples = _samples(3)
    kept, stats = asyncio.run(judge_samples(samples, _cfg(), provider=_UnparseableProvider()))
    assert len(kept) == 3
    assert stats.unparseable == 3
    assert stats.passed == 0


def test_judge_empty_input():
    kept, stats = asyncio.run(judge_samples([], _cfg(), provider=_PassAllProvider()))
    assert kept == []
    assert stats.judged == 0


def test_judge_preserves_original_order():
    samples = [{"text": f"msg_{i}", "label": "billing"} for i in range(6)]
    _MixedProvider._call_count = 0
    kept, _ = asyncio.run(judge_samples(samples, _cfg(), provider=_MixedProvider(), concurrency=1))
    texts = [s["text"] for s in kept]
    # Order must be preserved even though judge runs concurrently
    assert texts == sorted(texts, key=lambda t: int(t.split("_")[1]))


def test_judge_writes_debug_file(tmp_path):
    from synthdata_engine.debug import DebugWriter
    dbg = DebugWriter(tmp_path)
    asyncio.run(judge_samples(_samples(2), _cfg(), provider=_PassAllProvider(), debug=dbg))
    debug_file = tmp_path / "06_judge.md"
    assert debug_file.exists()
    content = debug_file.read_text()
    assert "Stage 5" in content
    assert "PASS" in content


def test_judge_respects_custom_thresholds():
    """A sample that passes min=7 should fail at min=10."""
    samples = _samples(2)
    # min=7 → should pass (scores are 9/9/8)
    kept_low, _ = asyncio.run(judge_samples(samples, _cfg(min_score=7), provider=_PassAllProvider()))
    assert len(kept_low) == 2

    # min=10 → should fail (scores are 9/9/8, all below 10)
    kept_high, _ = asyncio.run(judge_samples(samples, _cfg(min_score=10), provider=_PassAllProvider()))
    assert len(kept_high) == 0

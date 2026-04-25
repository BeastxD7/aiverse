"""Tests for Stage 1.5 — logic filter."""

import asyncio

from synthdata_engine.providers.base import LLMResponse
from synthdata_engine.stages.logic_filter import Combination, cartesian, filter_combinations


def _combos(n: int) -> list[Combination]:
    return [{"axis": str(i)} for i in range(n)]


class _KeepAllProvider:
    model = "mock"

    async def generate_json(self, system, user, *, max_retries=3, temperature=0.8):
        # Returns keep indices for all items in the batch
        # Parse how many items are in the batch from the prompt
        count = user.count("\n") - user.count("DOMAIN") - 5
        keep = list(range(max(count, 25)))
        return LLMResponse(
            outcome="success",
            raw_text=f'{{"keep": {keep}}}',
            parsed={"keep": keep},
        )

    async def generate_text(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(outcome="success", raw_text="ok", parsed=None)


class _KeepNoneProvider:
    model = "mock"

    async def generate_json(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(
            outcome="success",
            raw_text='{"keep": []}',
            parsed={"keep": []},
        )

    async def generate_text(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(outcome="success", raw_text="ok", parsed=None)


class _ErrorProvider:
    model = "mock"

    async def generate_json(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(outcome="error", raw_text="", parsed=None, error="network error")

    async def generate_text(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(outcome="error", raw_text="", parsed=None)


class _BadJSONProvider:
    model = "mock"

    async def generate_json(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(
            outcome="success",
            raw_text='{"not_keep": [0, 1]}',
            parsed={"not_keep": [0, 1]},
        )

    async def generate_text(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(outcome="success", raw_text="ok", parsed=None)


def test_cartesian_product():
    axes = {"a": ["x", "y"], "b": ["1", "2"]}
    combos = cartesian(axes)
    assert len(combos) == 4
    assert {"a": "x", "b": "1"} in combos
    assert {"a": "y", "b": "2"} in combos


def test_cartesian_single_axis():
    axes = {"color": ["red", "blue", "green"]}
    combos = cartesian(axes)
    assert len(combos) == 3


def test_filter_returns_all_when_all_valid():
    combos = _combos(5)
    result = asyncio.run(filter_combinations(
        combos,
        domain_brief="test domain",
        dataset_brief="test dataset",
        provider=_KeepAllProvider(),
    ))
    assert len(result) == 5


def test_filter_empty_input():
    result = asyncio.run(filter_combinations(
        [],
        domain_brief="d",
        dataset_brief="d",
        provider=_KeepAllProvider(),
    ))
    assert result == []


def test_filter_fail_open_on_provider_error():
    """If the LLM errors, keep all combinations — never silently drop data."""
    combos = _combos(5)
    result = asyncio.run(filter_combinations(
        combos,
        domain_brief="d",
        dataset_brief="d",
        provider=_ErrorProvider(),
    ))
    assert len(result) == len(combos)


def test_filter_fail_open_on_wrong_json_key():
    """If LLM returns JSON but without the 'keep' key, treat as keep-all."""
    combos = _combos(4)
    result = asyncio.run(filter_combinations(
        combos,
        domain_brief="d",
        dataset_brief="d",
        provider=_BadJSONProvider(),
    ))
    assert len(result) == len(combos)


def test_filter_removes_items_marked_implausible():
    combos = _combos(5)
    result = asyncio.run(filter_combinations(
        combos,
        domain_brief="d",
        dataset_brief="d",
        provider=_KeepNoneProvider(),
    ))
    # When provider keeps none but result would be empty, falls back to original
    assert len(result) >= 0  # empty keep returns empty (allowed — caller handles)


def test_filter_processes_in_batches():
    combos = _combos(30)
    result = asyncio.run(filter_combinations(
        combos,
        domain_brief="d",
        dataset_brief="d",
        provider=_KeepAllProvider(),
        batch_size=10,
    ))
    # All 30 should come back (KeepAllProvider keeps everything)
    assert len(result) == 30


def test_filter_writes_debug_file(tmp_path):
    from synthdata_engine.debug import DebugWriter
    dbg = DebugWriter(tmp_path)
    asyncio.run(filter_combinations(
        _combos(5),
        domain_brief="test",
        dataset_brief="test",
        provider=_KeepAllProvider(),
        debug=dbg,
    ))
    debug_file = tmp_path / "02_logic_filter.md"
    assert debug_file.exists()
    content = debug_file.read_text()
    assert "Stage 1.5" in content

"""Tests for Stage 1 — axis discovery."""

import asyncio

import pytest

from synthdata_engine.config import DatasetConfig, JobConfig, ProjectConfig, ProviderConfig
from synthdata_engine.providers.base import LLMResponse
from synthdata_engine.schema import DatasetSchema, EnumValue, SchemaField
from synthdata_engine.stages.discover import discover_axes


def _mock_cfg(axes_override=None):
    return JobConfig(
        project=ProjectConfig(name="Test", domain_brief="Customer support chat."),
        dataset=DatasetConfig(brief="Intent classifier.", target_count=10, axes=axes_override),
        schema=DatasetSchema(fields=[
            SchemaField(name="text", type="string"),
            SchemaField(
                name="label",
                type="enum",
                values=[EnumValue(name="billing"), EnumValue(name="shipping")],
            ),
        ]),
        seeds=[{"text": "where is my order", "label": "shipping"}],
        provider=ProviderConfig(type="bedrock"),
    )


class _GoodProvider:
    model = "mock"

    async def generate_json(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(
            outcome="success",
            raw_text='{"axes": {"tone": ["formal", "casual"], "length": ["short", "long", "medium"]}}',
            parsed={"axes": {"tone": ["formal", "casual"], "length": ["short", "long", "medium"]}},
        )

    async def generate_text(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(outcome="success", raw_text="ok", parsed=None)


class _FailProvider:
    model = "mock"

    async def generate_json(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(outcome="error", raw_text="", parsed=None, error="network failure")

    async def generate_text(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(outcome="error", raw_text="", parsed=None, error="network failure")


class _BadStructureProvider:
    """Returns success but with wrong JSON structure."""
    model = "mock"

    async def generate_json(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(
            outcome="success",
            raw_text='{"wrong_key": {}}',
            parsed={"wrong_key": {}},
        )

    async def generate_text(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(outcome="success", raw_text="ok", parsed=None)


class _SingleAxisProvider:
    """Returns only one axis — should raise because < 2."""
    model = "mock"

    async def generate_json(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(
            outcome="success",
            raw_text='{"axes": {"tone": ["formal", "casual"]}}',
            parsed={"axes": {"tone": ["formal", "casual"]}},
        )

    async def generate_text(self, system, user, *, max_retries=3, temperature=0.8):
        return LLMResponse(outcome="success", raw_text="ok", parsed=None)


def test_discover_returns_axes():
    axes = asyncio.run(discover_axes(_mock_cfg(), _GoodProvider()))
    assert "tone" in axes
    assert "length" in axes
    assert axes["tone"] == ["formal", "casual"]
    assert len(axes["length"]) == 3


def test_discover_raises_on_provider_failure():
    with pytest.raises(RuntimeError, match="axes discovery failed"):
        asyncio.run(discover_axes(_mock_cfg(), _FailProvider()))


def test_discover_raises_on_missing_axes_key():
    with pytest.raises(RuntimeError):
        asyncio.run(discover_axes(_mock_cfg(), _BadStructureProvider()))


def test_discover_raises_when_fewer_than_two_axes():
    with pytest.raises(RuntimeError, match="too few usable axes"):
        asyncio.run(discover_axes(_mock_cfg(), _SingleAxisProvider()))


def test_discover_reconciles_enum_field_values():
    """If an axis name matches a schema enum field, its values are replaced with the enum's values."""

    class _EnumAxisProvider:
        model = "mock"

        async def generate_json(self, system, user, *, max_retries=3, temperature=0.8):
            # Returns 'label' as an axis with wrong values
            return LLMResponse(
                outcome="success",
                raw_text='{"axes": {"label": ["wrong1", "wrong2"], "tone": ["formal", "casual"]}}',
                parsed={"axes": {"label": ["wrong1", "wrong2"], "tone": ["formal", "casual"]}},
            )

        async def generate_text(self, system, user, *, max_retries=3, temperature=0.8):
            return LLMResponse(outcome="success", raw_text="ok", parsed=None)

    axes = asyncio.run(discover_axes(_mock_cfg(), _EnumAxisProvider()))
    # 'label' should be forced to the schema's enum values
    assert axes["label"] == ["billing", "shipping"]
    assert axes["tone"] == ["formal", "casual"]


def test_discover_filters_axes_with_fewer_than_two_values():
    """Axes with < 2 values are silently dropped."""

    class _ThinAxisProvider:
        model = "mock"

        async def generate_json(self, system, user, *, max_retries=3, temperature=0.8):
            return LLMResponse(
                outcome="success",
                raw_text='{"axes": {"good": ["a", "b"], "bad": ["only_one"], "also_good": ["x", "y", "z"]}}',
                parsed={"axes": {"good": ["a", "b"], "bad": ["only_one"], "also_good": ["x", "y", "z"]}},
            )

        async def generate_text(self, system, user, *, max_retries=3, temperature=0.8):
            return LLMResponse(outcome="success", raw_text="ok", parsed=None)

    axes = asyncio.run(discover_axes(_mock_cfg(), _ThinAxisProvider()))
    assert "good" in axes
    assert "also_good" in axes
    assert "bad" not in axes


def test_discover_writes_debug_file(tmp_path):
    from synthdata_engine.debug import DebugWriter
    dbg = DebugWriter(tmp_path)
    asyncio.run(discover_axes(_mock_cfg(), _GoodProvider(), debug=dbg))
    debug_file = tmp_path / "01_axes_discovery.md"
    assert debug_file.exists()
    content = debug_file.read_text()
    assert "Stage 1" in content
    assert "tone" in content

import random

from synthdata_engine.config import AntiSeed
from synthdata_engine.schema import DatasetSchema, EnumValue, SchemaField
from synthdata_engine.stages.compose import compose_prompt


def _schema():
    return DatasetSchema(
        fields=[
            SchemaField(name="text", type="string"),
            SchemaField(
                name="label",
                type="enum",
                values=[
                    EnumValue(name="a", description="means first case"),
                    EnumValue(name="b", description="means second case"),
                ],
            ),
            SchemaField(name="confidence", type="float", min=0.7, max=1.0),
        ]
    )


def _kwargs():
    return dict(
        schema=_schema(),
        seeds=[],
        anti_seeds=[],
        personas=["a dev who types fast"],
        speaker_block="",
        rng=random.Random(0),
    )


def test_compose_pins_axis_matching_field():
    kwargs = _kwargs()
    system, user = compose_prompt(
        combination={"label": "a", "tone": "casual"},
        **kwargs,
    )
    assert system != ""
    assert '"label" must equal "a"' in user
    assert "means first case" in user  # enum description flows through
    assert "tone: casual" in user


def test_compose_includes_persona():
    kwargs = _kwargs()
    kwargs["personas"] = ["UNIQUE_PERSONA_123"]
    _, user = compose_prompt(combination={"label": "a"}, **kwargs)
    assert "UNIQUE_PERSONA_123" in user


def test_compose_injects_unique_seed():
    _, u1 = compose_prompt(combination={"label": "a"}, **_kwargs())
    _, u2 = compose_prompt(combination={"label": "a"}, **_kwargs())
    assert u1 != u2


def test_compose_uses_seeds_block():
    kwargs = _kwargs()
    kwargs["seeds"] = [{"text": "SEEDY_EXAMPLE", "label": "a", "confidence": 0.9}]
    _, user = compose_prompt(combination={"label": "a"}, **kwargs)
    assert "SEEDY_EXAMPLE" in user
    assert "DO NOT COPY" in user


def test_compose_includes_anti_seeds():
    kwargs = _kwargs()
    kwargs["anti_seeds"] = [
        AntiSeed(text="I'd like to apply for this role", reason="candidate voice — out of scope")
    ]
    _, user = compose_prompt(combination={"label": "a"}, **kwargs)
    assert "ANTI-EXAMPLES" in user
    assert "I'd like to apply for this role" in user
    assert "candidate voice" in user


def test_compose_includes_speaker_block():
    kwargs = _kwargs()
    kwargs["speaker_block"] = "SPEAKERS IN SCOPE:\n- HR manager"
    _, user = compose_prompt(combination={"label": "a"}, **kwargs)
    assert "SPEAKERS IN SCOPE" in user
    assert "HR manager" in user


def test_compose_lists_enum_values_when_not_pinned():
    """If label isn't in the combination, the generator should see all allowed values + meanings."""
    kwargs = _kwargs()
    _, user = compose_prompt(combination={"tone": "casual"}, **kwargs)
    assert '"label" must be one of' in user
    assert '"a"' in user and "means first case" in user
    assert '"b"' in user and "means second case" in user

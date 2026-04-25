"""Tests for quality gate and distribution report."""

from synthdata_engine.config import DatasetConfig
from synthdata_engine.quality import FieldDistribution, apply_quality_gate, compute_report
from synthdata_engine.schema import DatasetSchema, EnumValue, SchemaField


def _schema():
    return DatasetSchema(fields=[
        SchemaField(name="text", type="string"),
        SchemaField(name="label", type="enum", values=[
            EnumValue(name="happy"),
            EnumValue(name="sad"),
            EnumValue(name="angry"),
            EnumValue(name="out_of_scope"),
        ]),
        SchemaField(name="confidence", type="float", min=0.7, max=1.0),
    ])


def _dataset_cfg(**kwargs):
    defaults = dict(brief="test", target_count=10, min_text_chars=10, max_text_chars=500)
    defaults.update(kwargs)
    return DatasetConfig(**defaults)


def _samples(n: int, label="happy", conf=0.9) -> list[dict]:
    return [{"text": f"sample text number {i} is here", "label": label, "confidence": conf} for i in range(n)]


# --- apply_quality_gate ---

def test_gate_keeps_all_within_bounds():
    samples = _samples(5)
    kept, removed = apply_quality_gate(samples, _dataset_cfg(), _schema())
    assert kept == samples
    assert removed == 0


def test_gate_removes_too_short():
    samples = [{"text": "hi", "label": "happy", "confidence": 0.9}]
    kept, removed = apply_quality_gate(samples, _dataset_cfg(min_text_chars=10), _schema())
    assert len(kept) == 0
    assert removed == 1


def test_gate_removes_too_long():
    samples = [{"text": "x" * 600, "label": "happy", "confidence": 0.9}]
    kept, removed = apply_quality_gate(samples, _dataset_cfg(max_text_chars=500), _schema())
    assert len(kept) == 0
    assert removed == 1


def test_gate_empty_input():
    kept, removed = apply_quality_gate([], _dataset_cfg(), _schema())
    assert kept == []
    assert removed == 0


def test_gate_no_string_fields():
    schema = DatasetSchema(fields=[
        SchemaField(name="label", type="enum", values=[EnumValue(name="a")]),
    ])
    samples = [{"label": "a"}]
    kept, removed = apply_quality_gate(samples, _dataset_cfg(), schema)
    assert kept == samples
    assert removed == 0


# --- compute_report ---

def test_report_enum_counts_correct():
    samples = (
        _samples(3, label="happy") +
        _samples(4, label="sad") +
        _samples(2, label="angry") +
        _samples(1, label="out_of_scope")
    )
    report = compute_report(samples, _schema())
    label_dist = next(d for d in report.field_distributions if d.name == "label")
    assert label_dist.counts["happy"] == 3
    assert label_dist.counts["sad"] == 4
    assert label_dist.counts["angry"] == 2
    assert label_dist.counts["out_of_scope"] == 1


def test_report_critical_warning_for_zero_class():
    samples = _samples(10, label="happy")  # all happy, nothing else
    report = compute_report(samples, _schema())
    assert any("CRITICAL" in w and "sad" in w for w in report.imbalance_warnings)
    assert any("CRITICAL" in w and "angry" in w for w in report.imbalance_warnings)
    assert any("CRITICAL" in w and "out_of_scope" in w for w in report.imbalance_warnings)


def test_report_warning_for_underrepresented_class():
    # 20 samples, 4 classes, expected=5. Threshold is 60% = 3.0. angry=2, out_of_scope=1 both trigger.
    samples = (
        _samples(9, label="happy") +
        _samples(8, label="sad") +
        _samples(2, label="angry") +
        _samples(1, label="out_of_scope")
    )
    report = compute_report(samples, _schema())
    warning_fields = " ".join(report.imbalance_warnings)
    assert "out_of_scope" in warning_fields or "angry" in warning_fields


def test_report_no_warnings_for_balanced_data():
    samples = (
        _samples(5, label="happy") +
        _samples(5, label="sad") +
        _samples(5, label="angry") +
        _samples(5, label="out_of_scope")
    )
    report = compute_report(samples, _schema())
    assert report.imbalance_warnings == []


def test_report_float_field_stats():
    samples = [
        {"text": "some text here", "label": "happy", "confidence": 0.7},
        {"text": "some text here", "label": "happy", "confidence": 0.9},
        {"text": "some text here", "label": "happy", "confidence": 1.0},
    ]
    report = compute_report(samples, _schema())
    conf_dist = next(d for d in report.field_distributions if d.name == "confidence")
    assert conf_dist.min_val == 0.7
    assert conf_dist.max_val == 1.0
    assert abs(conf_dist.mean_val - 0.8667) < 0.001
    assert conf_dist.is_char_count is False


def test_report_string_field_is_char_count():
    samples = _samples(3)
    report = compute_report(samples, _schema())
    text_dist = next(d for d in report.field_distributions if d.name == "text")
    assert text_dist.is_char_count is True
    assert text_dist.min_val is not None


def test_report_empty_samples():
    report = compute_report([], _schema())
    assert report.total_samples == 0
    assert report.imbalance_warnings == []


def test_report_total_and_filtered():
    samples = _samples(8)
    report = compute_report(samples, _schema(), length_filtered=2)
    assert report.total_samples == 8
    assert report.filtered_by_length == 2


def test_report_as_dict_structure():
    samples = _samples(4)
    report = compute_report(samples, _schema())
    d = report.as_dict()
    assert "total_samples" in d
    assert "field_distributions" in d
    assert "imbalance_warnings" in d
    assert isinstance(d["field_distributions"], list)

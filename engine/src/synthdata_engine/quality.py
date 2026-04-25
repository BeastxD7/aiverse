"""Post-generation quality gates and distribution analytics.

Runs after Stage 6 (dedup). Applies text length filters and computes a
distribution report over every enum and numeric field.
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass, field

from .config import DatasetConfig
from .schema import DatasetSchema, SchemaField, extract_strings


@dataclass
class FieldDistribution:
    name: str
    counts: dict[str, int] = field(default_factory=dict)       # enum fields
    min_val: float | None = None                                # numeric fields
    max_val: float | None = None
    mean_val: float | None = None
    missing: int = 0
    is_char_count: bool = False                                  # True for string length stats


@dataclass
class QualityReport:
    total_samples: int
    filtered_by_length: int
    field_distributions: list[FieldDistribution]
    imbalance_warnings: list[str]

    def has_warnings(self) -> bool:
        return bool(self.imbalance_warnings)

    def as_dict(self) -> dict:
        return {
            "total_samples": self.total_samples,
            "filtered_by_length": self.filtered_by_length,
            "field_distributions": [
                {
                    "name": d.name,
                    **({"counts": d.counts} if d.counts else {}),
                    **({"min": d.min_val, "max": d.max_val, "mean": round(d.mean_val, 3) if d.mean_val is not None else None}
                       if d.min_val is not None else {}),
                    "missing": d.missing,
                }
                for d in self.field_distributions
            ],
            "imbalance_warnings": self.imbalance_warnings,
        }


def apply_quality_gate(
    samples: list[dict],
    cfg_dataset: DatasetConfig,
    schema: DatasetSchema,
) -> tuple[list[dict], int]:
    """Filter samples that fail length constraints. Returns (kept, removed_count)."""
    kept: list[dict] = []
    removed = 0
    for row in samples:
        strings = extract_strings(row, schema.fields)
        if not strings:
            kept.append(row)
            continue
        text = " ".join(strings).strip()
        length = len(text)
        if length < cfg_dataset.min_text_chars or length > cfg_dataset.max_text_chars:
            removed += 1
        else:
            kept.append(row)
    return kept, removed


def compute_report(
    samples: list[dict],
    schema: DatasetSchema,
    length_filtered: int = 0,
) -> QualityReport:
    """Compute distribution over all schema fields."""
    distributions: list[FieldDistribution] = []
    warnings: list[str] = []

    for f in schema.fields:
        dist = FieldDistribution(name=f.name)
        values = [row.get(f.name) for row in samples]
        missing = sum(1 for v in values if v is None)
        dist.missing = missing

        if f.type == "enum" and f.values:
            for ev in f.values:
                dist.counts[ev.name] = sum(1 for v in values if v == ev.name)

            # Warn if any class is below 50% of expected even share
            if samples:
                num_classes = len(f.values)
                expected = len(samples) / num_classes
                for ev in f.values:
                    actual = dist.counts.get(ev.name, 0)
                    if actual == 0:
                        warnings.append(
                            f"CRITICAL: field '{f.name}' value '{ev.name}' has 0 samples — "
                            "class completely absent. Enable require_balanced: true to fix."
                        )
                    elif actual < expected * 0.6:
                        warnings.append(
                            f"WARNING: field '{f.name}' value '{ev.name}' has only {actual} samples "
                            f"(expected ~{expected:.0f}, below 60% of fair share). "
                            "Consider require_balanced: true."
                        )

        elif f.type in ("float", "integer"):
            nums = [v for v in values if isinstance(v, (int, float)) and not isinstance(v, bool)]
            if nums:
                dist.min_val = float(min(nums))
                dist.max_val = float(max(nums))
                dist.mean_val = statistics.mean(nums)

        elif f.type == "string":
            lengths = [len(str(row.get(f.name, ""))) for row in samples]
            if lengths:
                dist.min_val = float(min(lengths))
                dist.max_val = float(max(lengths))
                dist.mean_val = statistics.mean(lengths)
                dist.is_char_count = True

        distributions.append(dist)

    return QualityReport(
        total_samples=len(samples),
        filtered_by_length=length_filtered,
        field_distributions=distributions,
        imbalance_warnings=warnings,
    )

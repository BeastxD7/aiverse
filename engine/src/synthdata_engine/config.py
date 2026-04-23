"""Job config loaded from YAML."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, Field

from .schema import DatasetSchema


class Speakers(BaseModel):
    """Which user types may / may not appear as authors of generated examples.

    `in_scope` grounds Stage 1 axis discovery and persona generation.
    `out_of_scope` is a hard prohibition — those personas must never appear.
    """

    in_scope: list[str] = Field(default_factory=list)
    out_of_scope: list[str] = Field(default_factory=list)

    def as_prompt_block(self) -> str:
        if not self.in_scope and not self.out_of_scope:
            return ""
        lines = []
        if self.in_scope:
            lines.append("SPEAKERS IN SCOPE (messages originate from these users):")
            lines.extend(f"- {s}" for s in self.in_scope)
        if self.out_of_scope:
            lines.append("SPEAKERS OUT OF SCOPE (NEVER generate a message from these):")
            lines.extend(f"- {s}" for s in self.out_of_scope)
        return "\n".join(lines)


class ProjectConfig(BaseModel):
    name: str
    domain_brief: str
    speakers: Speakers = Field(default_factory=Speakers)


class DatasetConfig(BaseModel):
    brief: str
    target_count: int = Field(ge=1, le=100_000)
    diversity: Literal["standard", "high", "edge_cases"] = "standard"
    persona_pool_size: int = Field(default=40, ge=5, le=200)


class ProviderConfig(BaseModel):
    """Provider settings.

    For `type: bedrock`, model/credentials/region come from env vars
    (AWS_MODEL_ID / AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY / AWS_REGION).
    The `model` field is optional for bedrock — env wins if both are set.
    """

    type: Literal["ollama", "bedrock"] = "ollama"
    model: str | None = None
    judge_model: str | None = None
    concurrency: int = Field(default=5, ge=1, le=50)
    timeout_seconds: int = Field(default=300, ge=5, le=900)
    host: str = "http://localhost:11434"  # ignored for bedrock


class DedupConfig(BaseModel):
    threshold: float = Field(default=0.85, ge=0.1, le=1.0)
    num_perm: int = 128


class JudgeConfig(BaseModel):
    enabled: bool = False
    min_correctness: int = 7
    min_realism: int = 7
    min_distinctiveness: int = 7


class LogicFilterConfig(BaseModel):
    enabled: bool = True
    batch_size: int = Field(default=25, ge=5, le=100)


class AntiSeed(BaseModel):
    """A negative example — text that must NEVER be generated, with the reason."""

    text: str
    reason: str


class JobConfig(BaseModel):
    project: ProjectConfig
    dataset: DatasetConfig
    dataset_schema: DatasetSchema = Field(alias="schema")
    seeds: list[dict[str, Any]] = Field(min_length=1, max_length=10)
    anti_seeds: list[AntiSeed] = Field(default_factory=list, max_length=10)
    provider: ProviderConfig
    dedup: DedupConfig = DedupConfig()
    judge: JudgeConfig = JudgeConfig()
    logic_filter: LogicFilterConfig = LogicFilterConfig()

    model_config = {"populate_by_name": True}


def load_config(path: str | Path) -> JobConfig:
    raw = yaml.safe_load(Path(path).read_text())
    cfg = JobConfig.model_validate(raw)
    for i, seed in enumerate(cfg.seeds):
        ok, errs = cfg.dataset_schema.validate_row(seed)
        if not ok:
            raise ValueError(f"seed example #{i} fails schema: {errs}")
    return cfg

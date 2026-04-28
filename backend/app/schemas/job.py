import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from ..models.job import JobStatus


class JobCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    output_format: str = Field(default="jsonl", pattern="^(jsonl|json|csv)$")
    config: dict[str, Any]  # validated against engine's JobConfig on create


class JobOut(BaseModel):
    model_config = {"from_attributes": True}

    id: uuid.UUID
    name: str
    status: JobStatus
    output_format: str
    output_row_count: int | None
    credits_reserved: int
    credits_used: int
    started_at: datetime | None
    completed_at: datetime | None
    elapsed_seconds: float | None
    error_message: str | None
    created_at: datetime


class JobListOut(BaseModel):
    model_config = {"from_attributes": True}

    id: uuid.UUID
    name: str
    status: JobStatus
    output_row_count: int | None
    credits_used: int
    elapsed_seconds: float | None
    created_at: datetime


class JobEventOut(BaseModel):
    model_config = {"from_attributes": True}

    sequence: int
    event_type: str
    stage: str
    payload: dict[str, Any]

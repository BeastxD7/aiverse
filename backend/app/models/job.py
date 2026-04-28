import uuid
from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import DateTime, Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSON, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin, UUIDPrimaryKey


class JobStatus(str, PyEnum):
    created = "created"
    queued = "queued"
    running = "running"
    completed = "completed"
    failed = "failed"
    cancelled = "cancelled"


class Job(Base, UUIDPrimaryKey, TimestampMixin):
    __tablename__ = "jobs"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[JobStatus] = mapped_column(Enum(JobStatus), default=JobStatus.created, nullable=False, index=True)

    # Full config snapshot — immutable after creation; never mutated
    config_snapshot: Mapped[dict] = mapped_column(JSON, nullable=False)

    output_format: Mapped[str] = mapped_column(String(10), default="jsonl", nullable=False)
    output_path: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    output_row_count: Mapped[int | None] = mapped_column(Integer, nullable=True)

    credits_reserved: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    credits_used: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    elapsed_seconds: Mapped[float | None] = mapped_column(Float, nullable=True)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="jobs")  # type: ignore[name-defined]
    events: Mapped[list["JobEvent"]] = relationship(
        "JobEvent", back_populates="job", order_by="JobEvent.sequence", cascade="all, delete-orphan"
    )
    credit_transactions: Mapped[list["CreditTransaction"]] = relationship(  # type: ignore[name-defined]
        "CreditTransaction", back_populates="job"
    )


class JobEvent(Base, UUIDPrimaryKey):
    """Append-only log of every on_stage / on_progress event — used for SSE replay."""
    __tablename__ = "job_events"

    job_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False, index=True
    )
    sequence: Mapped[int] = mapped_column(Integer, nullable=False)
    event_type: Mapped[str] = mapped_column(String(50), nullable=False)  # "stage" | "progress" | "done" | "error"
    stage: Mapped[str] = mapped_column(String(100), nullable=False)
    payload: Mapped[dict] = mapped_column(JSON, nullable=False)

    job: Mapped["Job"] = relationship("Job", back_populates="events")

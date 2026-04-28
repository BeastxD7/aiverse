import uuid
from enum import Enum as PyEnum

from sqlalchemy import Enum, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin, UUIDPrimaryKey


class TransactionType(str, PyEnum):
    grant = "grant"       # admin grants or signup bonus
    debit = "debit"       # job completed — actual cost charged
    reserve = "reserve"   # credits held when job starts
    refund = "refund"     # returned on job failure or overshoot


class CreditTransaction(Base, UUIDPrimaryKey, TimestampMixin):
    __tablename__ = "credit_transactions"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    type: Mapped[TransactionType] = mapped_column(Enum(TransactionType), nullable=False)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)  # positive = added, negative = removed
    balance_after: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    job_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True), ForeignKey("jobs.id", ondelete="SET NULL"), nullable=True, index=True
    )

    user: Mapped["User"] = relationship(  # type: ignore[name-defined]
        "User", back_populates="credit_transactions", foreign_keys=[user_id]
    )
    job: Mapped["Job | None"] = relationship("Job", back_populates="credit_transactions")  # type: ignore[name-defined]


class CreditSetting(Base, UUIDPrimaryKey, TimestampMixin):
    """Admin-configurable credit pricing knobs."""
    __tablename__ = "credit_settings"

    key: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    value: Mapped[str] = mapped_column(String(500), nullable=False)  # stored as string, cast at use
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    updated_by: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )


# Default keys and values — seeded on first run
CREDIT_SETTING_DEFAULTS: dict[str, tuple[str, str]] = {
    "credits_per_sample":      ("1",   "Credits charged per generated sample"),
    "free_credits_on_signup":  ("100", "Credits granted to every new user on registration"),
    "min_credits_per_job":     ("5",   "Minimum credits charged per job regardless of output size"),
}

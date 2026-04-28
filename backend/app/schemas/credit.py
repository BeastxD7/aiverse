import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class CreditBalanceOut(BaseModel):
    credits: int


class CreditTransactionOut(BaseModel):
    model_config = {"from_attributes": True}

    id: uuid.UUID
    type: str
    amount: int
    balance_after: int
    description: str | None
    job_id: uuid.UUID | None
    created_at: datetime


class CreditSettingOut(BaseModel):
    model_config = {"from_attributes": True}

    key: str
    value: str
    description: str | None
    updated_at: datetime


class CreditSettingUpdate(BaseModel):
    value: str = Field(min_length=1, max_length=500)

import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.credit import CREDIT_SETTING_DEFAULTS, CreditSetting, CreditTransaction, TransactionType
from ..models.user import User
from ..utils.errors import NotFoundError


class CreditService:
    def __init__(self, db: AsyncSession):
        self.db = db

    # --- Settings ---

    async def get_setting(self, key: str) -> int:
        result = await self.db.execute(select(CreditSetting).where(CreditSetting.key == key))
        row = result.scalar_one_or_none()
        if row:
            return int(row.value)
        default = CREDIT_SETTING_DEFAULTS.get(key)
        return int(default[0]) if default else 0

    async def set_setting(self, key: str, value: str, updated_by: uuid.UUID) -> CreditSetting:
        result = await self.db.execute(select(CreditSetting).where(CreditSetting.key == key))
        row = result.scalar_one_or_none()
        if not row:
            raise NotFoundError(f"Setting '{key}'")
        row.value = value
        row.updated_by = updated_by
        await self.db.commit()
        await self.db.refresh(row)
        return row

    async def list_settings(self) -> list[CreditSetting]:
        result = await self.db.execute(select(CreditSetting))
        return list(result.scalars().all())

    async def seed_defaults(self) -> None:
        """Insert default settings if they don't exist. Called on startup."""
        for key, (value, description) in CREDIT_SETTING_DEFAULTS.items():
            exists = await self.db.execute(select(CreditSetting).where(CreditSetting.key == key))
            if not exists.scalar_one_or_none():
                self.db.add(CreditSetting(key=key, value=value, description=description))
        await self.db.commit()

    # --- Transactions ---

    async def grant_signup_credits(self, user: User) -> None:
        amount = await self.get_setting("free_credits_on_signup")
        if amount <= 0:
            return
        await self._record(user, TransactionType.grant, amount, "Welcome bonus — free credits on signup")

    async def estimate_job_cost(self, target_count: int) -> int:
        per_sample = await self.get_setting("credits_per_sample")
        minimum = await self.get_setting("min_credits_per_job")
        return max(minimum, target_count * per_sample)

    async def reserve(self, user: User, amount: int, job_id: uuid.UUID) -> None:
        """Hold credits when a job starts. Fails if balance is insufficient."""
        from ..utils.errors import InsufficientCreditsError
        if user.credits < amount:
            raise InsufficientCreditsError(required=amount, available=user.credits)
        await self._record(user, TransactionType.reserve, -amount, "Credits reserved for job", job_id)

    async def finalize(self, user: User, reserved: int, actual: int, job_id: uuid.UUID) -> int:
        """Settle actual cost after job completes. Refunds any overshoot."""
        per_sample = await self.get_setting("credits_per_sample")
        minimum = await self.get_setting("min_credits_per_job")
        actual_cost = max(minimum, actual * per_sample)

        await self._record(user, TransactionType.debit, -actual_cost, "Job completed", job_id)

        overshoot = reserved - actual_cost
        if overshoot > 0:
            await self._record(user, TransactionType.refund, overshoot, "Unused reserved credits returned", job_id)

        return actual_cost

    async def refund(self, user: User, amount: int, job_id: uuid.UUID) -> None:
        """Full refund on job failure."""
        if amount > 0:
            await self._record(user, TransactionType.refund, amount, "Job failed — credits refunded", job_id)

    async def list_transactions(self, user_id: uuid.UUID, limit: int = 50, offset: int = 0) -> list[CreditTransaction]:
        result = await self.db.execute(
            select(CreditTransaction)
            .where(CreditTransaction.user_id == user_id)
            .order_by(CreditTransaction.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
        return list(result.scalars().all())

    # --- Internal ---

    async def _record(
        self,
        user: User,
        type_: TransactionType,
        amount: int,
        description: str,
        job_id: uuid.UUID | None = None,
    ) -> CreditTransaction:
        user.credits += amount
        tx = CreditTransaction(
            user_id=user.id,
            type=type_,
            amount=amount,
            balance_after=user.credits,
            description=description,
            job_id=job_id,
        )
        self.db.add(tx)
        return tx

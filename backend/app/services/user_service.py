import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.user import User
from ..core.security import hash_password
from ..utils.errors import NotFoundError


class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, user_id: uuid.UUID) -> User:
        result = await self.db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            raise NotFoundError("User")
        return user

    async def update(self, user: User, name: str | None, password: str | None) -> User:
        if name is not None:
            user.name = name
        if password is not None:
            user.hashed_password = hash_password(password)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def deactivate(self, user: User) -> None:
        user.is_active = False
        await self.db.commit()

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.database import get_db
from ..core.dependencies import get_current_user
from ..models.user import User
from ..schemas.user import UserOut, UserUpdate
from ..services.user_service import UserService
from ..utils.response import ApiResponse, api_success

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=ApiResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    return api_success(data=UserOut.model_validate(current_user))


@router.patch("/me", response_model=ApiResponse)
async def update_me(
    body: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    svc = UserService(db)
    user = await svc.update(current_user, body.name, body.password)
    return api_success(data=UserOut.model_validate(user), message="Profile updated")


@router.delete("/me", response_model=ApiResponse)
async def delete_me(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    svc = UserService(db)
    await svc.deactivate(current_user)
    return api_success(message="Account deactivated")

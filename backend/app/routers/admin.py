"""Admin-only routes — credit settings management."""

import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.database import get_db
from ..core.dependencies import require_admin
from ..models.user import User
from ..schemas.credit import CreditSettingOut, CreditSettingUpdate
from ..services.credit_service import CreditService
from ..utils.response import ApiResponse, api_success

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/credit-settings", response_model=ApiResponse)
async def list_credit_settings(
    _: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    svc = CreditService(db)
    settings = await svc.list_settings()
    return api_success(data=[CreditSettingOut.model_validate(s) for s in settings])


@router.patch("/credit-settings/{key}", response_model=ApiResponse)
async def update_credit_setting(
    key: str,
    body: CreditSettingUpdate,
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    svc = CreditService(db)
    setting = await svc.set_setting(key, body.value, admin.id)
    return api_success(
        data=CreditSettingOut.model_validate(setting),
        message=f"Setting '{key}' updated",
    )

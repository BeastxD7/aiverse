from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.database import get_db
from ..core.dependencies import get_current_user
from ..models.user import User
from ..schemas.credit import CreditBalanceOut, CreditTransactionOut
from ..services.credit_service import CreditService
from ..utils.pagination import PageParams, PaginatedData
from ..utils.response import ApiResponse, api_success

router = APIRouter(prefix="/credits", tags=["credits"])


@router.get("/balance", response_model=ApiResponse)
async def get_balance(current_user: User = Depends(get_current_user)):
    return api_success(data=CreditBalanceOut(credits=current_user.credits))


@router.get("/transactions", response_model=ApiResponse)
async def list_transactions(
    params: PageParams = Depends(),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    svc = CreditService(db)
    txns = await svc.list_transactions(current_user.id, limit=params.limit, offset=params.offset)
    out = [CreditTransactionOut.model_validate(t) for t in txns]
    return api_success(data=out)

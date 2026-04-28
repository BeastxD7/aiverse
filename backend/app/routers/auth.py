from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.database import get_db
from ..schemas.auth import LoginRequest, LoginResponse, RefreshRequest, RegisterRequest, TokenPair
from ..services.auth_service import AuthService
from ..utils.response import ApiResponse, api_success

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=ApiResponse, status_code=201)
async def register(body: RegisterRequest, db: AsyncSession = Depends(get_db)):
    svc = AuthService(db)
    user, access_token, refresh_token = await svc.register(body.name, body.email, body.password)
    return api_success(
        data=LoginResponse(
            user_id=str(user.id),
            name=user.name,
            email=user.email,
            role=user.role,
            credits=user.credits,
            tokens=TokenPair(access_token=access_token, refresh_token=refresh_token),
        ),
        message="Account created successfully",
    )


@router.post("/login", response_model=ApiResponse)
async def login(body: LoginRequest, db: AsyncSession = Depends(get_db)):
    svc = AuthService(db)
    user, access_token, refresh_token = await svc.login(body.email, body.password)
    return api_success(
        data=LoginResponse(
            user_id=str(user.id),
            name=user.name,
            email=user.email,
            role=user.role,
            credits=user.credits,
            tokens=TokenPair(access_token=access_token, refresh_token=refresh_token),
        ),
        message="Logged in successfully",
    )


@router.post("/refresh", response_model=ApiResponse)
async def refresh(body: RefreshRequest, db: AsyncSession = Depends(get_db)):
    svc = AuthService(db)
    access_token, new_refresh_token = await svc.refresh(body.refresh_token)
    return api_success(
        data=TokenPair(access_token=access_token, refresh_token=new_refresh_token),
        message="Tokens refreshed",
    )


@router.post("/logout", response_model=ApiResponse)
async def logout(body: RefreshRequest, db: AsyncSession = Depends(get_db)):
    svc = AuthService(db)
    await svc.logout(body.refresh_token)
    return api_success(message="Logged out successfully")

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .core.config import settings
from .core.database import AsyncSessionLocal
from .routers import admin, auth, credits, jobs, users
from .services.credit_service import CreditService
from .utils.errors import AppError
from .utils.response import api_error


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Seed default credit settings on startup
    async with AsyncSessionLocal() as db:
        await CreditService(db).seed_defaults()
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    lifespan=lifespan,
)

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Exception handlers ---

@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content=api_error(message=exc.message, error={"code": exc.code}).model_dump(),
    )


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content=api_error(
            message="Validation error",
            error={"code": "VALIDATION_ERROR", "detail": exc.errors()},
        ).model_dump(),
    )


@app.exception_handler(Exception)
async def unhandled_error_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content=api_error(
            message="Internal server error",
            error={"code": "INTERNAL_ERROR"},
        ).model_dump(),
    )


# --- Routers ---
PREFIX = "/api/v1"
app.include_router(auth.router, prefix=PREFIX)
app.include_router(users.router, prefix=PREFIX)
app.include_router(credits.router, prefix=PREFIX)
app.include_router(jobs.router, prefix=PREFIX)
app.include_router(admin.router, prefix=PREFIX)


@app.get("/health")
async def health():
    return {"status": "ok", "version": "0.1.0"}

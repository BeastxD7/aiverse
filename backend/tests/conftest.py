"""Shared fixtures for all test modules."""

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.database import get_db
from app.core.security import hash_password
from app.main import app
from app.models import Base
from app.models.user import User, UserRole

TEST_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/synthdata_test"

test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestSessionLocal = async_sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)


@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_db():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def db():
    async with TestSessionLocal() as session:
        yield session
        await session.rollback()


@pytest_asyncio.fixture
async def client(db: AsyncSession):
    async def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()


# --- Helpers ---

async def register(client: AsyncClient, email: str, password: str = "password123", name: str = "Test User") -> dict:
    resp = await client.post("/api/v1/auth/register", json={"name": name, "email": email, "password": password})
    assert resp.status_code == 201, resp.text
    return resp.json()["data"]


async def auth_headers(client: AsyncClient, email: str, password: str = "password123") -> dict:
    resp = await client.post("/api/v1/auth/login", json={"email": email, "password": password})
    assert resp.status_code == 200, resp.text
    token = resp.json()["data"]["tokens"]["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest_asyncio.fixture
async def user(client: AsyncClient) -> dict:
    """Registered user — returns login response data."""
    return await register(client, "user@test.com")


@pytest_asyncio.fixture
async def user_headers(client: AsyncClient, user: dict) -> dict:
    return {"Authorization": f"Bearer {user['tokens']['access_token']}"}


@pytest_asyncio.fixture
async def admin_user(client: AsyncClient, db: AsyncSession) -> dict:
    """Creates a user then promotes them to admin via DB."""
    data = await register(client, "admin@test.com", name="Admin User")
    result = await db.execute(
        __import__("sqlalchemy", fromlist=["select"]).select(User).where(User.email == "admin@test.com")
    )
    u = result.scalar_one()
    u.role = UserRole.admin
    await db.commit()
    return data


@pytest_asyncio.fixture
async def admin_headers(client: AsyncClient, admin_user: dict) -> dict:
    return await auth_headers(client, "admin@test.com")


SAMPLE_JOB_CONFIG = {
    "project": {
        "name": "Test Classifier",
        "domain_brief": "Customer support tickets for a fintech app.",
    },
    "dataset": {
        "brief": "Training data for a 2-class support classifier.",
        "target_count": 10,
        "require_balanced": True,
    },
    "schema": {
        "fields": [
            {"name": "text", "type": "string", "description": "The support message."},
            {
                "name": "label",
                "type": "enum",
                "description": "Category",
                "values": [
                    {"name": "billing", "description": "Billing questions"},
                    {"name": "security", "description": "Security issues"},
                ],
            },
        ]
    },
    "seeds": [{"text": "Why was I charged twice?", "label": "billing"}],
    "provider": {"type": "bedrock", "concurrency": 8},
    "judge": {"enabled": False},
    "logic_filter": {"enabled": False},
}

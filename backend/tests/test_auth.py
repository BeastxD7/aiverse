import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


async def test_register(client: AsyncClient):
    resp = await client.post("/api/v1/auth/register", json={
        "name": "Test User",
        "email": "test@example.com",
        "password": "password123",
    })
    assert resp.status_code == 201
    body = resp.json()
    assert body["success"] is True
    assert body["data"]["tokens"]["access_token"]
    assert body["data"]["credits"] == 100  # signup bonus


async def test_register_duplicate_email(client: AsyncClient):
    payload = {"name": "A", "email": "dup@example.com", "password": "password123"}
    await client.post("/api/v1/auth/register", json=payload)
    resp = await client.post("/api/v1/auth/register", json=payload)
    assert resp.status_code == 409
    assert resp.json()["success"] is False


async def test_login(client: AsyncClient):
    await client.post("/api/v1/auth/register", json={
        "name": "Login User",
        "email": "login@example.com",
        "password": "password123",
    })
    resp = await client.post("/api/v1/auth/login", json={
        "email": "login@example.com",
        "password": "password123",
    })
    assert resp.status_code == 200
    assert resp.json()["data"]["tokens"]["access_token"]


async def test_login_wrong_password(client: AsyncClient):
    resp = await client.post("/api/v1/auth/login", json={
        "email": "login@example.com",
        "password": "wrongpassword",
    })
    assert resp.status_code == 401
    assert resp.json()["success"] is False


async def test_get_me(client: AsyncClient):
    reg = await client.post("/api/v1/auth/register", json={
        "name": "Me User",
        "email": "me@example.com",
        "password": "password123",
    })
    token = reg.json()["data"]["tokens"]["access_token"]
    resp = await client.get("/api/v1/users/me", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    assert resp.json()["data"]["email"] == "me@example.com"

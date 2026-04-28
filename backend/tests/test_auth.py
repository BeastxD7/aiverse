"""Auth flow tests — register, login, refresh, logout, token guards."""

import pytest
from httpx import AsyncClient

from tests.conftest import auth_headers, register

pytestmark = pytest.mark.asyncio


# --- Register ---

async def test_register_success(client: AsyncClient):
    resp = await client.post("/api/v1/auth/register", json={
        "name": "Alice",
        "email": "alice@test.com",
        "password": "password123",
    })
    assert resp.status_code == 201
    body = resp.json()
    assert body["success"] is True
    assert body["data"]["email"] == "alice@test.com"
    assert body["data"]["role"] == "user"
    assert body["data"]["credits"] == 100          # signup bonus
    assert body["data"]["tokens"]["access_token"]
    assert body["data"]["tokens"]["refresh_token"]


async def test_register_duplicate_email(client: AsyncClient):
    payload = {"name": "Bob", "email": "bob@test.com", "password": "password123"}
    await client.post("/api/v1/auth/register", json=payload)
    resp = await client.post("/api/v1/auth/register", json=payload)
    assert resp.status_code == 409
    body = resp.json()
    assert body["success"] is False
    assert body["error"]["code"] == "CONFLICT"


async def test_register_short_password(client: AsyncClient):
    resp = await client.post("/api/v1/auth/register", json={
        "name": "Carol",
        "email": "carol@test.com",
        "password": "short",
    })
    assert resp.status_code == 422
    assert resp.json()["success"] is False


async def test_register_invalid_email(client: AsyncClient):
    resp = await client.post("/api/v1/auth/register", json={
        "name": "Dave",
        "email": "not-an-email",
        "password": "password123",
    })
    assert resp.status_code == 422


async def test_register_missing_fields(client: AsyncClient):
    resp = await client.post("/api/v1/auth/register", json={"email": "x@test.com"})
    assert resp.status_code == 422


# --- Login ---

async def test_login_success(client: AsyncClient):
    await register(client, "login_ok@test.com")
    resp = await client.post("/api/v1/auth/login", json={
        "email": "login_ok@test.com",
        "password": "password123",
    })
    assert resp.status_code == 200
    body = resp.json()
    assert body["success"] is True
    assert body["data"]["tokens"]["access_token"]
    assert body["data"]["credits"] == 100


async def test_login_wrong_password(client: AsyncClient):
    await register(client, "login_bad@test.com")
    resp = await client.post("/api/v1/auth/login", json={
        "email": "login_bad@test.com",
        "password": "wrongpassword",
    })
    assert resp.status_code == 401
    assert resp.json()["error"]["code"] == "UNAUTHORIZED"


async def test_login_nonexistent_email(client: AsyncClient):
    resp = await client.post("/api/v1/auth/login", json={
        "email": "nobody@test.com",
        "password": "password123",
    })
    assert resp.status_code == 401


# --- Token refresh ---

async def test_refresh_token(client: AsyncClient):
    data = await register(client, "refresh@test.com")
    refresh_token = data["tokens"]["refresh_token"]

    resp = await client.post("/api/v1/auth/refresh", json={"refresh_token": refresh_token})
    assert resp.status_code == 200
    body = resp.json()
    assert body["success"] is True
    assert body["data"]["access_token"]
    assert body["data"]["refresh_token"]
    # new refresh token must be different from old
    assert body["data"]["refresh_token"] != refresh_token


async def test_refresh_token_rotation(client: AsyncClient):
    """Using the old refresh token after rotation must fail."""
    data = await register(client, "rotation@test.com")
    old_refresh = data["tokens"]["refresh_token"]

    rotate_resp = await client.post("/api/v1/auth/refresh", json={"refresh_token": old_refresh})
    assert rotate_resp.status_code == 200

    # Old token is now revoked
    resp = await client.post("/api/v1/auth/refresh", json={"refresh_token": old_refresh})
    assert resp.status_code == 401


async def test_refresh_invalid_token(client: AsyncClient):
    resp = await client.post("/api/v1/auth/refresh", json={"refresh_token": "not-a-real-token"})
    assert resp.status_code == 401


# --- Logout ---

async def test_logout(client: AsyncClient):
    data = await register(client, "logout@test.com")
    refresh_token = data["tokens"]["refresh_token"]

    resp = await client.post("/api/v1/auth/logout", json={"refresh_token": refresh_token})
    assert resp.status_code == 200
    assert resp.json()["success"] is True

    # Refresh after logout must fail
    resp2 = await client.post("/api/v1/auth/refresh", json={"refresh_token": refresh_token})
    assert resp2.status_code == 401


# --- Auth guards ---

async def test_protected_route_no_token(client: AsyncClient):
    resp = await client.get("/api/v1/users/me")
    assert resp.status_code == 401


async def test_protected_route_bad_token(client: AsyncClient):
    resp = await client.get("/api/v1/users/me", headers={"Authorization": "Bearer bad.token.here"})
    assert resp.status_code == 401


async def test_protected_route_valid_token(client: AsyncClient):
    data = await register(client, "guard@test.com")
    token = data["tokens"]["access_token"]
    resp = await client.get("/api/v1/users/me", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200

"""Auth flow tests — register, login, refresh, logout, token guards."""

import pytest
from httpx import AsyncClient

from tests.conftest import auth_headers, register
from tests.helpers import (
    assert_auth_data,
    assert_envelope,
    assert_error,
    assert_success,
    assert_tokens,
)

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
    assert_success(body)
    assert_auth_data(body["data"])
    assert body["data"]["email"] == "alice@test.com"
    assert body["data"]["name"] == "Alice"
    assert body["data"]["role"] == "user"
    assert body["data"]["credits"] == 100


async def test_register_duplicate_email(client: AsyncClient):
    payload = {"name": "Bob", "email": "bob@test.com", "password": "password123"}
    await client.post("/api/v1/auth/register", json=payload)
    resp = await client.post("/api/v1/auth/register", json=payload)
    assert resp.status_code == 409
    assert_error(resp.json(), "CONFLICT")


async def test_register_short_password(client: AsyncClient):
    resp = await client.post("/api/v1/auth/register", json={
        "name": "Carol",
        "email": "carol@test.com",
        "password": "short",
    })
    assert resp.status_code == 422
    assert_error(resp.json(), "VALIDATION_ERROR")


async def test_register_invalid_email(client: AsyncClient):
    resp = await client.post("/api/v1/auth/register", json={
        "name": "Dave",
        "email": "not-an-email",
        "password": "password123",
    })
    assert resp.status_code == 422
    assert_error(resp.json(), "VALIDATION_ERROR")


async def test_register_missing_fields(client: AsyncClient):
    resp = await client.post("/api/v1/auth/register", json={"email": "x@test.com"})
    assert resp.status_code == 422
    assert_error(resp.json(), "VALIDATION_ERROR")


# --- Login ---

async def test_login_success(client: AsyncClient):
    await register(client, "login_ok@test.com")
    resp = await client.post("/api/v1/auth/login", json={
        "email": "login_ok@test.com",
        "password": "password123",
    })
    assert resp.status_code == 200
    body = resp.json()
    assert_success(body)
    assert_auth_data(body["data"])
    assert body["data"]["credits"] == 100


async def test_login_wrong_password(client: AsyncClient):
    await register(client, "login_bad@test.com")
    resp = await client.post("/api/v1/auth/login", json={
        "email": "login_bad@test.com",
        "password": "wrongpassword",
    })
    assert resp.status_code == 401
    assert_error(resp.json(), "UNAUTHORIZED")


async def test_login_nonexistent_email(client: AsyncClient):
    resp = await client.post("/api/v1/auth/login", json={
        "email": "nobody@test.com",
        "password": "password123",
    })
    assert resp.status_code == 401
    assert_error(resp.json(), "UNAUTHORIZED")


# --- Token refresh ---

async def test_refresh_token(client: AsyncClient):
    data = await register(client, "refresh@test.com")
    refresh_token = data["tokens"]["refresh_token"]

    resp = await client.post("/api/v1/auth/refresh", json={"refresh_token": refresh_token})
    assert resp.status_code == 200
    body = resp.json()
    assert_success(body)
    assert_tokens(body["data"])
    assert body["data"]["refresh_token"] != refresh_token


async def test_refresh_token_rotation(client: AsyncClient):
    """Using the old refresh token after rotation must fail."""
    data = await register(client, "rotation@test.com")
    old_refresh = data["tokens"]["refresh_token"]

    rotate_resp = await client.post("/api/v1/auth/refresh", json={"refresh_token": old_refresh})
    assert rotate_resp.status_code == 200

    resp = await client.post("/api/v1/auth/refresh", json={"refresh_token": old_refresh})
    assert resp.status_code == 401
    assert_error(resp.json(), "UNAUTHORIZED")


async def test_refresh_invalid_token(client: AsyncClient):
    resp = await client.post("/api/v1/auth/refresh", json={"refresh_token": "not-a-real-token"})
    assert resp.status_code == 401
    assert_error(resp.json(), "UNAUTHORIZED")


# --- Logout ---

async def test_logout(client: AsyncClient):
    data = await register(client, "logout@test.com")
    refresh_token = data["tokens"]["refresh_token"]

    resp = await client.post("/api/v1/auth/logout", json={"refresh_token": refresh_token})
    assert resp.status_code == 200
    body = resp.json()
    assert_success(body)

    resp2 = await client.post("/api/v1/auth/refresh", json={"refresh_token": refresh_token})
    assert resp2.status_code == 401


# --- Auth guards ---

async def test_protected_route_no_token(client: AsyncClient):
    resp = await client.get("/api/v1/users/me")
    assert resp.status_code == 401
    assert_envelope(resp.json())


async def test_protected_route_bad_token(client: AsyncClient):
    resp = await client.get("/api/v1/users/me", headers={"Authorization": "Bearer bad.token.here"})
    assert resp.status_code == 401
    assert_envelope(resp.json())


async def test_protected_route_valid_token(client: AsyncClient):
    data = await register(client, "guard@test.com")
    token = data["tokens"]["access_token"]
    resp = await client.get("/api/v1/users/me", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    assert_success(resp.json())


# --- HTTP error envelope ---

async def test_404_uses_standard_envelope(client: AsyncClient):
    """Non-existent routes must return the standard envelope, not FastAPI's default."""
    resp = await client.get("/api/v1/does-not-exist")
    assert resp.status_code == 404
    assert_envelope(resp.json())
    assert resp.json()["success"] is False


async def test_method_not_allowed_uses_standard_envelope(client: AsyncClient):
    """Wrong HTTP method must return the standard envelope, not {'detail': '...'}."""
    resp = await client.get("/api/v1/auth/register")  # GET on a POST-only route
    assert resp.status_code == 405
    body = resp.json()
    assert_envelope(body)
    assert body["success"] is False

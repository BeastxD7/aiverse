"""User profile tests — get_me, update, deactivate."""

import pytest
from httpx import AsyncClient

from tests.conftest import auth_headers, register

pytestmark = pytest.mark.asyncio


async def test_get_me(client: AsyncClient, user_headers: dict, user: dict):
    resp = await client.get("/api/v1/users/me", headers=user_headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["success"] is True
    assert body["data"]["email"] == user["email"]
    assert body["data"]["role"] == "user"
    assert body["data"]["credits"] == 100
    assert body["data"]["is_active"] is True
    assert "hashed_password" not in body["data"]


async def test_update_name(client: AsyncClient, user_headers: dict):
    resp = await client.patch("/api/v1/users/me", json={"name": "Updated Name"}, headers=user_headers)
    assert resp.status_code == 200
    assert resp.json()["data"]["name"] == "Updated Name"


async def test_update_password(client: AsyncClient):
    data = await register(client, "pwchange@test.com")
    headers = {"Authorization": f"Bearer {data['tokens']['access_token']}"}

    resp = await client.patch("/api/v1/users/me", json={"password": "newpassword456"}, headers=headers)
    assert resp.status_code == 200

    # Old password no longer works
    old_login = await client.post("/api/v1/auth/login", json={"email": "pwchange@test.com", "password": "password123"})
    assert old_login.status_code == 401

    # New password works
    new_login = await client.post("/api/v1/auth/login", json={"email": "pwchange@test.com", "password": "newpassword456"})
    assert new_login.status_code == 200


async def test_update_nothing(client: AsyncClient, user_headers: dict, user: dict):
    """PATCH with no fields is a no-op — returns current profile."""
    resp = await client.patch("/api/v1/users/me", json={}, headers=user_headers)
    assert resp.status_code == 200
    assert resp.json()["data"]["email"] == user["email"]


async def test_update_name_too_short(client: AsyncClient, user_headers: dict):
    resp = await client.patch("/api/v1/users/me", json={"name": "X"}, headers=user_headers)
    assert resp.status_code == 422


async def test_deactivate_account(client: AsyncClient):
    data = await register(client, "deactivate@test.com")
    headers = {"Authorization": f"Bearer {data['tokens']['access_token']}"}

    resp = await client.delete("/api/v1/users/me", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["success"] is True

    # Deactivated user cannot log in
    login = await client.post("/api/v1/auth/login", json={"email": "deactivate@test.com", "password": "password123"})
    assert login.status_code == 401


async def test_deactivated_token_rejected(client: AsyncClient):
    """Token issued before deactivation must be rejected on subsequent requests."""
    data = await register(client, "deact_token@test.com")
    headers = {"Authorization": f"Bearer {data['tokens']['access_token']}"}

    await client.delete("/api/v1/users/me", headers=headers)

    # Same token, now account is deactivated
    resp = await client.get("/api/v1/users/me", headers=headers)
    assert resp.status_code == 401

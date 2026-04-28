"""Admin route tests — credit settings CRUD and access control."""

import pytest
from httpx import AsyncClient

from tests.conftest import register

pytestmark = pytest.mark.asyncio


async def test_list_credit_settings_as_admin(client: AsyncClient, admin_headers: dict):
    resp = await client.get("/api/v1/admin/credit-settings", headers=admin_headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["success"] is True
    keys = [s["key"] for s in body["data"]]
    assert "credits_per_sample" in keys
    assert "free_credits_on_signup" in keys
    assert "min_credits_per_job" in keys


async def test_list_credit_settings_as_user_forbidden(client: AsyncClient, user_headers: dict):
    resp = await client.get("/api/v1/admin/credit-settings", headers=user_headers)
    assert resp.status_code == 403
    assert resp.json()["error"]["code"] == "FORBIDDEN"


async def test_list_credit_settings_unauthenticated(client: AsyncClient):
    resp = await client.get("/api/v1/admin/credit-settings")
    assert resp.status_code == 401


async def test_update_credit_setting(client: AsyncClient, admin_headers: dict):
    resp = await client.patch(
        "/api/v1/admin/credit-settings/credits_per_sample",
        json={"value": "2"},
        headers=admin_headers,
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["success"] is True
    assert body["data"]["key"] == "credits_per_sample"
    assert body["data"]["value"] == "2"

    # Reset back to 1 so other tests are unaffected
    await client.patch(
        "/api/v1/admin/credit-settings/credits_per_sample",
        json={"value": "1"},
        headers=admin_headers,
    )


async def test_update_signup_bonus(client: AsyncClient, admin_headers: dict):
    """Changing signup bonus takes effect for new registrations."""
    await client.patch(
        "/api/v1/admin/credit-settings/free_credits_on_signup",
        json={"value": "50"},
        headers=admin_headers,
    )

    data = await register(client, "newbonus@test.com")
    assert data["credits"] == 50

    # Reset
    await client.patch(
        "/api/v1/admin/credit-settings/free_credits_on_signup",
        json={"value": "100"},
        headers=admin_headers,
    )


async def test_update_nonexistent_setting(client: AsyncClient, admin_headers: dict):
    resp = await client.patch(
        "/api/v1/admin/credit-settings/does_not_exist",
        json={"value": "99"},
        headers=admin_headers,
    )
    assert resp.status_code == 404


async def test_update_setting_as_user_forbidden(client: AsyncClient, user_headers: dict):
    resp = await client.patch(
        "/api/v1/admin/credit-settings/credits_per_sample",
        json={"value": "99"},
        headers=user_headers,
    )
    assert resp.status_code == 403


async def test_update_setting_empty_value(client: AsyncClient, admin_headers: dict):
    resp = await client.patch(
        "/api/v1/admin/credit-settings/credits_per_sample",
        json={"value": ""},
        headers=admin_headers,
    )
    assert resp.status_code == 422

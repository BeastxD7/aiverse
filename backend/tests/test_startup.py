"""Startup and environment tests — verify app loads correctly."""

import os

import pytest
from httpx import AsyncClient

from tests.helpers import assert_envelope, assert_success

pytestmark = pytest.mark.asyncio


async def test_health_response_shape(client: AsyncClient):
    resp = await client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert "status" in body
    assert body["status"] == "ok"
    assert "version" in body


async def test_dotenv_loaded_into_os_environ():
    """DATABASE_URL from .env must be in os.environ so background tasks can read it.

    This catches the class of bug where the app starts fine (pydantic-settings
    loads .env into Settings) but background tasks that call os.environ.get()
    directly (like the engine's BedrockCredentials.from_env) see empty values.
    """
    assert os.environ.get("DATABASE_URL"), (
        "DATABASE_URL missing from os.environ — load_dotenv() not called at startup. "
        "Background engine tasks will fail with missing env var errors."
    )


async def test_secret_key_loaded():
    assert os.environ.get("SECRET_KEY"), "SECRET_KEY missing from os.environ"


async def test_404_returns_standard_envelope(client: AsyncClient):
    resp = await client.get("/api/v1/this-does-not-exist")
    assert resp.status_code == 404
    body = resp.json()
    assert_envelope(body)
    assert body["success"] is False
    assert body["data"] is None
    assert body["error"] is not None


async def test_405_returns_standard_envelope(client: AsyncClient):
    """Wrong HTTP method must return our envelope, not FastAPI's raw {'detail': '...'}."""
    resp = await client.get("/api/v1/auth/register")  # GET on POST-only route
    assert resp.status_code == 405
    body = resp.json()
    assert_envelope(body)
    assert body["success"] is False


async def test_unprotected_routes_accessible(client: AsyncClient):
    """Public routes must work without a token."""
    resp = await client.get("/health")
    assert resp.status_code == 200

    resp = await client.post("/api/v1/auth/login", json={"email": "x@x.com", "password": "wrong"})
    assert resp.status_code in (401, 422)  # wrong creds or validation — not 500

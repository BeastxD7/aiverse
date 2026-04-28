"""Job lifecycle tests — create, list, get, cancel, access control, credit checks."""

import uuid

import pytest
from httpx import AsyncClient

from tests.conftest import SAMPLE_JOB_CONFIG, register

pytestmark = pytest.mark.asyncio


async def _create_job(client: AsyncClient, headers: dict, name: str = "Test Job", config: dict | None = None) -> dict:
    resp = await client.post(
        "/api/v1/jobs/",
        json={"name": name, "config": config or SAMPLE_JOB_CONFIG},
        headers=headers,
    )
    assert resp.status_code == 201, resp.text
    return resp.json()["data"]


# --- Create ---

async def test_create_job_success(client: AsyncClient, user_headers: dict):
    resp = await client.post(
        "/api/v1/jobs/",
        json={"name": "My first job", "config": SAMPLE_JOB_CONFIG},
        headers=user_headers,
    )
    assert resp.status_code == 201
    body = resp.json()
    assert body["success"] is True
    job = body["data"]
    assert job["name"] == "My first job"
    assert job["status"] in ("created", "queued", "running", "failed")
    assert job["credits_reserved"] > 0
    assert job["output_format"] == "jsonl"


async def test_create_job_csv_format(client: AsyncClient, user_headers: dict):
    resp = await client.post(
        "/api/v1/jobs/",
        json={"name": "CSV job", "config": SAMPLE_JOB_CONFIG, "output_format": "csv"},
        headers=user_headers,
    )
    assert resp.status_code == 201
    assert resp.json()["data"]["output_format"] == "csv"


async def test_create_job_invalid_format(client: AsyncClient, user_headers: dict):
    resp = await client.post(
        "/api/v1/jobs/",
        json={"name": "Bad format", "config": SAMPLE_JOB_CONFIG, "output_format": "xml"},
        headers=user_headers,
    )
    assert resp.status_code == 422


async def test_create_job_missing_target_count(client: AsyncClient, user_headers: dict):
    bad_config = {**SAMPLE_JOB_CONFIG, "dataset": {"brief": "test"}}
    resp = await client.post(
        "/api/v1/jobs/",
        json={"name": "No target", "config": bad_config},
        headers=user_headers,
    )
    assert resp.status_code == 400
    assert resp.json()["error"]["code"] == "BAD_REQUEST"


async def test_create_job_unauthenticated(client: AsyncClient):
    resp = await client.post("/api/v1/jobs/", json={"name": "No auth", "config": SAMPLE_JOB_CONFIG})
    assert resp.status_code == 401


async def test_create_job_reserves_credits(client: AsyncClient, user_headers: dict):
    balance_before = (await client.get("/api/v1/credits/balance", headers=user_headers)).json()["data"]["credits"]

    await _create_job(client, user_headers)

    balance_after = (await client.get("/api/v1/credits/balance", headers=user_headers)).json()["data"]["credits"]
    assert balance_after < balance_before


# --- List ---

async def test_list_jobs_empty(client: AsyncClient):
    data = await register(client, "listjobs@test.com")
    headers = {"Authorization": f"Bearer {data['tokens']['access_token']}"}

    resp = await client.get("/api/v1/jobs/", headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["data"]["total"] == 0
    assert body["data"]["items"] == []


async def test_list_jobs_pagination(client: AsyncClient, user_headers: dict):
    await _create_job(client, user_headers, "Job A")
    await _create_job(client, user_headers, "Job B")

    resp = await client.get("/api/v1/jobs/?page=1&limit=1", headers=user_headers)
    assert resp.status_code == 200
    body = resp.json()["data"]
    assert len(body["items"]) == 1
    assert body["total"] >= 2
    assert body["pages"] >= 2


async def test_list_jobs_only_own(client: AsyncClient, user_headers: dict):
    """User A's jobs must not appear in User B's list."""
    data_b = await register(client, "other_list@test.com")
    headers_b = {"Authorization": f"Bearer {data_b['tokens']['access_token']}"}

    await _create_job(client, user_headers, "User A's job")

    resp = await client.get("/api/v1/jobs/", headers=headers_b)
    assert resp.json()["data"]["total"] == 0


# --- Get ---

async def test_get_job(client: AsyncClient, user_headers: dict):
    job = await _create_job(client, user_headers)
    resp = await client.get(f"/api/v1/jobs/{job['id']}", headers=user_headers)
    assert resp.status_code == 200
    assert resp.json()["data"]["id"] == job["id"]


async def test_get_job_not_found(client: AsyncClient, user_headers: dict):
    fake_id = str(uuid.uuid4())
    resp = await client.get(f"/api/v1/jobs/{fake_id}", headers=user_headers)
    assert resp.status_code == 404


async def test_get_other_users_job(client: AsyncClient, user_headers: dict):
    """Getting another user's job must return 404, not 403 (don't leak existence)."""
    job = await _create_job(client, user_headers)

    data_b = await register(client, "other_get@test.com")
    headers_b = {"Authorization": f"Bearer {data_b['tokens']['access_token']}"}

    resp = await client.get(f"/api/v1/jobs/{job['id']}", headers=headers_b)
    assert resp.status_code == 404


# --- Cancel ---

async def test_cancel_job(client: AsyncClient, user_headers: dict):
    job = await _create_job(client, user_headers)
    resp = await client.delete(f"/api/v1/jobs/{job['id']}", headers=user_headers)
    assert resp.status_code == 200
    assert resp.json()["data"]["status"] == "cancelled"


async def test_cancel_already_failed_job(client: AsyncClient, user_headers: dict):
    """Cannot cancel a job that already reached a terminal state."""
    job = await _create_job(client, user_headers)

    # Wait briefly for the background task to fail (engine not wired → NotImplementedError)
    import asyncio
    await asyncio.sleep(0.3)

    job_resp = await client.get(f"/api/v1/jobs/{job['id']}", headers=user_headers)
    status = job_resp.json()["data"]["status"]

    if status == "failed":
        resp = await client.delete(f"/api/v1/jobs/{job['id']}", headers=user_headers)
        assert resp.status_code == 400


async def test_cancel_other_users_job(client: AsyncClient, user_headers: dict):
    job = await _create_job(client, user_headers)

    data_b = await register(client, "other_cancel@test.com")
    headers_b = {"Authorization": f"Bearer {data_b['tokens']['access_token']}"}

    resp = await client.delete(f"/api/v1/jobs/{job['id']}", headers=headers_b)
    assert resp.status_code == 404


# --- Events ---

async def test_get_events_empty_initially(client: AsyncClient, user_headers: dict):
    job = await _create_job(client, user_headers)
    resp = await client.get(f"/api/v1/jobs/{job['id']}/events", headers=user_headers)
    assert resp.status_code == 200
    assert isinstance(resp.json()["data"], list)


async def test_get_events_other_user(client: AsyncClient, user_headers: dict):
    job = await _create_job(client, user_headers)

    data_b = await register(client, "other_events@test.com")
    headers_b = {"Authorization": f"Bearer {data_b['tokens']['access_token']}"}

    resp = await client.get(f"/api/v1/jobs/{job['id']}/events", headers=headers_b)
    assert resp.status_code == 404


# --- Output ---

async def test_download_output_not_ready(client: AsyncClient, user_headers: dict):
    """Job has no output yet — should return 404."""
    job = await _create_job(client, user_headers)
    resp = await client.get(f"/api/v1/jobs/{job['id']}/output", headers=user_headers)
    assert resp.status_code == 404


async def test_download_output_other_user(client: AsyncClient, user_headers: dict):
    job = await _create_job(client, user_headers)

    data_b = await register(client, "other_output@test.com")
    headers_b = {"Authorization": f"Bearer {data_b['tokens']['access_token']}"}

    resp = await client.get(f"/api/v1/jobs/{job['id']}/output", headers=headers_b)
    assert resp.status_code == 404


# --- Health ---

async def test_health(client: AsyncClient):
    resp = await client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"

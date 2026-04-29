"""End-to-end tests — hit the real running server and real LLM provider.

These tests are skipped by default. To run them:

    RUN_E2E_TESTS=1 uv run pytest tests/test_e2e.py -v -s

Requirements:
  - Server running:  uv run uvicorn app.main:app --reload
  - Bedrock creds:   AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION set
  - The tests register a fresh user each run, so no fixture state needed.
"""

import asyncio
import os
import time

import pytest
import httpx

E2E_BASE = os.getenv("E2E_BASE_URL", "http://localhost:8000")
SKIP = not os.getenv("RUN_E2E_TESTS")
SKIP_REASON = "Set RUN_E2E_TESTS=1 to run e2e tests (requires live server + Bedrock creds)"

SMALL_JOB_CONFIG = {
    "project": {
        "name": "E2E Smoke Test",
        "domain_brief": "Customer support tickets for a fintech app.",
    },
    "dataset": {
        "brief": "Binary classifier training data.",
        "target_count": 3,
        "require_balanced": False,
    },
    "schema": {
        "fields": [
            {"name": "text", "type": "string", "description": "Support message text."},
            {
                "name": "label",
                "type": "enum",
                "description": "Issue category.",
                "values": [
                    {"name": "billing", "description": "Billing questions"},
                    {"name": "security", "description": "Security issues"},
                ],
            },
        ]
    },
    "seeds": [{"text": "Why was I charged twice?", "label": "billing"}],
    "provider": {"type": "bedrock", "concurrency": 3},
    "judge": {"enabled": False},
    "logic_filter": {"enabled": False},
}


@pytest.fixture(scope="module")
def http():
    with httpx.Client(base_url=E2E_BASE, timeout=30) as client:
        yield client


@pytest.fixture(scope="module")
def auth_token(http):
    """Register a fresh user and return the access token."""
    ts = int(time.time())
    resp = http.post("/api/v1/auth/register", json={
        "name": "E2E User",
        "email": f"e2e_{ts}@test.com",
        "password": "e2epassword123",
    })
    assert resp.status_code == 201, resp.text
    return resp.json()["data"]["tokens"]["access_token"]


@pytest.fixture(scope="module")
def headers(auth_token):
    return {"Authorization": f"Bearer {auth_token}"}


def wait_for_job(http, headers, job_id, timeout=120):
    """Poll GET /jobs/:id until terminal status or timeout."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        resp = http.get(f"/api/v1/jobs/{job_id}", headers=headers)
        assert resp.status_code == 200, resp.text
        status = resp.json()["data"]["status"]
        if status in ("completed", "failed", "cancelled"):
            return resp.json()["data"]
        time.sleep(3)
    raise TimeoutError(f"Job {job_id} did not finish within {timeout}s")


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

@pytest.mark.skipif(SKIP, reason=SKIP_REASON)
def test_health(http):
    resp = http.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


@pytest.mark.skipif(SKIP, reason=SKIP_REASON)
def test_register_and_login(http):
    ts = int(time.time())
    email = f"e2e_login_{ts}@test.com"

    reg = http.post("/api/v1/auth/register", json={
        "name": "Login Test",
        "email": email,
        "password": "logintest123",
    })
    assert reg.status_code == 201
    assert reg.json()["data"]["credits"] == 100

    login = http.post("/api/v1/auth/login", json={"email": email, "password": "logintest123"})
    assert login.status_code == 200
    assert "access_token" in login.json()["data"]["tokens"]


@pytest.mark.skipif(SKIP, reason=SKIP_REASON)
def test_credit_balance(http, headers):
    resp = http.get("/api/v1/credits/balance", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["data"]["credits"] == 100


@pytest.mark.skipif(SKIP, reason=SKIP_REASON)
def test_create_job_and_complete(http, headers):
    """Full pipeline: create → wait for completion → download output."""
    resp = http.post("/api/v1/jobs/", headers=headers, json={
        "name": "E2E Smoke Job",
        "output_format": "jsonl",
        "config": SMALL_JOB_CONFIG,
    })
    assert resp.status_code == 201, resp.text
    job = resp.json()["data"]
    job_id = job["id"]

    assert job["status"] in ("queued", "running", "created")
    assert job["credits_reserved"] >= 3

    final = wait_for_job(http, headers, job_id, timeout=180)
    assert final["status"] == "completed", f"Job failed: {final.get('error_message')}"
    assert final["output_row_count"] >= 1

    # Download the output
    dl = http.get(f"/api/v1/jobs/{job_id}/output", headers=headers)
    assert dl.status_code == 200
    lines = [l for l in dl.text.strip().splitlines() if l]
    assert len(lines) == final["output_row_count"]

    import json as _json
    for line in lines:
        row = _json.loads(line)
        assert "text" in row
        assert "label" in row
        assert row["label"] in ("billing", "security")


@pytest.mark.skipif(SKIP, reason=SKIP_REASON)
def test_credits_reduced_after_job(http, headers):
    """Balance after job should be less than 100."""
    resp = http.get("/api/v1/credits/balance", headers=headers)
    assert resp.status_code == 200
    balance = resp.json()["data"]["credits"]
    assert balance < 100


@pytest.mark.skipif(SKIP, reason=SKIP_REASON)
def test_credit_transactions_recorded(http, headers):
    """Should see grant + reserve + debit + refund transactions."""
    resp = http.get("/api/v1/credits/transactions", headers=headers)
    assert resp.status_code == 200
    types = {t["type"] for t in resp.json()["data"]["items"]}
    assert "grant" in types
    assert "reserve" in types
    assert "debit" in types


@pytest.mark.skipif(SKIP, reason=SKIP_REASON)
def test_job_events_recorded(http, headers):
    """Event replay log should have at least start and done entries."""
    jobs = http.get("/api/v1/jobs/", headers=headers)
    assert jobs.status_code == 200
    completed = [j for j in jobs.json()["data"]["items"] if j["status"] == "completed"]
    assert completed, "No completed jobs found — run test_create_job_and_complete first"

    job_id = completed[0]["id"]
    resp = http.get(f"/api/v1/jobs/{job_id}/events", headers=headers)
    assert resp.status_code == 200
    events = resp.json()["data"]
    assert len(events) > 0
    stage_names = [e["stage"] for e in events]
    assert "start" in stage_names
    assert "done" in stage_names


@pytest.mark.skipif(SKIP, reason=SKIP_REASON)
def test_cancel_queued_job(http, headers):
    """Create a job and immediately cancel it before it finishes."""
    resp = http.post("/api/v1/jobs/", headers=headers, json={
        "name": "E2E Cancel Test",
        "output_format": "jsonl",
        "config": SMALL_JOB_CONFIG,
    })
    assert resp.status_code == 201
    job_id = resp.json()["data"]["id"]

    cancel = http.delete(f"/api/v1/jobs/{job_id}", headers=headers)
    assert cancel.status_code == 200
    assert cancel.json()["data"]["status"] in ("cancelled", "completed")


@pytest.mark.skipif(SKIP, reason=SKIP_REASON)
def test_csv_output_format(http, headers):
    """Job with CSV format produces valid CSV output."""
    resp = http.post("/api/v1/jobs/", headers=headers, json={
        "name": "E2E CSV Job",
        "output_format": "csv",
        "config": SMALL_JOB_CONFIG,
    })
    assert resp.status_code == 201
    job_id = resp.json()["data"]["id"]

    final = wait_for_job(http, headers, job_id, timeout=180)
    assert final["status"] == "completed"

    dl = http.get(f"/api/v1/jobs/{job_id}/output", headers=headers)
    assert dl.status_code == 200
    lines = dl.text.strip().splitlines()
    assert lines[0] == "text,label"  # CSV header
    assert len(lines) > 1

"""Credit system tests — balance, transactions, signup bonus, reservation."""

import pytest
from httpx import AsyncClient

from tests.conftest import SAMPLE_JOB_CONFIG, register

pytestmark = pytest.mark.asyncio


async def test_signup_bonus(client: AsyncClient):
    data = await register(client, "bonus@test.com")
    headers = {"Authorization": f"Bearer {data['tokens']['access_token']}"}

    resp = await client.get("/api/v1/credits/balance", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["data"]["credits"] == 100


async def test_balance_unauthenticated(client: AsyncClient):
    resp = await client.get("/api/v1/credits/balance")
    assert resp.status_code == 401


async def test_transactions_empty_on_signup(client: AsyncClient):
    data = await register(client, "txn_empty@test.com")
    headers = {"Authorization": f"Bearer {data['tokens']['access_token']}"}

    resp = await client.get("/api/v1/credits/transactions", headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["success"] is True
    # Should have exactly 1 transaction: the signup grant
    txns = body["data"]
    assert len(txns) == 1
    assert txns[0]["type"] == "grant"
    assert txns[0]["amount"] == 100
    assert txns[0]["balance_after"] == 100


async def test_balance_reduced_after_job_reservation(client: AsyncClient, user_headers: dict):
    """Creating a job reserves credits and reduces balance immediately."""
    balance_before = (await client.get("/api/v1/credits/balance", headers=user_headers)).json()["data"]["credits"]

    config = {**SAMPLE_JOB_CONFIG, "dataset": {**SAMPLE_JOB_CONFIG["dataset"], "target_count": 20}}
    await client.post("/api/v1/jobs/", json={"name": "Reserve test", "config": config}, headers=user_headers)

    balance_after = (await client.get("/api/v1/credits/balance", headers=user_headers)).json()["data"]["credits"]
    assert balance_after < balance_before


async def test_reserve_transaction_recorded(client: AsyncClient, user_headers: dict):
    config = {**SAMPLE_JOB_CONFIG, "dataset": {**SAMPLE_JOB_CONFIG["dataset"], "target_count": 10}}
    await client.post("/api/v1/jobs/", json={"name": "Txn test", "config": config}, headers=user_headers)

    resp = await client.get("/api/v1/credits/transactions", headers=user_headers)
    txns = resp.json()["data"]
    types = [t["type"] for t in txns]
    assert "reserve" in types


async def test_insufficient_credits(client: AsyncClient):
    """User with only signup credits cannot book a job that costs more."""
    data = await register(client, "broke@test.com")
    headers = {"Authorization": f"Bearer {data['tokens']['access_token']}"}

    # target_count=200 at 1 credit/sample = 200 credits needed; user only has 100
    config = {**SAMPLE_JOB_CONFIG, "dataset": {**SAMPLE_JOB_CONFIG["dataset"], "target_count": 200}}
    resp = await client.post("/api/v1/jobs/", json={"name": "Too big", "config": config}, headers=headers)
    assert resp.status_code == 402
    assert resp.json()["error"]["code"] == "INSUFFICIENT_CREDITS"


async def test_transactions_pagination(client: AsyncClient):
    data = await register(client, "txn_page@test.com")
    headers = {"Authorization": f"Bearer {data['tokens']['access_token']}"}

    resp = await client.get("/api/v1/credits/transactions?page=1&limit=5", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["success"] is True


async def test_transactions_unauthenticated(client: AsyncClient):
    resp = await client.get("/api/v1/credits/transactions")
    assert resp.status_code == 401

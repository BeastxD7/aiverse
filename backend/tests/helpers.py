"""Shared assertion helpers for response structure validation."""


def assert_envelope(body: dict) -> None:
    """Every response must have the standard 4-key envelope."""
    assert "success" in body, "missing 'success'"
    assert "message" in body, "missing 'message'"
    assert "data" in body, "missing 'data'"
    assert "error" in body, "missing 'error'"
    assert isinstance(body["success"], bool)
    assert isinstance(body["message"], str)


def assert_success(body: dict) -> None:
    assert_envelope(body)
    assert body["success"] is True
    assert body["error"] is None


def assert_error(body: dict, code: str) -> None:
    assert_envelope(body)
    assert body["success"] is False
    assert body["data"] is None
    assert body["error"] is not None
    assert "code" in body["error"], f"error missing 'code', got: {body['error']}"
    assert body["error"]["code"] == code, f"expected code={code}, got {body['error']['code']}"


def assert_auth_data(data: dict) -> None:
    for field in ("user_id", "name", "email", "role", "credits", "tokens"):
        assert field in data, f"auth data missing '{field}'"
    assert data["role"] in ("user", "admin")
    assert isinstance(data["credits"], int)
    assert_tokens(data["tokens"])


def assert_tokens(tokens: dict) -> None:
    for field in ("access_token", "refresh_token", "token_type"):
        assert field in tokens, f"tokens missing '{field}'"
    assert tokens["token_type"] == "bearer"
    assert len(tokens["access_token"]) > 20
    assert len(tokens["refresh_token"]) > 20


def assert_user_data(data: dict) -> None:
    for field in ("id", "name", "email", "role", "credits", "is_active", "created_at"):
        assert field in data, f"user data missing '{field}'"
    assert "hashed_password" not in data, "hashed_password must never be exposed"
    assert data["role"] in ("user", "admin")
    assert isinstance(data["credits"], int)
    assert isinstance(data["is_active"], bool)


def assert_job_data(data: dict) -> None:
    for field in ("id", "name", "status", "output_format", "credits_reserved",
                  "credits_used", "created_at"):
        assert field in data, f"job data missing '{field}'"
    assert data["status"] in ("created", "queued", "running", "completed", "failed", "cancelled")
    assert data["output_format"] in ("jsonl", "json", "csv")
    assert isinstance(data["credits_reserved"], int)
    assert isinstance(data["credits_used"], int)


def assert_job_list_data(data: dict) -> None:
    assert_paginated(data)
    for item in data["items"]:
        for field in ("id", "name", "status", "credits_used", "created_at"):
            assert field in item, f"job list item missing '{field}'"


def assert_transaction_data(txn: dict) -> None:
    for field in ("id", "type", "amount", "balance_after", "description", "created_at"):
        assert field in txn, f"transaction missing '{field}'"
    assert txn["type"] in ("grant", "reserve", "debit", "refund")
    assert isinstance(txn["amount"], int)
    assert isinstance(txn["balance_after"], int)


def assert_paginated(data: dict) -> None:
    for field in ("items", "total", "page", "limit", "pages"):
        assert field in data, f"paginated response missing '{field}'"
    assert isinstance(data["items"], list)
    assert isinstance(data["total"], int)
    assert isinstance(data["pages"], int)


def assert_credit_setting(setting: dict) -> None:
    for field in ("key", "value", "description"):
        assert field in setting, f"credit setting missing '{field}'"

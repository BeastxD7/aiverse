"""AWS Bedrock provider via the Converse API.

Uses `bedrock-runtime.converse` for cross-model compatibility (Claude, Llama,
Nova, Titan). Credentials and model ID are read from environment variables —
never from the YAML config — so secrets stay out of repos.

Required env vars:
    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    AWS_REGION
    AWS_MODEL_ID
"""

from __future__ import annotations

import asyncio
import os
from dataclasses import dataclass

from .base import LLMResponse
from .ollama import _looks_like_refusal, _repair_json  # reuse JSON + refusal logic


@dataclass
class BedrockCredentials:
    access_key_id: str
    secret_access_key: str
    region: str
    model_id: str

    @classmethod
    def from_env(cls) -> "BedrockCredentials":
        missing = [
            k
            for k in ("AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_REGION", "AWS_MODEL_ID")
            if not os.environ.get(k)
        ]
        if missing:
            raise RuntimeError(
                f"Bedrock provider missing env vars: {', '.join(missing)}. "
                "Set them in .env or export them in your shell."
            )
        return cls(
            access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
            secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
            region=os.environ["AWS_REGION"],
            model_id=os.environ["AWS_MODEL_ID"],
        )


class BedrockProvider:
    """Async wrapper around bedrock-runtime.converse with JSON repair + retries."""

    def __init__(
        self,
        *,
        creds: BedrockCredentials | None = None,
        timeout_seconds: int = 120,
        max_output_tokens: int = 2048,
    ) -> None:
        # Lazy boto3 import — keeps cold start fast when Bedrock isn't used.
        import boto3
        from botocore.config import Config

        self.creds = creds or BedrockCredentials.from_env()
        self.model = self.creds.model_id
        self.timeout = timeout_seconds
        self.max_output_tokens = max_output_tokens

        self._client = boto3.client(
            "bedrock-runtime",
            region_name=self.creds.region,
            aws_access_key_id=self.creds.access_key_id,
            aws_secret_access_key=self.creds.secret_access_key,
            config=Config(
                read_timeout=timeout_seconds,
                connect_timeout=10,
                retries={"max_attempts": 1},  # we handle retries ourselves
            ),
        )

    async def warmup(self) -> None:
        """Cheap round-trip so the first real call isn't an SDK-init cold start."""
        try:
            await self._converse(
                system="You reply with JSON only.",
                user="Return: {\"ok\": true}",
                format_json=True,
                max_tokens=32,
            )
        except Exception:  # noqa: BLE001
            pass

    async def generate_json(
        self,
        system: str,
        user: str,
        *,
        max_retries: int = 3,
    ) -> LLMResponse:
        last_err: str | None = None
        raw = ""
        for attempt in range(1, max_retries + 1):
            try:
                raw = await self._converse(system=system, user=user, format_json=True)
            except asyncio.TimeoutError as e:
                last_err = f"timeout after {self.timeout}s ({type(e).__name__})"
                await _backoff(attempt)
                continue
            except Exception as e:  # noqa: BLE001
                last_err = f"{type(e).__name__}: {e}"
                await _backoff(attempt)
                continue

            if _looks_like_refusal(raw):
                return LLMResponse(
                    outcome="refusal",
                    raw_text=raw,
                    parsed=None,
                    error="model refused",
                    attempts=attempt,
                )

            parsed = _repair_json(raw)
            if parsed is not None:
                return LLMResponse(
                    outcome="success",
                    raw_text=raw,
                    parsed=parsed,
                    attempts=attempt,
                )
            last_err = "unparseable JSON"
            await _backoff(attempt)

        if last_err and "timeout" in last_err:
            outcome = "timeout"
        elif last_err == "unparseable JSON":
            outcome = "invalid_json"
        else:
            outcome = "error"
        return LLMResponse(
            outcome=outcome,
            raw_text=raw,
            parsed=None,
            error=last_err,
            attempts=max_retries,
        )

    async def generate_text(
        self,
        system: str,
        user: str,
        *,
        max_retries: int = 3,
    ) -> LLMResponse:
        last_err: str | None = None
        raw = ""
        for attempt in range(1, max_retries + 1):
            try:
                raw = await self._converse(system=system, user=user, format_json=False)
                return LLMResponse(outcome="success", raw_text=raw, parsed=None, attempts=attempt)
            except asyncio.TimeoutError as e:
                last_err = f"timeout after {self.timeout}s ({type(e).__name__})"
                await _backoff(attempt)
            except Exception as e:  # noqa: BLE001
                last_err = f"{type(e).__name__}: {e}"
                await _backoff(attempt)

        outcome = "timeout" if last_err and "timeout" in last_err else "error"
        return LLMResponse(
            outcome=outcome,
            raw_text=raw,
            parsed=None,
            error=last_err,
            attempts=max_retries,
        )

    # ------------------------------------------------------------------ internals

    async def _converse(
        self,
        *,
        system: str,
        user: str,
        format_json: bool,
        max_tokens: int | None = None,
    ) -> str:
        """Run a single converse call in a thread (boto3 is sync)."""
        max_tok = max_tokens or self.max_output_tokens
        user_content = user
        if format_json:
            # Bedrock's converse has no cross-model JSON mode. Reinforce it.
            user_content = user + "\n\nReturn ONLY valid JSON. No prose, no markdown fences."

        def _call() -> str:
            resp = self._client.converse(
                modelId=self.model,
                system=[{"text": system}],
                messages=[{"role": "user", "content": [{"text": user_content}]}],
                inferenceConfig={
                    "maxTokens": max_tok,
                    "temperature": 0.8,
                },
            )
            blocks = resp.get("output", {}).get("message", {}).get("content", [])
            text_parts = [b.get("text", "") for b in blocks if isinstance(b, dict) and "text" in b]
            return "".join(text_parts).strip()

        return await asyncio.wait_for(asyncio.to_thread(_call), timeout=self.timeout)


async def _backoff(attempt: int) -> None:
    await asyncio.sleep(min(2 ** (attempt - 1), 8))

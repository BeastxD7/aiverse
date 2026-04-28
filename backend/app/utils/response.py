from typing import Any

from pydantic import BaseModel


class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Any | None = None
    error: Any | None = None


def api_success(data: Any = None, message: str = "Success") -> ApiResponse:
    return ApiResponse(success=True, message=message, data=data)


def api_error(message: str = "Something went wrong", error: Any = None) -> ApiResponse:
    return ApiResponse(success=False, message=message, error=error)

from fastapi import HTTPException


class AppError(HTTPException):
    def __init__(self, status_code: int, message: str, code: str):
        super().__init__(status_code=status_code, detail={"message": message, "code": code})
        self.message = message
        self.code = code


class NotFoundError(AppError):
    def __init__(self, resource: str = "Resource"):
        super().__init__(404, f"{resource} not found", "NOT_FOUND")


class UnauthorizedError(AppError):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(401, message, "UNAUTHORIZED")


class ForbiddenError(AppError):
    def __init__(self, message: str = "You do not have permission to perform this action"):
        super().__init__(403, message, "FORBIDDEN")


class ConflictError(AppError):
    def __init__(self, message: str):
        super().__init__(409, message, "CONFLICT")


class BadRequestError(AppError):
    def __init__(self, message: str):
        super().__init__(400, message, "BAD_REQUEST")


class InsufficientCreditsError(AppError):
    def __init__(self, required: int, available: int):
        super().__init__(
            402,
            f"Insufficient credits: need {required}, have {available}",
            "INSUFFICIENT_CREDITS",
        )

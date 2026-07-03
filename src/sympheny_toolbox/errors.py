"""Exception hierarchy for the Sympheny API client."""

from __future__ import annotations


class SymphenyError(Exception):
    """Base class for all errors raised by sympheny-toolbox."""


class APIError(SymphenyError):
    """The API returned an unsuccessful HTTP status code."""

    def __init__(self, message: str, *, status_code: int, body: str | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.body = body


class AuthenticationError(APIError):
    """Authentication failed (invalid credentials or expired/rejected token)."""


class NotFoundError(APIError):
    """The requested resource does not exist (HTTP 404)."""


class UnexpectedResponseError(SymphenyError):
    """The API response did not contain the expected payload."""

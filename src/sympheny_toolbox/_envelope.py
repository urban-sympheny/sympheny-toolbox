"""Helpers for unwrapping the ``ResponseDto*`` envelopes used by the Sympheny platform API."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

from sympheny_toolbox.errors import UnexpectedResponseError


if TYPE_CHECKING:
    from pydantic import BaseModel

T = TypeVar("T")


def unwrap(data: T | None) -> T:
    """Return the ``data`` payload of a response envelope, raising if it is missing."""
    if data is None:
        raise UnexpectedResponseError("API response did not contain the expected 'data' payload")
    return data


def dump(model: BaseModel) -> Any:
    """Serialize a request model to JSON-compatible data using the API's camelCase aliases."""
    return model.model_dump(mode="json", by_alias=True, exclude_none=True)

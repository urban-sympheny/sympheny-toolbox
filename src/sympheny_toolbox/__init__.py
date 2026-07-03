"""sympheny-toolbox — Python client for the Sympheny API.

Provides a synchronous client (:class:`Sympheny`) and its asynchronous twin
(:class:`AsyncSympheny`), typed request/response models (:mod:`sympheny_toolbox.models`),
and high-level automation helpers (:mod:`sympheny_toolbox.workflows`).
"""

from sympheny_toolbox._async import AsyncSympheny
from sympheny_toolbox._sync import Sympheny
from sympheny_toolbox.errors import APIError, AuthenticationError, NotFoundError, SymphenyError, UnexpectedResponseError


__all__ = [
    "APIError",
    "AsyncSympheny",
    "AuthenticationError",
    "NotFoundError",
    "Sympheny",
    "SymphenyError",
    "UnexpectedResponseError",
]

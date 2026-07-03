"""Shared fixtures: a mock Sympheny API served through ``httpx.MockTransport``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import httpx
import pytest

from sympheny_toolbox import AsyncSympheny, Sympheny


if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Iterator

BASE_URL = "https://api.sympheny.test"
TOKEN_PATH = "/backoffice/auth/ext/token"  # noqa: S105


class MockAPI:
    """In-memory fake of the Sympheny API.

    Responses are registered per ``(method, path)`` as a queue: each request
    consumes the next response, and the last registered one repeats. The token
    endpoint is built in and issues a fresh token (``tok-1``, ``tok-2``, ...)
    per authentication call. All non-token requests are recorded in ``requests``.
    """

    def __init__(self) -> None:
        self._routes: dict[tuple[str, str], list[httpx.Response]] = {}
        self.requests: list[httpx.Request] = []
        self.auth_calls = 0
        self.token_expires_in = 3600

    def add(self, method: str, path: str, json_body: Any = None, *, status_code: int = 200, content: bytes | None = None) -> None:
        response = httpx.Response(status_code, content=content) if content is not None else httpx.Response(status_code, json=json_body)
        self._routes.setdefault((method.upper(), path), []).append(response)

    def handler(self, request: httpx.Request) -> httpx.Response:
        path = request.url.path
        if path == TOKEN_PATH:
            self.auth_calls += 1
            return httpx.Response(200, json={"access_token": f"tok-{self.auth_calls}", "token_type": "Bearer", "expires_in": self.token_expires_in})
        self.requests.append(request)
        queue = self._routes.get((request.method, path))
        if not queue:
            return httpx.Response(500, text=f"MockAPI: no response registered for {request.method} {path}")
        return queue.pop(0) if len(queue) > 1 else queue[0]

    @property
    def last_request(self) -> httpx.Request:
        return self.requests[-1]

    @property
    def last_json(self) -> Any:
        return json.loads(self.requests[-1].content)


@pytest.fixture
def api() -> MockAPI:
    return MockAPI()


@pytest.fixture
def client(api: MockAPI) -> Iterator[Sympheny]:
    sympheny = Sympheny("user@example.com", "secret", base_url=BASE_URL)
    # The transport builds its own httpx client; swap it for one backed by the mock API.
    sympheny._transport._client = httpx.Client(base_url=BASE_URL, transport=httpx.MockTransport(api.handler))
    with sympheny:
        yield sympheny


@pytest.fixture
async def async_client(api: MockAPI) -> AsyncIterator[AsyncSympheny]:
    sympheny = AsyncSympheny("user@example.com", "secret", base_url=BASE_URL)
    sympheny._transport._client = httpx.AsyncClient(base_url=BASE_URL, transport=httpx.MockTransport(api.handler))
    async with sympheny:
        yield sympheny

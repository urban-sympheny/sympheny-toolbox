"""Tests for the authenticating transport: token lifecycle and error mapping."""

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx
import pytest

from sympheny_toolbox import AsyncSympheny, Sympheny
from sympheny_toolbox.errors import APIError, AuthenticationError, NotFoundError, PermissionDeniedError


if TYPE_CHECKING:
    from .conftest import MockAPI


SCENARIO_PATH = "/sympheny-app/scenario/scn-1"
SCENARIO_BODY = {"data": {"scenarioGuid": "scn-1", "scenarioName": "Test scenario"}}


def test_authenticates_lazily_and_caches_token(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", SCENARIO_PATH, SCENARIO_BODY)

    assert api.auth_calls == 0  # no token fetched at construction time
    client.scenarios.get("scn-1")
    client.scenarios.get("scn-1")

    assert api.auth_calls == 1
    assert all(request.headers["Authorization"] == "Bearer tok-1" for request in api.requests)


def test_reauthenticates_after_token_expiry(client: Sympheny, api: MockAPI) -> None:
    api.token_expires_in = 30  # below the 60 s expiry margin: token is immediately stale
    api.add("GET", SCENARIO_PATH, SCENARIO_BODY)

    client.scenarios.get("scn-1")
    client.scenarios.get("scn-1")

    assert api.auth_calls == 2
    assert api.requests[-1].headers["Authorization"] == "Bearer tok-2"


def test_retries_once_with_fresh_token_on_401(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", SCENARIO_PATH, {"message": "token revoked"}, status_code=401)
    api.add("GET", SCENARIO_PATH, SCENARIO_BODY)

    scenario = client.scenarios.get("scn-1")

    assert scenario.scenario_name == "Test scenario"
    assert api.auth_calls == 2
    assert api.requests[-1].headers["Authorization"] == "Bearer tok-2"


def test_persistent_401_raises_authentication_error(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", SCENARIO_PATH, {"message": "nope"}, status_code=401)
    api.add("GET", SCENARIO_PATH, {"message": "still nope"}, status_code=401)

    with pytest.raises(AuthenticationError) as exc_info:
        client.scenarios.get("scn-1")
    assert exc_info.value.status_code == 401


def test_403_raises_permission_denied_error(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", SCENARIO_PATH, {"message": "forbidden"}, status_code=403)

    with pytest.raises(PermissionDeniedError) as exc_info:
        client.scenarios.get("scn-1")
    assert exc_info.value.status_code == 403


def test_404_raises_not_found_error(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", "/sympheny-app/scenario/missing", {"message": "gone"}, status_code=404)

    with pytest.raises(NotFoundError) as exc_info:
        client.scenarios.get("missing")
    assert exc_info.value.status_code == 404


def test_500_raises_api_error_with_body(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", SCENARIO_PATH, {"message": "boom"}, status_code=500)

    with pytest.raises(APIError) as exc_info:
        client.scenarios.get("scn-1")
    error = exc_info.value
    assert error.status_code == 500
    assert error.body is not None
    assert "boom" in error.body
    assert SCENARIO_PATH in str(error)


def test_empty_response_body_returns_none(client: Sympheny, api: MockAPI) -> None:
    api.add("PUT", "/sympheny-app/scenarios/scn-1/close-diagram", content=b"", status_code=204)

    assert client._transport.request_json("PUT", "/sympheny-app/scenarios/scn-1/close-diagram") is None


def test_unauthenticated_request_sends_no_auth_header(client: Sympheny, api: MockAPI) -> None:
    api.add("PUT", "/bucket/upload", content=b"", status_code=200)

    client.unofficial.upload_to_presigned_url("https://api.sympheny.test/bucket/upload", b"file-content")

    request = api.last_request
    assert "Authorization" not in request.headers
    assert request.content == b"file-content"
    assert api.auth_calls == 0


async def test_async_client_authenticates_and_maps_errors(async_client: AsyncSympheny, api: MockAPI) -> None:
    api.add("GET", SCENARIO_PATH, SCENARIO_BODY)
    api.add("GET", "/sympheny-app/scenario/missing", {"message": "gone"}, status_code=404)

    scenario = await async_client.scenarios.get("scn-1")
    assert scenario.scenario_guid == "scn-1"
    assert api.last_request.headers["Authorization"] == "Bearer tok-1"

    with pytest.raises(NotFoundError):
        await async_client.scenarios.get("missing")


def test_base_url_selection() -> None:
    default_client = Sympheny("u", "p")
    dev_client = Sympheny("u", "p", is_dev=True)
    override_client = Sympheny("u", "p", is_dev=True, base_url="https://example.test")
    try:
        assert httpx.URL(default_client.base_url).host == "eu-north-1-api.sympheny.com"
        assert httpx.URL(dev_client.base_url).host == "eu-north-1-api.dev.sympheny.com"
        assert httpx.URL(override_client.base_url).host == "example.test"
    finally:
        default_client.close()
        dev_client.close()
        override_client.close()

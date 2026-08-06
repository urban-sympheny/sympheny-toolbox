"""Operations on user accounts of the Sympheny backoffice API (``External Users``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox.models import GetUserProfileExt


if TYPE_CHECKING:
    from sympheny_toolbox._async._transport import AsyncTransport


class AsyncUsers:
    """User account endpoints (``External Users``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def profile(self) -> GetUserProfileExt:
        """Get the profile of the authenticated user. ``GET /backoffice/ext/users/profile``"""
        raw = await self._t.request_json("GET", "/backoffice/ext/users/profile")
        return GetUserProfileExt.model_validate(raw)

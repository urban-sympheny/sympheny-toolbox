"""Tests for the ``.properties`` credential loading utilities."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from sympheny_toolbox.utils import load_creds_basic, load_properties


if TYPE_CHECKING:
    from pathlib import Path


def test_load_properties(tmp_path: Path) -> None:
    path = tmp_path / "creds.properties"
    path.write_text(
        "# a comment\n"
        "! another comment\n"
        "\n"
        "username=user@example.com\n"
        "password = s3cret=with=equals\n"
        "url: https://example.test\n"
        "  indented.key = value  \n"
        "line without separator\n",
        encoding="utf-8",
    )

    properties = load_properties(path)

    assert properties == {
        "username": "user@example.com",
        "password": "s3cret=with=equals",
        "url": "https://example.test",
        "indented.key": "value",
    }


def test_load_creds_basic(tmp_path: Path) -> None:
    path = tmp_path / "creds.properties"
    path.write_text("username=user@example.com\npassword=hunter2\n", encoding="utf-8")

    assert load_creds_basic(path) == ("user@example.com", "hunter2")


def test_load_creds_basic_missing_key(tmp_path: Path) -> None:
    path = tmp_path / "creds.properties"
    path.write_text("username=user@example.com\n", encoding="utf-8")

    with pytest.raises(KeyError):
        load_creds_basic(path)

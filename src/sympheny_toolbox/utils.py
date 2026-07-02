"""Small utilities: credential loading from Java-style ``.properties`` files."""

from __future__ import annotations

from pathlib import Path


def load_properties(path: str | Path) -> dict[str, str]:
    """Parse a simple Java-style ``.properties`` file into a dict.

    Supports ``key=value`` and ``key: value`` lines, blank lines, and comments
    starting with ``#`` or ``!``. Escape sequences and multi-line values are not
    supported.
    """
    properties: dict[str, str] = {}
    for raw_line in Path(path).read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith(("#", "!")):
            continue
        separator_index = min((i for i in (line.find("="), line.find(":")) if i >= 0), default=-1)
        if separator_index < 0:
            continue
        key = line[:separator_index].strip()
        value = line[separator_index + 1 :].strip()
        properties[key] = value
    return properties


def load_creds_basic(path: str | Path) -> tuple[str, str]:
    """Load ``username`` and ``password`` from a ``.properties`` file."""
    properties = load_properties(path)
    return properties["username"], properties["password"]

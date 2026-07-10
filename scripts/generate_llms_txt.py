"""Generate ``llms.txt`` and ``llms-full.txt`` for AI consumers.

Both files are derived from the ``zensical.toml`` nav and the Markdown sources
under ``docs/`` — no network, deterministic output. They are written into the
built site (default ``site/``) so they are served from the site root, following
the `llms.txt <https://llmstxt.org/>`_ convention:

* ``llms.txt`` — a compact, nav-ordered index: one bullet per page with its
  title, URL, and a one-line description.
* ``llms-full.txt`` — every page's Markdown body concatenated in nav order, for
  tools that want the whole corpus in a single fetch.

Run after ``zensical build`` (which creates and, with ``--clean``, wipes the
output directory):

    uv run python scripts/generate_llms_txt.py

Pass ``--output DIR`` to write somewhere other than ``site/``.
"""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG = REPO_ROOT / "zensical.toml"
DOCS = REPO_ROOT / "docs"
DEFAULT_OUTPUT = REPO_ROOT / "site"

_FRONT_MATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
_GENERATED_RE = re.compile(r"\A<!-- GENERATED.*?-->\n", re.DOTALL)
_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_DESC_LIMIT = 200


def load_config() -> dict[str, Any]:
    with CONFIG.open("rb") as fh:
        project: dict[str, Any] = tomllib.load(fh)["project"]
    return project


def collect_pages(entry: object) -> list[str]:
    """Return the leaf page paths under a single nav entry, in order."""
    if isinstance(entry, str):
        return [entry]
    if not isinstance(entry, dict):
        return []
    ((_, value),) = entry.items()
    if isinstance(value, str):
        return [value]
    pages: list[str] = []
    for child in value:
        pages.extend(collect_pages(child))
    return pages


def top_level_sections(nav: list[dict]) -> list[tuple[str, list[str]]]:
    """Split the nav into ``(section title, [page paths])`` groups (one per tab)."""
    sections: list[tuple[str, list[str]]] = []
    for item in nav:
        ((title, value),) = item.items()
        pages = [value] if isinstance(value, str) else [p for child in value for p in collect_pages(child)]
        sections.append((title, pages))
    return sections


def strip_metadata(text: str) -> str:
    """Drop YAML front matter and any leading GENERATED comment."""
    text = _FRONT_MATTER_RE.sub("", text)
    return _GENERATED_RE.sub("", text)


def extract_title(body: str, path: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.rsplit("/", 1)[-1].removesuffix(".md")


def extract_description(body: str) -> str:
    """The first prose paragraph after the H1, flattened to one line."""
    started = False
    para: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not started:
            if stripped.startswith("# "):
                started = True
            continue
        if not stripped:
            if para:
                break
            continue
        # Skip non-prose lead blocks (images, HTML, headings, lists, tables, ...).
        if stripped.startswith(("![", "<", "#", "-", "*", ">", "|", "!!!", "```", "===", "|")):
            if para:
                break
            continue
        para.append(stripped)
    text = _LINK_RE.sub(r"\1", " ".join(para))
    text = re.sub(r"[`*_]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= _DESC_LIMIT:
        return text
    return text[:_DESC_LIMIT].rsplit(" ", 1)[0] + "…"


def page_url(path: str, site_url: str) -> str:
    slug = path.removesuffix(".md").removesuffix("index").strip("/")
    base = site_url.rstrip("/")
    return f"{base}/{slug}/" if slug else f"{base}/"


def build_index(config: dict, sections: list[tuple[str, list[str]]]) -> str:
    lines = [f"# {config['site_name']}", "", f"> {config['site_description']}", ""]
    for title, pages in sections:
        lines.append(f"## {title}")
        lines.append("")
        for path in pages:
            body = strip_metadata((DOCS / path).read_text())
            page_title = extract_title(body, path)
            desc = extract_description(body)
            url = page_url(path, config["site_url"])
            lines.append(f"- [{page_title}]({url}): {desc}" if desc else f"- [{page_title}]({url})")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_full(config: dict, sections: list[tuple[str, list[str]]]) -> str:
    parts = [f"# {config['site_name']}", "", f"> {config['site_description']}", ""]
    for _, pages in sections:
        for path in pages:
            body = strip_metadata((DOCS / path).read_text()).strip()
            url = page_url(path, config["site_url"])
            parts.append("---")
            parts.append("")
            parts.append(f"<!-- Source: {url} -->")
            parts.append("")
            parts.append(body)
            parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    args = sys.argv[1:]
    output = DEFAULT_OUTPUT
    if "--output" in args:
        output = Path(args[args.index("--output") + 1])

    config = load_config()
    sections = top_level_sections(config["nav"])

    output.mkdir(parents=True, exist_ok=True)
    page_count = sum(len(pages) for _, pages in sections)
    (output / "llms.txt").write_text(build_index(config, sections))
    (output / "llms-full.txt").write_text(build_full(config, sections))
    print(f"Wrote llms.txt and llms-full.txt ({page_count} pages) into {output}/")


if __name__ == "__main__":
    main()

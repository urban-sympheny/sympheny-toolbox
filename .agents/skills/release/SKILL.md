---
name: release
description: >
  How to prepare a release of sympheny-toolbox — pick the semantic-version bump,
  close out the changelog, bump pyproject.toml, and verify. Use this skill
  whenever the maintainer asks to release, cut a version, bump the version, or
  prepare a version for PyPI. Publishing itself is maintainer-only: the agent
  never tags and never pushes.
---

# Release skill

A release is a staged change in the working tree, not an action against PyPI.
The agent prepares it; the maintainer pushes and tags.

## Steps

1. **Read `[Unreleased]` in `CHANGELOG.md` and pick the bump** from what is
   actually in it: any breaking change → MAJOR, new backward-compatible
   features → MINOR, fixes only → PATCH. `Docs`-only entries do not force a
   bump beyond PATCH.
2. **Close out the changelog.** Rename `[Unreleased]` to
   `## [X.Y.Z] - YYYY-MM-DD` (today's date), keep the Keep a Changelog
   categories (`Added` / `Changed` / `Fixed` / `Removed` / `Docs`), and start a
   fresh empty `## [Unreleased]` above it. Add the release's link reference at
   the bottom of the file alongside the existing ones.
   - Entries describe the net change against the **previous released version**.
     When closing out a final release that had pre-releases, consolidate them
     into one section and drop intra-prerelease churn — anything added and
     removed again before the final release does not belong in the entry.
3. **Bump `version` in `pyproject.toml`** to the same `X.Y.Z`, in the same
   change. The publish workflow refuses a tag that disagrees with it.
4. **Verify** (below).
5. **Hand off.** Report that the release is staged and that the maintainer
   pushes and tags `vX.Y.Z` to trigger the PyPI publish; the workflow re-checks
   that the tag matches the project version and runs `./scripts/check.sh --ci`.
   Do not tag, do not push, and do not commit unless asked.

## Verification (end every release prep with this)

1. `./scripts/check.sh` — must pass.
2. `uv run zensical build --clean --strict` — must succeed with zero warnings
   (full docs rules: `.agents/skills/docs/SKILL.md`).
3. Grep for stale version strings — old or pre-release numbers left in
   `README.md`, `docs/`, or elsewhere — and fix them.
4. Confirm the working tree contains only the intended files: never stage local
   environment files (`.claude/`, scratch files, editor config).

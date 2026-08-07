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
4. **Run `uv lock`** after the bump, so `uv.lock`'s pinned `sympheny-toolbox`
   version matches. Both `ci.yml` and `docs.yml` install with
   `uv sync --locked`, which hard-fails on drift instead of re-locking — a
   stale lock breaks the install step on every pipeline, including ones
   unrelated to the release. `uv.lock` is part of the release change, not a
   follow-up: it belongs beside `CHANGELOG.md` and `pyproject.toml` in the same
   commit whenever a commit is asked for.
5. **Verify** (below).
6. **Hand off.** Report that the release is staged in the working tree and give
   the maintainer the commands to run themselves — commit the release files,
   merge/push `main`, then tag the release commit and push the tag:
   ```sh
   git add CHANGELOG.md pyproject.toml uv.lock
   git commit -m "chore: release vX.Y.Z"
   git push origin main
   git tag -a vX.Y.Z -m "vX.Y.Z"
   git push origin vX.Y.Z
   ```
   Pushing the tag triggers `publish.yml`, which runs the full CI job, re-checks
   that the tag matches `uv version --short`, then builds and publishes. The tag
   must point at the commit that carries the bump. Do not tag, do not push, and
   do not commit unless asked — give the commands, don't run them.

## Verification (end every release prep with this)

1. `./scripts/check.sh` — must pass.
2. `uv run zensical build --clean --strict` — must succeed with zero warnings
   (full docs rules: `.agents/skills/docs/SKILL.md`).
3. Grep for stale version strings — old or pre-release numbers left in
   `README.md`, `docs/`, or elsewhere — and fix them.
4. Confirm the lock was regenerated: `git diff uv.lock` must show the
   `sympheny-toolbox` version line moving to `X.Y.Z`. An unchanged `uv.lock`
   means step 4 was skipped and CI will fail on `uv sync --locked`.
5. `git status` — the working tree should carry `CHANGELOG.md`,
   `pyproject.toml`, `uv.lock`, and nothing else beyond the release's own
   changes. Never include local environment files (`.claude/`, scratch files,
   editor config).

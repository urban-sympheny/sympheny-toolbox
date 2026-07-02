# Task: Agent Instructions Setup + API Client Migration (sympheny-toolbox)

## Working process
- This is a multi-step project. Don't try to finish it in one session — work through the phases below and pause for review between them.
- Before starting each phase, ask me any clarifying questions you need. Don't silently guess on anything that affects architecture, tooling, or file layout.
- Before writing code, briefly propose your plan/file layout for that phase and wait for confirmation.

## Global rules (apply to every phase — also copy these into AGENTS.md)
- Never push commits to the remote. I review and push myself. Only create local commits if I explicitly ask you to.
- Prefer the Python standard library. Only add a third-party dependency if it gives a clear, real benefit over the stdlib equivalent — check before adding, don't assume.
- Keep things minimal — no speculative abstractions, no unused tooling.
- Maintain semantic versioning (MAJOR.MINOR.PATCH):
  - MAJOR — breaking API changes
  - MINOR — new, backward-compatible features
  - PATCH — bug fixes
- Update docs whenever behavior or interfaces change.
- Update tests whenever behavior or interfaces change (once the test suite exists — see Phase 3).

---

## Phase 1 — Agent instruction files

**Goal:** one tool-agnostic instruction setup that works for any AI coding agent, not just Claude.

1. Create `AGENTS.md` at the repo root.
   - Content: the "Global rules" above, plus any other essential conventions for this repo (formatting, linting, structure). Keep it tight — only things that actually change agent behavior. No objectives, no project background — this file is rules only.
   - Research current best practices for AGENTS.md-style instruction files (e.g. the emerging agents.md convention) before writing it, and follow them where they make sense here.
2. Create `CLAUDE.md` at the repo root that simply points to `AGENTS.md` — a short stub, not a duplicate.
3. If any skills get added for this repo, put them under `.agents/skills/` and symlink `.claude/skills -> .agents/skills`, so Claude Code picks them up without duplicating content.
4. Check whether any MCP servers would meaningfully help agents working in this repo (e.g. Context7 for up-to-date library docs) and add config for them only if genuinely useful — don't add speculatively.
5. Tell me whether a `docs/adr/` (Architecture Decision Records) folder is worth adding for this repo, with your reasoning — I haven't decided yet.

---

## Phase 2 — API client from OpenAPI spec

**Input spec:** `docs/sympheny_openapi.json` (already in the repo).

1. Build a client for this API from the spec, optimizing for efficiency, readability, and idiomatic Python. Evaluate codegen tools vs. a hand-written client and pick whichever gets us there with the least bloat — explain the tradeoff.
2. We need both sync and async call support. Decide the best way to provide both (e.g. `httpx` supports both natively) and justify the choice.
3. Some existing calls in the current client aren't in `sympheny_openapi.json`. Keep them, but clearly mark them (naming, docstrings, or module separation) as **not part of the official documented API**, so they're easy to distinguish from spec-backed calls.
4. Evaluate tooling before committing to it. For each of the following, check whether stdlib gives comparable quality; only keep what earns its place:
   - **Pydantic** — request/response models + validation
   - **httpx** — sync + async HTTP
   - **Polars** — only if there's an actual data-handling need in this client; don't add it speculatively
5. This migration is a breaking API change — bump the package **MAJOR** version as part of this phase.

---

## Phase 3 — Tests (later, not now)
Flag this as a follow-up once the client is stable. Don't build it yet.

---

## Background context (for your awareness only — do NOT put this in AGENTS.md)
- This client has two eventual audiences: it will be embedded in an MCP server so AI tools can call it, and it will also be used directly by customers as a standalone API client package. **The MCP use case is the first priority** — optimize for that first — but keep the client's public surface (naming, models, error handling) clean and stable enough that customer-facing use later doesn't force a rework or another breaking version bump.
- We'll eventually publish API docs + usage examples (ReadTheDocs or another option — not decided yet). Keep docstrings and structure documentation-friendly, but don't build the doc site now.
- The test suite is a deliberate second step (Phase 3), not part of this pass.

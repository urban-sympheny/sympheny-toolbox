---
name: docs
description: >
  How to create, regenerate, and edit pages of the product documentation site
  (Zensical, four surfaces: Web app / REST API / Python SDK / MCP). Use this
  skill for ANY task that touches the docs/ directory or zensical.toml — writing or
  editing a guide, regenerating the SDK reference after SDK changes, regenerating
  the REST API reference after the OpenAPI spec (specs/sympheny_openapi.json)
  changes, adding a page to the nav,
  fixing links, or reviewing docs in a PR — even if the user doesn't say "docs"
  explicitly (e.g. "the new endpoint needs to be documented", "update the site
  after this SDK change").
---

# Docs Skill

This repo's documentation is a Zensical site built from Markdown in
`docs/`, configured by `zensical.toml`, deployed by GitHub Actions to Pages.
Two parts of the site are **generated** and must never be hand-edited; the rest
is hand-written prose that follows the conventions below.

## Ground rules (read before any docs task)

1. **Markdown + the sanctioned extension whitelist.** Pages may use exactly
   the syntax enabled by the `markdown_extensions` listed in `zensical.toml`
   (currently: admonitions, collapsible details, content tabs, code blocks,
   `attr_list` — which covers buttons like `[Text](page.md){ .md-button }` —
   and toc permalinks). Two extensions carry a **narrowed sanction** (Phase 5b):
   `md_in_html` may be used **only** for the upstream
   `<div class="grid cards" markdown>` card grid on index/landing pages, and
   `pymdownx.emoji` **only** for bundled-set icon and arrow shortcodes
   (`:material-web:`, `:octicons-arrow-right-24:`, …) inside those cards —
   neither licenses arbitrary raw HTML or decorative emoji elsewhere. MDX,
   React components, and other raw HTML are banned, with two exceptions: the
   GENERATED header comment and
   `<video controls preload="metadata" src="…"></video>` for S3-hosted
   screencasts. If content genuinely needs something with no equivalent in
   the whitelist, **do not silently drop it or hack raw HTML** — flag it with
   `TODO(review)`, tell the maintainer in your report, and propose either a
   new whitelisted extension or a new sanctioned HTML element (that's how
   `<video>` was approved). Extending the whitelist is a deliberate
   maintainer decision, made in `zensical.toml`, never ad-hoc per page.
   Two further **infrastructure** sanctions (Phase 5c) sit outside page
   content and do not license raw HTML in Markdown: (a) a `custom_dir`
   theme override (`overrides/main.html`) is permitted **only** for the
   announcement bar's `announce` block (the dismissible beta banner) — no
   other block overrides; (b) HTML inside `zensical.toml` **config values** —
   the `copyright` footer string and the `extra.consent` description — is
   permitted for their links (Support / Privacy policy / Change cookie
   settings, and the privacy-policy link). One `docs/api/explorer.html` is a
   standalone non-Markdown page (the Scalar API explorer, kept 2026-07-10,
   not in the nav) copied verbatim, not Markdown content. There is NO
   `extra_javascript` — a snippet was tried 2026-07-10 and reverted after it
   interfered with content tabs. None of these relax the Markdown-only rule
   for pages.
2. **Generated pages are outputs, not sources.** Pages beginning with
   `<!-- GENERATED` (all of `docs/api/reference/` and `docs/sdk/reference/`)
   are produced by scripts/tasks in this skill. To change them, change the
   source (docstrings, `specs/sympheny_openapi.json`, generator, templates) and regenerate.
   If you find yourself editing one directly, stop — that edit will be
   destroyed on the next regeneration.
3. **One conceptual SDK.** The SDK ships identical sync and async clients —
   `Sympheny` and `AsyncSympheny` (the sync one is code-generated from the
   async source by `scripts/generate_sync.py`). The docs describe
   **only the async client**; sync appears only inside tabbed code snippets.
   Never create a page, nav entry, or heading for the sync client — it would
   double the reference and the search results for zero information.
4. **Every code example must run.** Execute snippets against the SDK before
   committing. If an example can't be run (needs prod data), mark it
   `<!-- illustrative-only -->` so reviewers know.
5. **Don't invent product facts.** If you're unsure how the product behaves,
   write `<!-- TODO(review): <your question> -->` and move on. A gap flagged
   for a human beats a confident hallucination in customer-facing docs.
6. **Verify before you finish.** Every task ends with the Verification section
   at the bottom of this file.

## Looking up Zensical behavior (context7 MCP)

Zensical is pre-1.0 and changes fast — your training data about it is stale or
absent, and it is NOT MkDocs/Material (close cousin, diverging config and
feature set). Never answer a Zensical question from memory:

1. **First stop: the context7 MCP server**, library ID `/zensical/docs` (the
   official docs repo — skip the resolve step and query it directly). Use it
   for any Zensical uncertainty: `zensical.toml` keys, theme features, nav
   syntax, markdown extension behavior, `--strict`/`--clean` semantics, CLI
   flags. One focused question per query. Prefer it over web search.
2. Context7 answers often show paired `mkdocs.yml`/`zensical.toml` examples —
   this repo is **`zensical.toml` only**; ignore the YAML variant.
3. Docs describe the latest release; this repo pins `zensical==<version>` in
   `pyproject.toml`. If a documented feature doesn't work, check the pin
   before assuming user error — and confirm against the installed package
   (`.venv/.../zensical/`) or a throwaway build in your scratchpad when it
   matters. Policy: keep the `==` pin and bump it deliberately in a dedicated
   PR (reviewed quarterly) whose only check is "site builds + links valid +
   visual spot-check" — Zensical is pre-1.0; an unpinned dep breaks CI on
   upstream's schedule. Always build with `--clean`.
4. Finding a feature in the docs is **not** permission to use it: the
   extension whitelist and sanctions recorded in ground rule 1 still govern.
   New extensions, theme features, or plugins go through the escalation rule
   (ground rule 1).
5. If the context7 server isn't connected in your session, fall back to
   <https://zensical.org/docs/> via web fetch; the same rules apply.

## Site map (where things go)

| Content type | Location | Kind |
|---|---|---|
| Web-app / product guides, concepts | `docs/web-app/` | hand-written |
| REST API overview + auth | `docs/api/index.md`, `docs/api/authentication.md` | hand-written |
| REST API reference (per tag) | `docs/api/reference/` | **generated** from `specs/sympheny_openapi.json` |
| SDK install/quickstart, sync-vs-async explainer | `docs/sdk/index.md` | hand-written |
| SDK workflow guides (multi-step flows) | `docs/sdk/workflows/` | hand-written |
| SDK reference (per resource group) + models | `docs/sdk/reference/` | **generated** from async client source |
| AI-tooling docs ("Use with AI") | `docs/ai/` | hand-written (MCP setup + llms.txt; placeholder until MCP ships) |
| operationId ↔ SDK method mapping | `docs/_data/sdk_map.yml` | generated, committed |

Concepts (energy-system modelling vocabulary) live once, under
`docs/web-app/concepts/`. Link to them; never restate them.

## Task: regen-api-reference

Run when `specs/sympheny_openapi.json` changes, or when CI's stale-generation
check fails. (The spec itself is maintainer-merged by `scripts/merge_openapi.py`
from private upstream exports — never hand-edit or regenerate it yourself.)

1. Run the generator: `uv run python scripts/generate_api_reference.py`
   (reads the committed `specs/sympheny_openapi.json` — never fetch a live endpoint).
2. Confirm output invariants:
   - one page per tag under `docs/api/reference/`, deterministic order;
   - each operation has anchor `#operation-{operationId}`;
   - each operation cross-links its SDK method via `docs/_data/sdk_map.yml`
     (missing mapping entries → add them, don't drop the link silently);
   - GENERATED header present on every page.
3. If the spec added/removed tags, update the `zensical.toml` nav accordingly.
4. Verify (see below), commit generated pages + nav change together with the
   spec change or in the immediately following PR.

## Task: regen-sdk-reference

Run whenever the SDK's public surface changes (new/removed/renamed methods,
changed signatures or docstrings, new models), or when the drift-detector CI
fails.

1. Source of truth: the **async** client classes (`src/sympheny_toolbox/_async/`)
   and the Pydantic models module (`src/sympheny_toolbox/models.py`, itself
   generated from the spec). Read the changed resource group(s); do not
   regenerate untouched groups unless templates changed.
2. For each affected resource group, write `docs/sdk/reference/{resource}.md`:
   - one `##` section per method with anchor `#method-{resource}-{method_name}`;
   - async signature, then the docstring rendered as prose (method docstrings
     are one-line summaries embedding the REST method + path, not Google-style
     Args/Returns blocks) + parameter/return tables derived from the typed
     signature and models;
   - model names link into the models pages (models are grouped by resource,
     not one giant page — 191 models don't fit on one page);
   - a tabbed usage snippet, Sync tab and Async tab, identical except
     `Sympheny`/`AsyncSympheny` and `await` (see Conventions for the exact syntax);
   - cross-link to the REST operation via `sdk_map.yml`;
   - GENERATED header.
3. Update `docs/_data/sdk_map.yml` for any new/renamed methods.
4. Do NOT create anything documenting the sync client (ground rule 3).
5. Run the drift detector (`uv run python scripts/check_sdk_docs_drift.py`) — it must
   pass. Verify, then commit.

## Task: write or edit a guide

1. Place it per the site map; add it to the `zensical.toml` nav (nav is
   explicit — an unlisted page is invisible).
2. Follow Conventions below. Structure: what the reader will achieve (1–2
   sentences) → prerequisites → numbered steps with runnable code → what to
   read next (2–3 relative links into the references or concepts).
3. Deep-link generously: SDK method mentions link to
   `../reference/{resource}.md#method-...`; REST operations to
   `../../api/reference/{tag}.md#operation-...`; concepts to
   `../../web-app/concepts/...`.
4. Run every snippet (ground rule 4). Verify, commit.

## Task: migrate a Confluence page

1. Convert to Markdown, then **rewrite** to the conventions — do not
   transcribe. Confluence content is known-outdated: check each claim against
   the current product; flag anything unverifiable with `TODO(review)`.
2. Split pages that mix concepts with how-to: concept → `web-app/concepts/`,
   procedure → `web-app/step-by-step-guide/` (or `web-app/advanced-workflows/`).
3. Note the superseded Confluence URL in the PR description so a redirect/
   banner can be placed on the old page.

## Conventions

**Style.** Second person ("you"), present tense, imperative steps. Short
paragraphs. One H1 per page (the title). Sentence-case headings. Spell out the
product's domain terms exactly as the UI does. No marketing tone.

**No em-dashes.** Never use `—` (or `–`) in page content. They read as
machine-written. Restructure the sentence instead: use a period and two short
sentences, a comma, a colon before a list or an explanation, or parentheses for
a genuine aside. The same goes for the bullet lists on landing pages: write
`[Hubs](hubs.md): the buildings or groups of buildings you model.` with a colon,
not a dash. Hyphens in compound words (`on-site`, `multi-energy`,
`sentence-case`) and minus signs in numbers are fine; it is only the long dash
that is banned. Two exceptions, both outside hand-written prose: the `GENERATED`
header emitted by the generators, and quoted product strings or API values that
contain a dash of their own.

A dash is also not a table placeholder. A cell with nothing to say reads `n/a`
(no unit, no default), and a cell for a required argument reads `required`. The
generators follow the same rule.

**Direct, human language.** Say the thing. Prefer the short common word over
the formal one (`use` not `utilize`, `about` not `regarding`, `so` not
`thereby`). Cut hedges and filler (`simply`, `just`, `please note that`,
`it is important to understand that`, `in order to`, `leverage`, `robust`,
`seamless`, `powerful`, `comprehensive`). Lead with the action, not the
preamble: "Click **Save**." beats "You will now want to make sure you click the
Save button." Address the reader's task, and where a limit or a gotcha exists,
state it plainly instead of softening it.

**Naming: nav title, filename, and H1 all match.** A page's file name is the
kebab-case form of its nav title, and its H1 is that title in sentence case.
Pick the title first, then derive the path from it.

| Nav title | Path | H1 |
| --- | --- | --- |
| Energy carriers step | `step-by-step-guide/energy-carriers-step.md` | `# Energy carriers step` |
| Sign up and log in | `getting-started/sign-up-and-log-in.md` | `# Sign up and log in` |
| Step-by-step guide | `step-by-step-guide/index.md` | `# Step-by-step guide` |
| Imports & exports step | `step-by-step-guide/imports-exports-step.md` | `# Imports & exports step` |
| What's new | `whats-new/index.md` | `# What's new` |

Rules that follow from it:

- Lowercase, words joined by single hyphens, no spaces, no underscores, no
  capitals. Punctuation is dropped rather than transliterated, so an apostrophe
  or an ampersand simply disappears (`What's new` → `whats-new`,
  `Imports & exports step` → `imports-exports-step`). Directories follow the same
  rule: a section directory is the kebab-case of its nav title.
- A section is a directory whose landing page is `index.md`, with an H1 equal to
  the section name.
- Keep the title short. The section already gives the context, so a page inside
  Getting started is `structure.md` ("Structure"), not
  `web-app-structure.md` ("Web app structure"), and a page inside Parameters is
  `hubs.md` ("Hubs"), not `hubs-parameters.md` ("Hubs parameters").
- Keep filler words out of the title itself (`the`, `a`, `how-to`,
  `introduction-to`), so that the filename can mirror it exactly: "Download
  results", not "Download the results". Use the plural the UI uses for list pages
  ("Analyses" → `analyses.md`, not `analysis.md`).
- Images live in the section's `img/` directory and are named after the page they
  belong to plus a counter (`quick-start-7.png`, `energy-carriers-step-2.png`). A
  picture used by more than one page gets a descriptive name instead
  (`database-center-panel.png`).
- Renaming a page changes its URL. Rename only when the title genuinely changed,
  rename its images in the same commit, repoint every relative link, and note
  the old path in the PR so a redirect can be added.

Three deliberate exceptions, and no others:

1. **Surface roots keep their short directory names** even though their nav
   titles are longer: `web-app/` ("Web app"), `api/` ("REST API"), `sdk/`
   ("Python SDK"), `ai/` ("Use with AI"). They sit in every URL on the site and
   in every relative link between surfaces, so they are stable by design.
2. **The site home** (`docs/index.md`, H1 "Sympheny documentation") is not a
   section index and has no directory to match.
3. **Release notes** are `whats-new/<month>-<year>.md` with an H1 of
   "`Month YYYY`" (`november-2025.md` → `# November 2025`). The nav lists them
   newest first, so the file name does not carry the ordering.

**Tabbed sync/async snippets** (linked tabs, and the reader's choice persists
site-wide):

```markdown
=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        scenario = await client.scenarios.get(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        scenario = client.scenarios.get(scenario_guid)
    ```
```

**Admonitions** for warnings and notes only, not for decoration:

```markdown
!!! warning
    `time_limit` is the solver's processing budget in **minutes** (queue time
    excluded), not seconds.
```

**Search tags.** Every hand-written page carries a YAML front-matter `tags:`
block (Zensical 0.0.47 renders chips and indexes the tags into search with zero
config). Tags are a fixed, closed vocabulary on two axes:

- **surface** (which of the four surfaces the page documents): `web-app`, `api`,
  `sdk`, `mcp`.
- **topic** (what kind of page it is): `getting-started`, `how-to`, `concepts`,
  `troubleshooting`, `workflow`, `release-notes`.

The convention, in full:

1. **Exactly one surface tag plus exactly one topic tag**, in that order,
   surface first. Two tags is the norm; three is already unusual and needs a
   reason.
2. **The topic tag matches the section the page lives in.** A page under
   `getting-started/` is tagged `getting-started`; a step page under
   `step-by-step-guide/` is `how-to`; anything under `concepts/` or
   `parameters/` is `concepts`; support and FAQ pages are `troubleshooting`;
   release notes are `release-notes`; SDK workflow guides are `workflow`. If the
   right topic tag is not the one its section implies, the page is in the wrong
   section. Move the page, don't bend the tag.
3. **A section landing page (`index.md`) may carry the surface tag alone.** The
   surface's own landing page (`web-app/index.md`) always does.
4. **The site home (`docs/index.md`) stays untagged.** It sits above all four
   surfaces, so no surface tag applies.
5. **Never coin a tag.** No product names, feature names, page titles, versions,
   or capitalised variants. Extending the vocabulary is a deliberate maintainer
   decision, like the extension whitelist (ground rule 1).
6. **Generated reference pages get tags only from their generators**, never by
   hand-editing the output (ground rule 2). Pages under `api/reference/` and
   `sdk/reference/` are currently untagged by design.

Front-matter shape, which is the whole of it:

```markdown
---
tags:
  - web-app
  - how-to
---

# Page title
```

Examples: a scenario-editor guide is `web-app` + `how-to`; an SDK workflow guide
is `sdk` + `workflow`; a release note is `web-app` + `release-notes`; the FAQ
page is `web-app` + `troubleshooting`.

**Links** are always relative (`../api/reference/scenarios.md#operation-...`),
never absolute site URLs. Relative links keep the corpus portable and let CI
validate them.

**GENERATED header** (first line of every generated page):

```markdown
<!-- GENERATED — do not edit by hand. Source: <path-to-source>.
     Regenerate: .agents/skills/docs/SKILL.md → task <task-name>. -->
```

## Verification (end every task with this)

1. `uv run zensical build --clean --strict` — must succeed with **zero
   warnings**; link validation failures are errors. Always pass `--clean`:
   Zensical's page cache is pre-1.0 and stale cache entries mask or invent
   warnings (CI builds with `--clean` too, per upstream guidance). Everything in `docs/` ends up in the
   built site (Zensical has no `exclude_docs`), which is why `docs/` holds
   only site content — the OpenAPI specs live in `specs/`, `KNOWN_ISSUES.md`
   at the repo root. Never add non-documentation files to `docs/`.
2. Serve locally and check the touched pages render: tabs toggle, tables fit,
   nav entry appears, search finds the page by its title.
3. For generated content: `git diff --stat` matches expectations (no churn in
   untouched groups), and the relevant CI script
   (`check_sdk_docs_drift.py` / stale-generation check) passes locally.
4. Confirm no page documents the sync client and no absolute internal links
   were introduced (`grep -rn "https://<docs-domain>" docs/` should be empty).
5. Style and naming pass on every page you touched:
   - No em-dashes: `grep -rn "—\|–" docs/ --include="*.md"` returns nothing
     outside the `GENERATED` headers.
   - Filenames are the kebab-case of their nav titles, and each H1 matches its
     nav title.
   - Front matter carries one surface tag plus one topic tag, and the topic tag
     matches the page's section (landing pages may carry the surface alone; the
     site home stays untagged).
   - Read the prose back once: no hedges or filler, no marketing adjectives, the
     action first in each step.

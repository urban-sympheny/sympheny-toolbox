# Help Center Migration Report

The Sympheny Help Center (Confluence) has been migrated to the new documentation
site. This report summarizes what moved, what improved along the way, and what
is still open.

**Last updated:** 2026-07-10

## The short version

Every one of the **76 Help Center pages is accounted for** — nothing was lost
silently. Each page was either migrated (usually improved along the way),
merged into a better home, recreated as an honest "coming soon" placeholder
(where Confluence itself never had real content), or deliberately dropped for a
stated reason.

| What happened to it | Pages |
|---|---|
| Migrated with content | 50 |
| Merged into another page | 7 |
| Recreated as "coming soon" (Confluence had no real content either) | 10 |
| Dropped deliberately | 9 |

## What the new site covers

The old Help Center only documented the web application. The new site has four
sections:

- **Web Application** — everything migrated from the Help Center: getting
  started, the quick-start walkthrough, how-to guides for projects, analyses
  and the scenario editor, the Database Center and EnyTool, all modelling
  concepts and parameter definitions, a glossary, release notes back to
  November 2021, and troubleshooting/FAQs.
- **REST API** — new: an overview, an authentication guide, a complete
  reference for all 87 API operations, and an interactive API explorer. This
  replaces (and goes far beyond) the old "Using the API" pages.
- **Python SDK** — new: install and quick-start guides, step-by-step workflow
  guides (create a scenario from Excel, run the solver, download results), and
  a complete reference of all SDK methods.
- **Use with AI** — new: how AI tools can consume our docs, and a placeholder
  for the upcoming MCP server.

## Improvements made during the migration

Pages were **rewritten, not copy-pasted**. Content was edited to a consistent
style guide; rough or outdated prose (notably the quick start, which was also
incomplete in Confluence) was fixed and completed. Claims we couldn't verify
were flagged for human review instead of being carried over blindly — all of
those flags have since been resolved.

- **18 screencast videos rescued.** The Confluence export silently dropped
  every embedded video from the release-notes pages. All 18 were recovered,
  given descriptive names, re-hosted on our own storage, and re-embedded on the
  right pages.
- **All attachments re-hosted.** 5 spreadsheet templates and the Zürich weather
  dataset were Confluence attachments that would have died with the old site;
  they now live on our own storage. 169 screenshots were optimized and moved
  with their pages.
- **No dead links.** Every link back to the old V2 help site or into live
  Confluence was removed — relinked to the migrated page where one exists,
  otherwise replaced with plain text.
- **Glossary rebuilt.** Instead of duplicating definitions, every term now
  links to its concept page — one place to maintain each definition.
- **Honest placeholders.** Ten Confluence pages had no real content (they just
  said "V3 docs coming soon" or were empty). These are now explicit
  "coming soon" pages that link the nearest real content, so no page pretends
  to document something it doesn't.

## What was dropped, and why

- **The tutorials section** (Tutorial 1 set-up and results, the V2→V3 migration
  guide) — outdated; decision by the maintainer.
- **"How to Model Specific Technologies"** (English + German) — was never part
  of the export; decided not to migrate.
- **Pure navigation pages** (User Guide, Usage Instructions, What's New
  containers) — replaced by the site navigation itself.
- **Empty pages** (API Workflow, Example Workflows) — there was nothing to
  migrate.

One earlier drop was reversed: the **EnyFlow framework** pages were restored by
maintainer decision and now live under the web-app how-to guides.

## Still open

- **Write real content for the 13 "coming soon" pages**: six concept pages
  (imports, exports, storage technologies, network technologies, intra-hub
  networks, technology packages), three scenario-editor steps (imports &
  exports, storage technologies, network links), executing scenarios, scenario
  results, output parameters, and common issues & solutions. These were
  placeholders in Confluence too — this is new writing, not migration debt.
- **Point people at the new site**: once it is the official home, the old
  Confluence pages should get a "we've moved" banner. Until then the new site
  shows a beta banner linking back to the legacy documentation.

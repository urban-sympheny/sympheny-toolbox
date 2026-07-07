---
tags:
  - mcp
---

# Use with AI

Sympheny is built to be driven by AI assistants and coding agents. This section covers the ways to connect Sympheny to an AI tool.

## MCP server

The Sympheny MCP server lets an AI assistant call the Sympheny API directly — creating scenarios, running solver jobs, and reading results — over a standard [Model Context Protocol](https://modelcontextprotocol.io/) connection.

!!! info "Coming soon"
    The MCP server has not been released yet. See [MCP server setup](mcp.md) for the configuration you will use once it ships.

Until then, drive Sympheny programmatically with the [REST API](../api/index.md) or the [Python SDK](../sdk/index.md) — both are agent-friendly and fully documented on this site.

## Machine-readable docs

This site publishes two machine-readable indexes, served from the site root and
regenerated on every build:

- [`llms.txt`](https://urban-sympheny.github.io/sympheny-toolbox/llms.txt) — a
  compact, nav-ordered index of every page with a one-line description.
- [`llms-full.txt`](https://urban-sympheny.github.io/sympheny-toolbox/llms-full.txt) —
  the full documentation concatenated in reading order, for tools that want the
  whole corpus in a single fetch.

Both follow the [llms.txt](https://llmstxt.org/) convention.

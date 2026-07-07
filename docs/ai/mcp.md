---
tags:
  - mcp
  - how-to
---

# MCP server setup

The Sympheny MCP server exposes the Sympheny API to AI assistants over the
[Model Context Protocol](https://modelcontextprotocol.io/), so a model can create
scenarios, run solver jobs, and read results without you wiring up HTTP calls
yourself. It is a remote server, reachable over streamable HTTP.

!!! warning "Not yet available"
    The MCP server has not been released. The configuration below is the shape
    you will use once it ships — the server URL is a **placeholder** and will not
    connect today. Authentication settings will be added here when the server is
    published; the exact scheme is not final yet.

Throughout this page the placeholder endpoint is:

```text
https://mcp.sympheny.com/mcp    # placeholder — not live yet
```

## Claude Code

Add the server from the CLI (the `--transport http` flag is required for a remote
server):

```bash
claude mcp add --transport http sympheny https://mcp.sympheny.com/mcp
```

To share the configuration with a team, use `--scope project`, which writes a
checked-in `.mcp.json`:

```json
{
  "mcpServers": {
    "sympheny": {
      "type": "http",
      "url": "https://mcp.sympheny.com/mcp"
    }
  }
}
```

Verify the connection with `claude mcp get sympheny` or the `/mcp` command.

## Claude Desktop

Open **Settings → Connectors → Add custom connector**, enter the server URL, and
click **Add**. This is the recommended path for remote servers — no config file
to edit.

## ChatGPT

Enable **Developer mode**, then open **Settings → Connectors → Create** and enter
the server URL. When calling a model through the API instead, add the server as an
MCP tool:

```json
{
  "type": "mcp",
  "server_label": "sympheny",
  "server_url": "https://mcp.sympheny.com/mcp"
}
```

## Gemini CLI

Add the server to `~/.gemini/settings.json` under `mcpServers`, using `httpUrl`
for the streamable-HTTP transport:

```json
{
  "mcpServers": {
    "sympheny": {
      "httpUrl": "https://mcp.sympheny.com/mcp"
    }
  }
}
```

---

Not using an MCP client yet? Drive Sympheny with the [REST API](../api/index.md)
or the [Python SDK](../sdk/index.md) today.

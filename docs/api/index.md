---
tags:
  - api
---

# REST API

The Sympheny REST API gives you programmatic access to everything you can do in
the Sympheny web application: create projects and analyses, model energy hubs,
demands, supply technologies and networks, run optimizations, and integrate
Sympheny into your own tools and workflows.

If you work in Python, the [Python SDK](../sdk/index.md) wraps this API with
typed methods and automatic authentication — prefer it over calling the API
directly.

## Base URL

All requests go to a single host:

```
https://eu-north-1-api.sympheny.com
```

The path prefix selects the API area:

| Prefix | Area | What it covers |
| --- | --- | --- |
| `/sympheny-app` | Web application | Projects, analyses, scenarios, hubs, energy carriers, demands, technologies, networks. |
| `/backoffice` | Account | Access tokens and your user profile. |
| `/sense-api` | Solver | Submitting solver jobs, tracking their progress, and your job quota. |

## Authentication

Every endpoint except the token endpoint requires a Bearer token in the
`Authorization` header. See [Authentication](authentication.md) for the
login flow.

## Versioning

Some web application endpoints carry a version segment in the path (`v2`, `v2_1`,
`v2_2`). The [reference](reference/projects.md) documents the current version
of each operation — use the paths exactly as shown there.

## Responses and errors

Web application (`/sympheny-app`) endpoints wrap every response in an envelope:

```json
{
  "data": { ... },
  "status": { "code": "...", "desc": "...", "message": "..." }
}
```

The payload is in `data`; `status` carries a machine-readable code and a
human-readable message. Account (`/backoffice`) and solver (`/sense-api`)
endpoints return the payload directly and report errors as a JSON object with
a `detail` field.

Errors use conventional HTTP status codes: `400` for invalid input, `401` for
a missing, invalid, or expired token, `403` when the action isn't permitted
for your account, `404` for an unknown resource, `409` for conflicts (for
example a duplicate name), and `422` for request validation failures on
account and solver endpoints.

## Known issues

Some endpoints have surprising behaviors with client-side workarounds. They
are tracked in
[KNOWN_ISSUES.md](https://github.com/urban-sympheny/sympheny-toolbox/blob/main/KNOWN_ISSUES.md)
in the SDK repository.

## Reference

The [API reference](reference/projects.md) documents all operations, grouped
by resource — each page lists the operations' parameters, request and response
schemas, and example requests.

## API Explorer

Prefer trying requests as you read? The
[API Explorer](explorer.html){ target="_blank" rel="noopener" } renders the
same specification interactively with live "try it" support — paste a
[bearer token](authentication.md) and send requests straight from the browser.
It opens in a new tab; this reference stays the canonical documentation.

---
tags:
  - api
  - getting-started
---

# Authentication

The API authenticates with JWT Bearer tokens. You exchange your Sympheny
account credentials (the email and password you use to log in to the web
application) for an access token, then send that token with every request.

## Get a token

Call
[`POST /backoffice/auth/ext/token`](reference/auth.md#operation-post_oauth_webapp_backoffice_auth_ext_token_post)
with your credentials:

<!-- illustrative-only: requires real account credentials -->

=== "curl"

    ```bash
    curl -X POST "https://eu-north-1-api.sympheny.com/backoffice/auth/ext/token" \
      -H "Content-Type: application/json" \
      -d '{"email": "you@example.com", "password": "..."}'
    ```

=== "Python"

    ```python
    import httpx

    response = httpx.post(
        "https://eu-north-1-api.sympheny.com/backoffice/auth/ext/token",
        json={"email": "you@example.com", "password": "..."},
    )
    response.raise_for_status()
    token = response.json()["access_token"]
    ```

The response contains the token and its lifetime in seconds:

```json
{
  "access_token": "eyJhbGciOi...",
  "token_type": "Bearer",
  "expires_in": 86400
}
```

The token endpoint is rate-limited against bursts of login attempts, so fetch
a token once and reuse it until expiry rather than logging in per request.

## Use the token

Send the token in the `Authorization` header of every request:

```bash
curl "https://eu-north-1-api.sympheny.com/sympheny-app/projects" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

A missing, invalid, or expired token yields `401 Unauthorized`.

## Token lifetime

Tokens expire `expires_in` seconds after they are issued and cannot be
refreshed. Request a new one the same way. Tokens can also be revoked before
their stated expiry, so treat any `401` as a signal to re-authenticate and
retry once.

!!! note
    The [Python SDK](../sdk/index.md) does all of this for you: it fetches a
    token lazily on the first request, caches it until shortly before expiry,
    and retries once with a fresh token on `401`.

## Keep credentials out of code

Read credentials from environment variables or a local file excluded from
version control. Never commit them:

```python
import os

email = os.environ["SYMPHENY_EMAIL"]
password = os.environ["SYMPHENY_PASSWORD"]
```

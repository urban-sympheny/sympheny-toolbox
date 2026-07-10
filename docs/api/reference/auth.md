<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Auth

External API - auth resource

## Post Oauth Webapp { #operation-post_oauth_webapp_backoffice_auth_ext_token_post }

```
POST /backoffice/auth/ext/token
```

No authentication required.

**Request body** (`Auth0UserCredentials`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `email` | string (email) | yes |  |
| `password` | string | yes |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/backoffice/auth/ext/token" \
  -H "Content-Type: application/json" \
  -d '{
  "email": "user@example.com",
  "password": "string"
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | Successful Response | `Auth0UserAccessToken` |
| 400 | Bad Request | `AppException` |
| 401 | Unauthorized | `AppException` |
| 404 | Not Found | `AppException` |
| 409 | Conflict | `AppException` |
| 500 | Internal Server Error | `AppException` |
| 422 | Validation Error | `HTTPValidationError` |

**Example response** (200)

```json
{
  "access_token": "string",
  "token_type": "string",
  "expires_in": 0
}
```

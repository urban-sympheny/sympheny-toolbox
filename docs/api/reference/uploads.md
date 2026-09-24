<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Uploads

## S3 presigned url 1 { #operation-s3PresignedUrl_1 }

```
GET /sympheny-app/db-update/s3-presigned-url
```

Requires a [Bearer token](../authentication.md).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `deletePrevious` | query | boolean | no | Default: `false`. |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/db-update/s3-presigned-url" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoS3PresignedUrlDto` |

**Example response** (200)

```json
{
  "data": {
    "s3PresignedUrl": "string"
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

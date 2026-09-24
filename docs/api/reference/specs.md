<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Specs

## Finish specs and submit for exec v2 list { #operation-finishSpecsAndSubmitForExecV2List }

```
PUT /sympheny-app/v2/specs
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.scenarios.prepare_specs_input_files()`](../../sdk/reference/scenarios.md#method-scenarios-prepare_specs_input_files).

This triggers the specs file generation asynchronously. Then poll GET /scenario/{scenarioGuid}/specs-input-file-url until returned presignedUrl is not null

**Request body** (`ScenarioGuidListDto`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `scenarioGuids` | array of string | yes |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/v2/specs" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "scenarioGuids": [
    "string"
  ]
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoStatus` |

**Example response** (200)

```json
{
  "data": {
    "code": "string",
    "desc": "string",
    "message": "string"
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

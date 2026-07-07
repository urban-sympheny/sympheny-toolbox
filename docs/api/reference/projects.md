<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Projects

## View my projects { #operation-viewMyProjects }

```
GET /sympheny-app/projects
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.projects.list()`](../../sdk/reference/projects.md#method-projects-list).

Here you must use version=V2. Also name must be unique

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/projects" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoProjectSummaryResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "projects": [
      {
        "projectName": "string",
        "projectGuid": "string",
        "created": "2026-01-01T00:00:00Z",
        "updated": "2026-01-01T00:00:00Z",
        "coverImage": "string",
        "projectOwnerEmail": "string",
        "secondaryOwners": [
          {
            "email": "string",
            "canEdit": true,
            "favorite": true
          }
        ],
        "lockUserEmail": "string",
        "lock": true,
        "lockTime": "2026-01-01T00:00:00Z",
        "ownedByCurrentUser": true,
        "editableByCurrentUser": true,
        "originalDefaultProjectGuid": "string",
        "version": "V1",
        "favorite": true,
        "gisCentroidX": 0.0,
        "gisCentroidY": 0.0,
        "zoomExtentXmin": 0.0,
        "zoomExtentYmin": 0.0,
        "zoomExtentXmax": 0.0,
        "zoomExtentYmax": 0.0,
        "processing": true
      }
    ]
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Create new project { #operation-createNewProject }

```
POST /sympheny-app/projects
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.projects.create()`](../../sdk/reference/projects.md#method-projects-create).

Here you must use version=V2. Also name must be unique

**Request body** (`ProjectRequestDto`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `projectName` | string | yes |  |
| `version` | string | yes | One of: `V1`, `V2`. |
| `webhookUrl` | string, nullable | no |  |
| `favorite` | boolean, nullable | no |  |
| `gisCentroidX` | number, nullable | no |  |
| `gisCentroidY` | number, nullable | no |  |
| `zoomExtentXmin` | number, nullable | no |  |
| `zoomExtentYmin` | number, nullable | no |  |
| `zoomExtentXmax` | number, nullable | no |  |
| `zoomExtentYmax` | number, nullable | no |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/projects" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "projectName": "string",
  "version": "V1",
  "webhookUrl": "string",
  "favorite": true,
  "gisCentroidX": 0.0,
  "gisCentroidY": 0.0,
  "zoomExtentXmin": 0.0,
  "zoomExtentYmin": 0.0,
  "zoomExtentXmax": 0.0,
  "zoomExtentYmax": 0.0
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | `ResponseDtoProjectResponseDto` |

**Example response** (201)

```json
{
  "data": {
    "projectName": "string",
    "projectGuid": "string",
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "coverImage": "string",
    "projectOwnerEmail": "string",
    "secondaryOwners": [
      {
        "email": "string",
        "canEdit": true,
        "favorite": true
      }
    ],
    "lockUserEmail": "string",
    "lock": true,
    "lockTime": "2026-01-01T00:00:00Z",
    "ownedByCurrentUser": true,
    "editableByCurrentUser": true,
    "originalDefaultProjectGuid": "string",
    "version": "V1",
    "favorite": true,
    "gisCentroidX": 0.0,
    "gisCentroidY": 0.0,
    "zoomExtentXmin": 0.0,
    "zoomExtentYmin": 0.0,
    "zoomExtentXmax": 0.0,
    "zoomExtentYmax": 0.0,
    "processing": true
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## View project details { #operation-viewProjectDetails }

```
GET /sympheny-app/projects/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.projects.get()`](../../sdk/reference/projects.md#method-projects-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |
| `includeAnalyses` | query | boolean | no | Default: `true`. |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/projects/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoProjectDetailResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "images": [
      {
        "url": "string",
        "guid": "string",
        "cover": true
      }
    ],
    "projectName": "string",
    "projectGuid": "string",
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "projectOwner": "string",
    "projectOwnerEmail": "string",
    "secondaryOwners": [
      {
        "email": "string",
        "canEdit": true,
        "favorite": true
      }
    ],
    "lockUserEmail": "string",
    "lock": true,
    "lockTime": "2026-01-01T00:00:00Z",
    "ownedByCurrentUser": true,
    "editableByCurrentUser": true,
    "ownerHistory": [
      {
        "ownedAt": "2026-01-01T00:00:00Z",
        "ownerEmail": "string"
      }
    ],
    "analyses": [
      {
        "analysisGuid": "string",
        "analysisName": "string",
        "created": "2026-01-01T00:00:00Z",
        "updated": "2026-01-01T00:00:00Z",
        "scenarios": [
          {
            "scenarioGuid": "string",
            "scenarioName": "string",
            "updated": "2026-01-01T00:00:00Z",
            "readyForExecution": true,
            "preparingExecutionV2": true,
            "masterScenarioGuid": "string",
            "projectGuid": "string",
            "projectName": "string",
            "analysisGuid": "string",
            "analysisName": "string",
            "enymap": {
              "length": null,
              "interestRate": null,
              "exchangeCurrency": null,
              "exchangeRate": null,
              "scope": null,
              "technologies": null,
              "demands": null,
              "imports": null,
              "exports": null,
              "multiHubs": null
            },
            "variant": true
          }
        ]
      }
    ],
    "coverImage": "string",
    "originalDefaultProjectGuid": "string",
    "version": "V1",
    "webhookUrl": "string",
    "favorite": true,
    "gisCentroidX": 0.0,
    "gisCentroidY": 0.0,
    "zoomExtentXmin": 0.0,
    "zoomExtentYmin": 0.0,
    "zoomExtentXmax": 0.0,
    "zoomExtentYmax": 0.0
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Delete project { #operation-deleteProject }

```
DELETE /sympheny-app/projects/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.projects.delete()`](../../sdk/reference/projects.md#method-projects-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/projects/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoProjectSummaryResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "projects": [
      {
        "projectName": "string",
        "projectGuid": "string",
        "created": "2026-01-01T00:00:00Z",
        "updated": "2026-01-01T00:00:00Z",
        "coverImage": "string",
        "projectOwnerEmail": "string",
        "secondaryOwners": [
          {
            "email": "string",
            "canEdit": true,
            "favorite": true
          }
        ],
        "lockUserEmail": "string",
        "lock": true,
        "lockTime": "2026-01-01T00:00:00Z",
        "ownedByCurrentUser": true,
        "editableByCurrentUser": true,
        "originalDefaultProjectGuid": "string",
        "version": "V1",
        "favorite": true,
        "gisCentroidX": 0.0,
        "gisCentroidY": 0.0,
        "zoomExtentXmin": 0.0,
        "zoomExtentYmin": 0.0,
        "zoomExtentXmax": 0.0,
        "zoomExtentYmax": 0.0,
        "processing": true
      }
    ]
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

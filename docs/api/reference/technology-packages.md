<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Technology packages

## Delete technology package { #operation-deleteTechnologyPackage }

```
DELETE /sympheny-app/scenarios/{scenarioGuid}/technology-packages/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.technology_packages.delete()`](../../sdk/reference/technology_packages.md#method-technology_packages-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |
| `guid` | path | string | yes |  |
| `deleteTechs` | query | boolean | no | Default: `false`. |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/{scenarioGuid}/technology-packages/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoTechnologyPackageListResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "technologyPackages": [
      {
        "name": "string",
        "guid": "string",
        "conversionTechnologies": [
          "string"
        ],
        "storageTechnologies": [
          "string"
        ],
        "dbOrganization": "string"
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

## Get all technology packages by scenario v2 { #operation-getAllTechnologyPackagesByScenarioV2 }

```
GET /sympheny-app/v2/scenarios/{scenarioGuid}/technology-packages
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.technology_packages.list()`](../../sdk/reference/technology_packages.md#method-technology_packages-list).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/{scenarioGuid}/technology-packages" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoTechnologyPackageListResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "technologyPackages": [
      {
        "maximumConversions": 0,
        "maximumStorages": 0,
        "mustBeInstalled": "canBeInstalled",
        "mutuallyExclusiveGroup": "string",
        "name": "string",
        "guid": "string",
        "conversionTechnologies": [
          {
            "guid": "string",
            "name": "string"
          }
        ],
        "storageTechnologies": [
          {
            "guid": "string",
            "name": "string"
          }
        ]
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

## Get technology package by guid v2 { #operation-getTechnologyPackageByGuidV2 }

```
GET /sympheny-app/v2/scenarios/{scenarioGuid}/technology-packages/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.technology_packages.get()`](../../sdk/reference/technology_packages.md#method-technology_packages-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/{scenarioGuid}/technology-packages/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoTechnologyPackageResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "maximumConversions": 0,
    "maximumStorages": 0,
    "mustBeInstalled": "canBeInstalled",
    "mutuallyExclusiveGroup": "string",
    "name": "string",
    "guid": "string",
    "conversionTechnologies": [
      {
        "guid": "string",
        "name": "string"
      }
    ],
    "storageTechnologies": [
      {
        "guid": "string",
        "name": "string"
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

## Specify technology package v2 1 { #operation-specifyTechnologyPackageV2_1 }

```
POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/technology-packages
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.technology_packages.create()`](../../sdk/reference/technology_packages.md#method-technology_packages-create).

conversionTechnologies or storageTechnologies must not be empty

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Request body** (`TechnologyPackageRequestDtoV2`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `maximumConversions` | integer (int32), nullable | no |  |
| `maximumStorages` | integer (int32), nullable | no |  |
| `mustBeInstalled` | string, nullable | no | One of: `canBeInstalled`, `mustBeInstalled`, `mustBeInstalledInAtLeastOneHub`, `None`. |
| `mutuallyExclusiveGroup` | string, nullable | no |  |
| `name` | string | yes |  |
| `conversionTechnologies` | array of string, nullable | no |  |
| `storageTechnologies` | array of string, nullable | no |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/v2_1/scenarios/{scenarioGuid}/technology-packages" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "maximumConversions": 0,
  "maximumStorages": 0,
  "mustBeInstalled": "canBeInstalled",
  "mutuallyExclusiveGroup": "string",
  "name": "string",
  "conversionTechnologies": [
    "string"
  ],
  "storageTechnologies": [
    "string"
  ]
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | `ResponseDtoTechnologyPackageResponseDtoV2` |

**Example response** (201)

```json
{
  "data": {
    "maximumConversions": 0,
    "maximumStorages": 0,
    "mustBeInstalled": "canBeInstalled",
    "mutuallyExclusiveGroup": "string",
    "name": "string",
    "guid": "string",
    "conversionTechnologies": [
      {
        "guid": "string",
        "name": "string"
      }
    ],
    "storageTechnologies": [
      {
        "guid": "string",
        "name": "string"
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

## Update technology package v2 1 { #operation-updateTechnologyPackageV2_1 }

```
PUT /sympheny-app/v2_1/scenarios/{scenarioGuid}/technology-packages/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.technology_packages.update()`](../../sdk/reference/technology_packages.md#method-technology_packages-update).

conversionTechnologies or storageTechnologies must not be empty

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |
| `guid` | path | string | yes |  |

**Request body** (`TechnologyPackageRequestDtoPUT`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `maximumConversions` | integer (int32), nullable | no |  |
| `maximumStorages` | integer (int32), nullable | no |  |
| `mustBeInstalled` | string, nullable | no | One of: `canBeInstalled`, `mustBeInstalled`, `mustBeInstalledInAtLeastOneHub`, `None`. |
| `mutuallyExclusiveGroup` | string, nullable | no |  |
| `name` | string | yes |  |
| `conversionTechnologies` | array of `GuidDtoPUT`, nullable | no |  |
| `storageTechnologies` | array of `GuidDtoPUT`, nullable | no |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/v2_1/scenarios/{scenarioGuid}/technology-packages/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "maximumConversions": 0,
  "maximumStorages": 0,
  "mustBeInstalled": "canBeInstalled",
  "mutuallyExclusiveGroup": "string",
  "name": "string",
  "conversionTechnologies": [
    {
      "guid": "string"
    }
  ],
  "storageTechnologies": [
    {
      "guid": "string"
    }
  ]
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | `ResponseDtoTechnologyPackageResponseDtoV2` |

**Example response** (201)

```json
{
  "data": {
    "maximumConversions": 0,
    "maximumStorages": 0,
    "mustBeInstalled": "canBeInstalled",
    "mutuallyExclusiveGroup": "string",
    "name": "string",
    "guid": "string",
    "conversionTechnologies": [
      {
        "guid": "string",
        "name": "string"
      }
    ],
    "storageTechnologies": [
      {
        "guid": "string",
        "name": "string"
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

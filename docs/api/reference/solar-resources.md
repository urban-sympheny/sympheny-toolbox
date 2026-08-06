<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Solar resources

## Delete solar on site resource { #operation-deleteSolarOnSiteResource }

```
DELETE /sympheny-app/scenarios/solar-on-site-resource/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.solar_resources.delete()`](../../sdk/reference/solar_resources.md#method-solar_resources-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/solar-on-site-resource/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoSolarOnSiteResourceListResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "solarResources": [
      {
        "solarResourceGuid": "string",
        "energyCarrierGuid": "string",
        "energyCarrierName": "string",
        "hubs": [
          {
            "hubName": "string",
            "hubGuid": "string",
            "availableSolarCollectorArea": 0.0,
            "availableResourceType": "string",
            "technologyDimensioningStdValue": 0.0
          }
        ],
        "created": "2026-01-01T00:00:00Z",
        "updated": "2026-01-01T00:00:00Z",
        "irradianceProfileType": "GENERATED",
        "solarResourceMetadataName": "string",
        "solarResourceMetadataDbOrganization": "string",
        "solarResourceMetadataGuid": "string",
        "solarResourceMetadataLocation": "string",
        "solarResourceMetadataType": "string",
        "solarResourceMetadataSlope": 0.0,
        "solarResourceMetadataOrientation": "string"
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

## Get solar on site resources v2 { #operation-getSolarOnSiteResourcesV2 }

```
GET /sympheny-app/v2/scenarios/solar-on-site-resource/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.solar_resources.get()`](../../sdk/reference/solar_resources.md#method-solar_resources-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/solar-on-site-resource/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoSolarOnSiteResourceResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "name": "string",
    "solarResourceGuid": "string",
    "energyCarrierGuid": "string",
    "energyCarrierName": "string",
    "hubs": [
      {
        "hubName": "string",
        "hubGuid": "string",
        "availableSolarCollectorArea": 0.0,
        "availableResourceType": "Area"
      }
    ],
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "irradianceProfileType": "GENERATED",
    "solarResourceMetadataName": "string",
    "solarResourceMetadataDbOrganization": "string",
    "solarResourceMetadataGuid": "string",
    "solarResourceMetadataLocation": "string",
    "solarResourceMetadataType": "string",
    "solarResourceMetadataSlope": 0.0,
    "solarResourceMetadataOrientation": "string",
    "stages": [
      "00000000-0000-0000-0000-000000000000"
    ],
    "profileId": 0
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Get all solar on site resources by scenario v2 { #operation-getAllSolarOnSiteResourcesByScenarioV2 }

```
GET /sympheny-app/v2/scenarios/{scenarioGuid}/solar-on-site-resource
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.solar_resources.list()`](../../sdk/reference/solar_resources.md#method-solar_resources-list).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/{scenarioGuid}/solar-on-site-resource" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoListSolarOnSiteResourceResponseDtoV2` |

**Example response** (200)

```json
{
  "data": [
    {
      "name": "string",
      "solarResourceGuid": "string",
      "energyCarrierGuid": "string",
      "energyCarrierName": "string",
      "hubs": [
        {
          "hubName": "string",
          "hubGuid": "string",
          "availableSolarCollectorArea": 0.0,
          "availableResourceType": "Area"
        }
      ],
      "created": "2026-01-01T00:00:00Z",
      "updated": "2026-01-01T00:00:00Z",
      "irradianceProfileType": "GENERATED",
      "solarResourceMetadataName": "string",
      "solarResourceMetadataDbOrganization": "string",
      "solarResourceMetadataGuid": "string",
      "solarResourceMetadataLocation": "string",
      "solarResourceMetadataType": "string",
      "solarResourceMetadataSlope": 0.0,
      "solarResourceMetadataOrientation": "string",
      "stages": [
        "00000000-0000-0000-0000-000000000000"
      ],
      "profileId": 0
    }
  ],
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Upload new solar on site resource v2 1 { #operation-uploadNewSolarOnSiteResourceV2_1 }

```
POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/solar-on-site-resource
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.solar_resources.create()`](../../sdk/reference/solar_resources.md#method-solar_resources-create).

energyCarrierGuid must be a carrier with subType in: SOLAR_ROOF,BIOMASS,GEOTHERMAL,HYDRO,PROCESS_WASTE_HEAT,SOLAR_FACADE,SOLAR_PARAPET,TIDAL,WIND

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Request body** (`SolarOnSiteResourceRequestDtoV2`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | yes |  |
| `energyCarrierGuid` | string | yes |  |
| `hubs` | array of `SolarOnSiteResourcesHubRequestDtoV2` | yes |  |
| `profileId` | integer (int64) | yes |  |
| `stages` | array of string (uuid) | yes |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/v2_1/scenarios/{scenarioGuid}/solar-on-site-resource" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "energyCarrierGuid": "string",
  "hubs": [
    {
      "hubGuid": "string",
      "availableSolarCollectorArea": 0.0,
      "availableResourceType": "Area"
    }
  ],
  "profileId": 0,
  "stages": [
    "00000000-0000-0000-0000-000000000000"
  ]
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | `ResponseDtoSolarOnSiteResourceResponseDtoV2` |

**Example response** (201)

```json
{
  "data": {
    "name": "string",
    "solarResourceGuid": "string",
    "energyCarrierGuid": "string",
    "energyCarrierName": "string",
    "hubs": [
      {
        "hubName": "string",
        "hubGuid": "string",
        "availableSolarCollectorArea": 0.0,
        "availableResourceType": "Area"
      }
    ],
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "irradianceProfileType": "GENERATED",
    "solarResourceMetadataName": "string",
    "solarResourceMetadataDbOrganization": "string",
    "solarResourceMetadataGuid": "string",
    "solarResourceMetadataLocation": "string",
    "solarResourceMetadataType": "string",
    "solarResourceMetadataSlope": 0.0,
    "solarResourceMetadataOrientation": "string",
    "stages": [
      "00000000-0000-0000-0000-000000000000"
    ],
    "profileId": 0
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Edit solar on site resource v2 2 { #operation-editSolarOnSiteResourceV2_2 }

```
PUT /sympheny-app/v2_2/scenarios/solar-on-site-resource/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.solar_resources.update()`](../../sdk/reference/solar_resources.md#method-solar_resources-update).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Request body** (`SolarOnSiteResourceRequestDtoPUT`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | yes |  |
| `energyCarrierGuid` | string | yes |  |
| `energyCarrierName` | string | yes |  |
| `hubs` | array of `HubSolarOnSiteResourceRequestDtoPUT` | yes |  |
| `irradianceProfileType` | string | yes | One of: `GENERATED`, `UPLOADED`, `SAVED`. |
| `solarResourceMetadataName` | string, nullable | no |  |
| `solarResourceMetadataDbOrganization` | string, nullable | no |  |
| `solarResourceMetadataGuid` | string, nullable | no |  |
| `solarResourceMetadataLocation` | string, nullable | no |  |
| `solarResourceMetadataType` | string, nullable | no |  |
| `solarResourceMetadataSlope` | number, nullable | no |  |
| `solarResourceMetadataOrientation` | string, nullable | no |  |
| `stages` | array of string (uuid) | yes |  |
| `profileId` | integer (int64) | yes |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/v2_2/scenarios/solar-on-site-resource/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "energyCarrierGuid": "string",
  "energyCarrierName": "string",
  "hubs": [
    {
      "hubGuid": "string",
      "availableSolarCollectorArea": 0.0,
      "availableResourceType": "Area"
    }
  ],
  "irradianceProfileType": "GENERATED",
  "solarResourceMetadataName": "string",
  "solarResourceMetadataDbOrganization": "string",
  "solarResourceMetadataGuid": "string",
  "solarResourceMetadataLocation": "string",
  "solarResourceMetadataType": "string",
  "solarResourceMetadataSlope": 0.0,
  "solarResourceMetadataOrientation": "string",
  "stages": [
    "00000000-0000-0000-0000-000000000000"
  ],
  "profileId": 0
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoSolarOnSiteResourceResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "name": "string",
    "solarResourceGuid": "string",
    "energyCarrierGuid": "string",
    "energyCarrierName": "string",
    "hubs": [
      {
        "hubName": "string",
        "hubGuid": "string",
        "availableSolarCollectorArea": 0.0,
        "availableResourceType": "Area"
      }
    ],
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "irradianceProfileType": "GENERATED",
    "solarResourceMetadataName": "string",
    "solarResourceMetadataDbOrganization": "string",
    "solarResourceMetadataGuid": "string",
    "solarResourceMetadataLocation": "string",
    "solarResourceMetadataType": "string",
    "solarResourceMetadataSlope": 0.0,
    "solarResourceMetadataOrientation": "string",
    "stages": [
      "00000000-0000-0000-0000-000000000000"
    ],
    "profileId": 0
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

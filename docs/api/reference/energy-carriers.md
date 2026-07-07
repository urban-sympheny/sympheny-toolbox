<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Energy carriers

## Get energy carrier by guid { #operation-getEnergyCarrierByGuid }

```
GET /sympheny-app/carriers/{carrierGuid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.energy_carriers.get()`](../../sdk/reference/energy_carriers.md#method-energy_carriers-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `carrierGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/carriers/{carrierGuid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoEnergyCarrierResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "energyCarrierGuid": "string",
    "typeKey": "string",
    "typeDisplayName": "string",
    "subtypeKey": "string",
    "subtypeDisplayName": "string",
    "energyCarrierName": "string",
    "colorHexCode": "string",
    "fixedInputShare": 0.0,
    "outputEfficiency": 0.0,
    "customOutputEfficiencyActivated": true,
    "customInputEfficiencyActivated": true,
    "customSeasonalityValues": [
      {
        "month": "JANUARY",
        "value": 0.0
      }
    ],
    "outputEfficiencyProfileId": 0,
    "created": "2026-01-01T00:00:00Z",
    "primary": true
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Delete energy carrier { #operation-deleteEnergyCarrier }

```
DELETE /sympheny-app/scenarios/carriers/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.energy_carriers.delete()`](../../sdk/reference/energy_carriers.md#method-energy_carriers-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/carriers/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoEnergyCarriersListResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "energyCarriers": [
      {
        "energyCarrierGuid": "string",
        "typeKey": "string",
        "typeDisplayName": "string",
        "subtypeKey": "string",
        "subtypeDisplayName": "string",
        "energyCarrierName": "string",
        "colorHexCode": "string",
        "fixedInputShare": 0.0,
        "outputEfficiency": 0.0,
        "customOutputEfficiencyActivated": true,
        "customInputEfficiencyActivated": true,
        "customSeasonalityValues": [
          {
            "month": "JANUARY",
            "value": 0.0
          }
        ],
        "outputEfficiencyProfileId": 0,
        "created": "2026-01-01T00:00:00Z",
        "primary": true
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

## Find all energy carriers by scenario { #operation-findAllEnergyCarriersByScenario }

```
GET /sympheny-app/scenarios/{scenarioGuid}/carriers
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.energy_carriers.list()`](../../sdk/reference/energy_carriers.md#method-energy_carriers-list).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/{scenarioGuid}/carriers" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoEnergyCarriersListResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "energyCarriers": [
      {
        "energyCarrierGuid": "string",
        "typeKey": "string",
        "typeDisplayName": "string",
        "subtypeKey": "string",
        "subtypeDisplayName": "string",
        "energyCarrierName": "string",
        "colorHexCode": "string",
        "fixedInputShare": 0.0,
        "outputEfficiency": 0.0,
        "customOutputEfficiencyActivated": true,
        "customInputEfficiencyActivated": true,
        "customSeasonalityValues": [
          {
            "month": "JANUARY",
            "value": 0.0
          }
        ],
        "outputEfficiencyProfileId": 0,
        "created": "2026-01-01T00:00:00Z",
        "primary": true
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

## Edit energy carrier v2 { #operation-editEnergyCarrierV2 }

```
PUT /sympheny-app/v2/carriers/{carrierGuid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.energy_carriers.update()`](../../sdk/reference/energy_carriers.md#method-energy_carriers-update).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `carrierGuid` | path | string | yes |  |

**Request body** (`EnergyCarrierResponseDto`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `energyCarrierGuid` | string | yes |  |
| `typeKey` | string | yes |  |
| `typeDisplayName` | string | yes |  |
| `subtypeKey` | string | yes |  |
| `subtypeDisplayName` | string | yes |  |
| `energyCarrierName` | string | yes |  |
| `colorHexCode` | string | yes |  |
| `fixedInputShare` | number, nullable | no |  |
| `outputEfficiency` | number, nullable | no |  |
| `customOutputEfficiencyActivated` | boolean | yes |  |
| `customInputEfficiencyActivated` | boolean | yes |  |
| `customSeasonalityValues` | array of `CustomSeasonalityResponseDto`, nullable | no |  |
| `outputEfficiencyProfileId` | integer (int64), nullable | no |  |
| `created` | string (date-time) | yes |  |
| `primary` | boolean, nullable | no |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/v2/carriers/{carrierGuid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "energyCarrierGuid": "string",
  "typeKey": "string",
  "typeDisplayName": "string",
  "subtypeKey": "string",
  "subtypeDisplayName": "string",
  "energyCarrierName": "string",
  "colorHexCode": "string",
  "fixedInputShare": 0.0,
  "outputEfficiency": 0.0,
  "customOutputEfficiencyActivated": true,
  "customInputEfficiencyActivated": true,
  "customSeasonalityValues": [
    {
      "month": "JANUARY",
      "value": 0.0
    }
  ],
  "outputEfficiencyProfileId": 0,
  "created": "2026-01-01T00:00:00Z",
  "primary": true
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoEnergyCarrierResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "energyCarrierGuid": "string",
    "typeKey": "string",
    "typeDisplayName": "string",
    "subtypeKey": "string",
    "subtypeDisplayName": "string",
    "energyCarrierName": "string",
    "colorHexCode": "string",
    "fixedInputShare": 0.0,
    "outputEfficiency": 0.0,
    "customOutputEfficiencyActivated": true,
    "customInputEfficiencyActivated": true,
    "customSeasonalityValues": [
      {
        "month": "JANUARY",
        "value": 0.0
      }
    ],
    "outputEfficiencyProfileId": 0,
    "created": "2026-01-01T00:00:00Z",
    "primary": true
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Create new energy carrier v2 { #operation-createNewEnergyCarrierV2 }

```
POST /sympheny-app/v2/scenarios/{scenarioGuid}/carriers
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.energy_carriers.create()`](../../sdk/reference/energy_carriers.md#method-energy_carriers-create).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Request body** (`EnergyCarrierRequestDtoV2`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `subType` | string | yes | One of: `ELECTRICITY`, `ELECTRICITY_RENEWABLE`, `WOOD_CHIPS`, `WOOD_PELLETS`, `COAL`, `OIL`, `GAS`, `BIOGAS`, `HYDROGEN`, `HYDROGEN_PRESSURIZED`, `COOLING_1`, `COOLING_2`, `COOLING_3`, `COOLING_4`, `ICE`, `HEAT_1`, `HEAT_2`, `HEAT_3`, `HEAT_4`, `HEAT_5`, `HEAT_6`, `HEAT_7`, `HEAT_8`, `HEAT_9`, `HEAT_AMBIENT`, `STEAM_LOW_PRESSURE`, `SOLAR_ROOF`, `SOLAR_FACADE`, `SOLAR_PARAPET`, `WIND`, `HYDRO`, `BIOMASS`, `GEOTHERMAL`, `TIDAL`, `PROCESS_WASTE_HEAT`, `CUSTOM`. |
| `energyCarrierName` | string | yes |  |
| `colorHexCode` | string, nullable | no |  |
| `allowVirtualLoad` | boolean, nullable | no |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/{scenarioGuid}/carriers" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "subType": "ELECTRICITY",
  "energyCarrierName": "string",
  "colorHexCode": "string",
  "allowVirtualLoad": true
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | `ResponseDtoEnergyCarrierResponseDto` |

**Example response** (201)

```json
{
  "data": {
    "energyCarrierGuid": "string",
    "typeKey": "string",
    "typeDisplayName": "string",
    "subtypeKey": "string",
    "subtypeDisplayName": "string",
    "energyCarrierName": "string",
    "colorHexCode": "string",
    "fixedInputShare": 0.0,
    "outputEfficiency": 0.0,
    "customOutputEfficiencyActivated": true,
    "customInputEfficiencyActivated": true,
    "customSeasonalityValues": [
      {
        "month": "JANUARY",
        "value": 0.0
      }
    ],
    "outputEfficiencyProfileId": 0,
    "created": "2026-01-01T00:00:00Z",
    "primary": true
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

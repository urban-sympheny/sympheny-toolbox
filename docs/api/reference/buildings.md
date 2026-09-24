<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Buildings

## Post Buildings { #operation-post_buildings_api_services_gis_buildings_post }

```
POST /api-services/gis/buildings
```

Requires a [Bearer token](../authentication.md).

**Request body** (`BuildingsRequest`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `aoi` | `Geometry` | yes | A class representing a geojson geometry. |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/api-services/gis/buildings" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "aoi": {
    "type": "Point",
    "coordinates": [
      null
    ]
  }
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | Successful Response | `BuildingFeatureCollection` |
| 401 | Error: Not authenticated | n/a |
| 404 | Error: Not found | n/a |
| 422 | Validation Error | `HTTPValidationError` |

**Example response** (200)

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          null
        ]
      },
      "properties": {
        "source": "string",
        "area_m2": 0,
        "floors": 0,
        "height_m": 0.0,
        "building_type": "RESIDENCE_MFH",
        "construction_year": 0,
        "addresses": [
          {
            "street": "string",
            "house_number": "string",
            "postcode": "string",
            "locality": "string",
            "country": "string",
            "formatted": "string",
            "source": "string"
          }
        ]
      }
    }
  ],
  "properties": {}
}
```

<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/buildings.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Buildings

Building lookups. Available on the client as `client.buildings`.

## buildings.in_area { #method-buildings-in_area }

```python
async def in_area(aoi: Geometry) -> BuildingFeatureCollection
```

Find the buildings within an area, as GeoJSON features.

REST operation: [`POST /api-services/gis/buildings`](../../api/reference/buildings.md#operation-post_buildings_api_services_gis_buildings_post)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `aoi` | [`Geometry`](models/gis.md#model-Geometry) | yes | Area of interest. |

**Returns:** [`BuildingFeatureCollection`](models/gis.md#model-BuildingFeatureCollection)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        buildings = await client.buildings.in_area(aoi)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        buildings = client.buildings.in_area(aoi)
    ```

<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/unofficial.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Unofficial endpoints

Endpoints outside the official documented Sympheny API. May change without notice. Available on the client as `client.unofficial`.

!!! warning
    Every method on this page calls an endpoint that is **not part of the official
    documented Sympheny API**. These endpoints may change or disappear without notice,
    and they return raw JSON payloads (`dict`/`list`) instead of typed models. Prefer an
    official, typed equivalent whenever one exists.

## unofficial.get_analysis { #method-unofficial-get_analysis }

```python
async def get_analysis(analysis_guid: str) -> dict[str, Any]
```

UNOFFICIAL — Get analysis details incl. scenarios and results.

REST operation: `GET /sympheny-app/analysis/{guid}` (not part of the official spec)

Prefer `client.analyses.get` unless you need the `results` payload (scenarios / input-file paths), which the official endpoint does not return.

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `analysis_guid` | `str` | yes | GUID of the analysis. |

**Returns:** `dict[str, Any]`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        analysis = await client.unofficial.get_analysis(analysis_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        analysis = client.unofficial.get_analysis(analysis_guid)
    ```

## unofficial.create_master_scenario { #method-unofficial-create_master_scenario }

```python
async def create_master_scenario(payload: dict[str, Any]) -> dict[str, Any]
```

UNOFFICIAL — Create a master scenario.

REST operation: `POST /sympheny-app/master-scenario/` (not part of the official spec)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `payload` | `dict[str, Any]` | yes | Raw JSON payload. |

**Returns:** `dict[str, Any]`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        result = await client.unofficial.create_master_scenario(payload)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        result = client.unofficial.create_master_scenario(payload)
    ```

## unofficial.list_variants { #method-unofficial-list_variants }

```python
async def list_variants(master_scenario_guid: str) -> list[dict[str, Any]]
```

UNOFFICIAL — List scenario variants of a master scenario.

REST operation: `GET /sympheny-app/master-scenario/{guid}/scenario-variants` (not part of the official spec)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `master_scenario_guid` | `str` | yes | GUID of the master scenario. |

**Returns:** list of `dict[str, Any]`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        variants = await client.unofficial.list_variants(master_scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        variants = client.unofficial.list_variants(master_scenario_guid)
    ```

## unofficial.delete_all_variants { #method-unofficial-delete_all_variants }

```python
async def delete_all_variants(master_scenario_guid: str) -> None
```

UNOFFICIAL — Delete all scenario variants of a master scenario.

REST operation: `DELETE /sympheny-app/master-scenario/{guid}/scenario-variants` (not part of the official spec)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `master_scenario_guid` | `str` | yes | GUID of the master scenario. |

**Returns:** `None`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        await client.unofficial.delete_all_variants(master_scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        client.unofficial.delete_all_variants(master_scenario_guid)
    ```

## unofficial.get_variants_excel_url { #method-unofficial-get_variants_excel_url }

```python
async def get_variants_excel_url(master_scenario_guid: str) -> str
```

UNOFFICIAL — Get a presigned URL to the variants Excel export.

REST operation: `GET /sympheny-app/master-scenario/{guid}/scenario-variants-excel` (not part of the official spec)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `master_scenario_guid` | `str` | yes | GUID of the master scenario. |

**Returns:** `str`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        url = await client.unofficial.get_variants_excel_url(master_scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        url = client.unofficial.get_variants_excel_url(master_scenario_guid)
    ```

## unofficial.create_variants_from_excel_url { #method-unofficial-create_variants_from_excel_url }

```python
async def create_variants_from_excel_url(
    presigned_url: str,
    master_scenario_guid: str,
    *,
    delete_existing: bool = True,
) -> Any
```

UNOFFICIAL — Create scenario variants from an uploaded Excel file.

REST operation: `PUT /sympheny-app/scenario-variants-excel` (not part of the official spec)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `presigned_url` | `str` | yes | Presigned S3 URL the Excel file was uploaded to. |
| `master_scenario_guid` | `str` | yes | GUID of the master scenario. |
| `delete_existing` | `bool` | no | Delete the existing scenario variants first. Defaults to `True`. |

**Returns:** `Any`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        result = await client.unofficial.create_variants_from_excel_url(presigned_url, master_scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        result = client.unofficial.create_variants_from_excel_url(presigned_url, master_scenario_guid)
    ```

## unofficial.get_upload_url { #method-unofficial-get_upload_url }

```python
async def get_upload_url() -> str
```

UNOFFICIAL — Get a presigned S3 URL for file uploads.

REST operation: `GET /sympheny-app/db-update/s3-presigned-url` (not part of the official spec)

**Returns:** `str`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        url = await client.unofficial.get_upload_url()
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        url = client.unofficial.get_upload_url()
    ```

## unofficial.upload_to_presigned_url { #method-unofficial-upload_to_presigned_url }

```python
async def upload_to_presigned_url(presigned_url: str, content: bytes) -> None
```

UNOFFICIAL — Upload raw bytes to a presigned S3 URL (no Sympheny auth).

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `presigned_url` | `str` | yes | Presigned S3 URL from `get_upload_url`. |
| `content` | `bytes` | yes | Raw file bytes to upload. |

**Returns:** `None`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        await client.unofficial.upload_to_presigned_url(presigned_url, content)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        client.unofficial.upload_to_presigned_url(presigned_url, content)
    ```

## unofficial.create_scenario_from_excel_url { #method-unofficial-create_scenario_from_excel_url }

```python
async def create_scenario_from_excel_url(
    presigned_url: str,
    scenario_name: str,
    analysis_guid: str,
) -> str
```

UNOFFICIAL — Create a scenario from an uploaded Excel file; returns the scenario GUID.

REST operation: `POST /sympheny-app/v2/analysis/{guid}/scenario/excel` (not part of the official spec)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `presigned_url` | `str` | yes | Presigned S3 URL the Excel file was uploaded to. |
| `scenario_name` | `str` | yes | Name for the new scenario. |
| `analysis_guid` | `str` | yes | GUID of the analysis. |

**Returns:** `str`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        scenario_guid = await client.unofficial.create_scenario_from_excel_url(presigned_url, scenario_name, analysis_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        scenario_guid = client.unofficial.create_scenario_from_excel_url(presigned_url, scenario_name, analysis_guid)
    ```

## unofficial.close_diagram { #method-unofficial-close_diagram }

```python
async def close_diagram(scenario_guid: str) -> None
```

UNOFFICIAL — Close the hub diagram of a scenario.

REST operation: `PUT /sympheny-app/scenarios/{guid}/close-diagram` (not part of the official spec)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** `None`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        await client.unofficial.close_diagram(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        client.unofficial.close_diagram(scenario_guid)
    ```

## unofficial.generate_specs { #method-unofficial-generate_specs }

```python
async def generate_specs(scenario_guids: list[str]) -> None
```

UNOFFICIAL — Trigger input-file (specs) generation for scenarios.

REST operation: `PUT /sympheny-app/v2/specs` (not part of the official spec)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guids` | list of `str` | yes | GUIDs of the scenarios to generate input files for. |

**Returns:** `None`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        await client.unofficial.generate_specs(scenario_guids)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        client.unofficial.generate_specs(scenario_guids)
    ```

## unofficial.generate_scenario_specs { #method-unofficial-generate_scenario_specs }

```python
async def generate_scenario_specs(scenario_guid: str) -> None
```

UNOFFICIAL — Trigger specs generation for a single scenario.

REST operation: `PUT /sympheny-app/v2/scenarios/{guid}/specs` (not part of the official spec)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** `None`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        await client.unofficial.generate_scenario_specs(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        client.unofficial.generate_scenario_specs(scenario_guid)
    ```

## unofficial.create_scenario_enymap { #method-unofficial-create_scenario_enymap }

```python
async def create_scenario_enymap(analysis_guid: str, payload: dict[str, Any]) -> dict[str, Any]
```

UNOFFICIAL — Create an enymap scenario.

REST operation: `POST /sympheny-app/analysis/{guid}/scenario-enymap` (not part of the official spec)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `analysis_guid` | `str` | yes | GUID of the analysis. |
| `payload` | `dict[str, Any]` | yes | Raw JSON payload. |

**Returns:** `dict[str, Any]`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        result = await client.unofficial.create_scenario_enymap(analysis_guid, payload)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        result = client.unofficial.create_scenario_enymap(analysis_guid, payload)
    ```

## unofficial.create_gis_hub { #method-unofficial-create_gis_hub }

```python
async def create_gis_hub(scenario_guid: str, polygon: list[Any]) -> Any
```

UNOFFICIAL — Create a GIS hub for an enymap scenario.

REST operation: `POST /sympheny-app/scenario-enymap/{guid}/create-gis-hub` (not part of the official spec)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `polygon` | list of `Any` | yes | Polygon coordinates. |

**Returns:** `Any`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        result = await client.unofficial.create_gis_hub(scenario_guid, polygon)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        result = client.unofficial.create_gis_hub(scenario_guid, polygon)
    ```

## unofficial.create_demand_solar { #method-unofficial-create_demand_solar }

```python
async def create_demand_solar(scenario_guid: str) -> Any
```

UNOFFICIAL — Create demands and solar resources for an enymap scenario.

REST operation: `POST /sympheny-app/scenario-enymap/{guid}/create-demand-solar` (not part of the official spec)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** `Any`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        result = await client.unofficial.create_demand_solar(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        result = client.unofficial.create_demand_solar(scenario_guid)
    ```

## unofficial.gis_background_jobs { #method-unofficial-gis_background_jobs }

```python
async def gis_background_jobs() -> list[dict[str, Any]]
```

UNOFFICIAL — List GIS background jobs (`api-services` backend).

REST operation: `GET /api-services/gis/background` (not part of the official spec)

**Returns:** list of `dict[str, Any]`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        jobs = await client.unofficial.gis_background_jobs()
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        jobs = client.unofficial.gis_background_jobs()
    ```

## unofficial.hub_demand { #method-unofficial-hub_demand }

```python
async def hub_demand(
    demand_type: str,
    building_type: str,
    buildings: list[dict[str, Any]],
) -> list[dict[str, Any]]
```

UNOFFICIAL — Estimate building energy demand (`api-services` backend).

REST operation: `POST /api-services/demand/hub_demand` (not part of the official spec)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `demand_type` | `str` | yes |  |
| `building_type` | `str` | yes |  |
| `buildings` | list of `dict[str, Any]` | yes |  |

**Returns:** list of `dict[str, Any]`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        demands = await client.unofficial.hub_demand(demand_type, building_type, buildings)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        demands = client.unofficial.hub_demand(demand_type, building_type, buildings)
    ```

## unofficial.get_database_demand_profile { #method-unofficial-get_database_demand_profile }

```python
async def get_database_demand_profile(demand_guid: str) -> list[dict[str, Any]]
```

UNOFFICIAL — Get the normalized profile of a database energy demand.

REST operation: `GET /sympheny-app/database-energy-demands/{guid}/profile` (not part of the official spec)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `demand_guid` | `str` | yes | GUID of the demand. |

**Returns:** list of `dict[str, Any]`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        profile = await client.unofficial.get_database_demand_profile(demand_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        profile = client.unofficial.get_database_demand_profile(demand_guid)
    ```

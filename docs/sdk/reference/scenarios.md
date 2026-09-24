<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/scenarios.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Scenarios

Operations on scenarios. Available on the client as `client.scenarios`.

## scenarios.list { #method-scenarios-list }

```python
async def list(analysis_guid: str) -> list[ScenarioResponseDto]
```

List the scenarios of an analysis.

REST operation: [`GET /sympheny-app/analysis/{guid}/scenario`](../../api/reference/scenarios.md#operation-listScenarios)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `analysis_guid` | `str` | yes | GUID of the analysis. |

**Returns:** list of [`ScenarioResponseDto`](models/common.md#model-ScenarioResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        scenarios = await client.scenarios.list(analysis_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        scenarios = client.scenarios.list(analysis_guid)
    ```

## scenarios.create { #method-scenarios-create }

```python
async def create(analysis_guid: str, request: ScenarioRequestDto) -> ScenarioResponseDto
```

Create a new scenario in an analysis.

REST operation: [`POST /sympheny-app/analysis/{guid}/scenario`](../../api/reference/scenarios.md#operation-createNewScenario)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `analysis_guid` | `str` | yes | GUID of the analysis. |
| `request` | [`ScenarioRequestDto`](models/scenarios.md#model-ScenarioRequestDto) | yes | Request body. |

**Returns:** [`ScenarioResponseDto`](models/common.md#model-ScenarioResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        scenario = await client.scenarios.create(analysis_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        scenario = client.scenarios.create(analysis_guid, request)
    ```

## scenarios.get { #method-scenarios-get }

```python
async def get(scenario_guid: str) -> ScenarioResponseDto
```

Get scenario details.

REST operation: [`GET /sympheny-app/scenario/{scenarioGuid}`](../../api/reference/scenarios.md#operation-getScenario)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** [`ScenarioResponseDto`](models/common.md#model-ScenarioResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        scenario = await client.scenarios.get(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        scenario = client.scenarios.get(scenario_guid)
    ```

## scenarios.rename { #method-scenarios-rename }

```python
async def rename(scenario_guid: str, request: ScenarioRequestDto) -> ScenarioResponseDto
```

Rename a scenario in place.

REST operation: [`PUT /sympheny-app/scenarios/{scenarioGuid}`](../../api/reference/scenarios.md#operation-renameScenario)

Unlike [`copy`](#method-scenarios-copy), this sets the scenario's name directly, so it works within the scenario's current analysis without creating a duplicate.

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `request` | [`ScenarioRequestDto`](models/scenarios.md#model-ScenarioRequestDto) | yes | Request body. |

**Returns:** [`ScenarioResponseDto`](models/common.md#model-ScenarioResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        scenario = await client.scenarios.rename(scenario_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        scenario = client.scenarios.rename(scenario_guid, request)
    ```

## scenarios.delete { #method-scenarios-delete }

```python
async def delete(scenario_guid: str) -> Status
```

Delete a scenario.

REST operation: [`DELETE /sympheny-app/scenario/{scenarioGuid}`](../../api/reference/scenarios.md#operation-deleteScenario)

The API returns no `data` payload for this endpoint even on success, so a missing payload is treated as an empty [`Status`](models/common.md#model-Status) rather than an error.

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** [`Status`](models/common.md#model-Status)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        status = await client.scenarios.delete(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        status = client.scenarios.delete(scenario_guid)
    ```

## scenarios.copy { #method-scenarios-copy }

```python
async def copy(
    scenario_guid: str,
    *,
    analysis_destination_guid: str | None = None,
    name: str | None = None,
) -> ScenarioResponseDto
```

Copy a scenario, optionally into another analysis.

REST operation: [`PUT /sympheny-app/scenarios/copy/{scenarioGuid}`](../../api/reference/scenarios.md#operation-copyScenario)

Broken as of this writing (to be fixed server-side): the `name` argument is only applied when `analysis_destination_guid` is omitted (the copy stays in the source's analysis). When a destination *is* given, `name` is ignored and the copy takes the source's name *without* deduplicating, so copying the same source into one analysis twice fails the `scenario_name + analysis_id` unique constraint. To place a renamed copy in another analysis: copy into it without a name (the server assigns a unique "... (Copy)" name), then copy that in place with the wanted name.

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `analysis_destination_guid` | `str`, optional | no | GUID of the destination analysis; when omitted the copy stays in the source scenario's analysis. |
| `name` | `str`, optional | no | Name for the copy; see the caveat above. |

**Returns:** [`ScenarioResponseDto`](models/common.md#model-ScenarioResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        scenario = await client.scenarios.copy(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        scenario = client.scenarios.copy(scenario_guid)
    ```

## scenarios.excel_upload_url { #method-scenarios-excel_upload_url }

```python
async def excel_upload_url(*, delete_previous: bool | None = None) -> str
```

Get a presigned URL to upload a scenario Excel file to.

REST operation: [`GET /sympheny-app/db-update/s3-presigned-url`](../../api/reference/uploads.md#operation-s3PresignedUrl_1)

Upload the file to the returned URL with a plain HTTP `PUT` (no bearer token), then pass the URL to [`create_from_excel`](#method-scenarios-create_from_excel) or [`replace_from_excel`](#method-scenarios-replace_from_excel).

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `delete_previous` | `bool`, optional | no | Sent as the `deletePrevious` query parameter; the API defaults to `false`. |

**Returns:** `str`, the presigned upload URL.

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        url = await client.scenarios.excel_upload_url()
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        url = client.scenarios.excel_upload_url()
    ```

## scenarios.create_from_excel { #method-scenarios-create_from_excel }

```python
async def create_from_excel(analysis_guid: str, s3_presigned_url: str, name: str) -> ScenarioResponseDto
```

Create a scenario in an analysis from an uploaded Excel file.

REST operation: [`POST /sympheny-app/v2/analysis/{guid}/scenario/excel`](../../api/reference/scenarios.md#operation-createNewScenarioExcelV2_1)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `analysis_guid` | `str` | yes | GUID of the analysis. |
| `s3_presigned_url` | `str` | yes | URL from [`excel_upload_url`](#method-scenarios-excel_upload_url) that the file was uploaded to. |
| `name` | `str` | yes | Name of the new scenario. |

**Returns:** [`ScenarioResponseDto`](models/common.md#model-ScenarioResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        scenario = await client.scenarios.create_from_excel(analysis_guid, url, "From Excel")
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        scenario = client.scenarios.create_from_excel(analysis_guid, url, "From Excel")
    ```

## scenarios.replace_from_excel { #method-scenarios-replace_from_excel }

```python
async def replace_from_excel(scenario_guid: str, s3_presigned_url: str) -> ScenarioResponseDto
```

Replace a scenario's content with an uploaded Excel file.

REST operation: [`PUT /sympheny-app/v2/scenarios/{scenarioGuid}/excel`](../../api/reference/scenarios.md#operation-createNewScenarioExcelV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `s3_presigned_url` | `str` | yes | URL from [`excel_upload_url`](#method-scenarios-excel_upload_url) that the file was uploaded to. |

**Returns:** [`ScenarioResponseDto`](models/common.md#model-ScenarioResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        scenario = await client.scenarios.replace_from_excel(scenario_guid, url)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        scenario = client.scenarios.replace_from_excel(scenario_guid, url)
    ```

## scenarios.prepare_specs_input_files { #method-scenarios-prepare_specs_input_files }

```python
async def prepare_specs_input_files(scenario_guids: list[str]) -> Status
```

Start generating the specs input files of scenarios of one analysis.

REST operation: [`PUT /sympheny-app/v2/specs`](../../api/reference/specs.md#operation-finishSpecsAndSubmitForExecV2List)

Generation runs in the background: poll [`specs_input_file_url`](#method-scenarios-specs_input_file_url) for each scenario until it returns a URL.

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guids` | list of `str` | yes | GUIDs of the scenarios; all must belong to the same analysis. |

**Returns:** [`Status`](models/common.md#model-Status)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        status = await client.scenarios.prepare_specs_input_files([scenario_guid])
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        status = client.scenarios.prepare_specs_input_files([scenario_guid])
    ```

## scenarios.specs_input_file_url { #method-scenarios-specs_input_file_url }

```python
async def specs_input_file_url(scenario_guid: str) -> str | None
```

Get the download URL of a scenario's specs input file.

REST operation: [`GET /sympheny-app/scenario/{scenarioGuid}/specs-input-file-url`](../../api/reference/scenarios.md#operation-getSpecsInputFileUrl)

Returns `None` until the file started by [`prepare_specs_input_files`](#method-scenarios-prepare_specs_input_files) is ready.

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** `str`, the presigned download URL, or `None` while the file is not ready.

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        url = await client.scenarios.specs_input_file_url(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        url = client.scenarios.specs_input_file_url(scenario_guid)
    ```

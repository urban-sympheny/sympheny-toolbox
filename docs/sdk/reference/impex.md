<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/energy.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Imports and exports (impex)

Operations on energy imports and exports. Available on the client as `client.impex`.

## impex.create { #method-impex-create }

```python
async def create(scenario_guid: str, request: ImportExportRequestDtoV2) -> ImportExportResponseDtoV2
```

Create a new import/export in a scenario.

REST operation: [`POST /sympheny-app/v2_1/scenario/{scenarioGuid}/impex`](../../api/reference/impex.md#operation-createNewImpexV2_1)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `request` | [`ImportExportRequestDtoV2`](models/energy.md#model-ImportExportRequestDtoV2) | yes | Request body. |

**Returns:** [`ImportExportResponseDtoV2`](models/energy.md#model-ImportExportResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        impex = await client.impex.create(scenario_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        impex = client.impex.create(scenario_guid, request)
    ```

## impex.list { #method-impex-list }

```python
async def list(scenario_guid: str) -> list[ImportExportResponseDtoV2]
```

List the imports/exports of a scenario.

REST operation: [`GET /sympheny-app/v2/scenarios/{scenarioGuid}/impexes`](../../api/reference/impex.md#operation-findAllByScenarioV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** list of [`ImportExportResponseDtoV2`](models/energy.md#model-ImportExportResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        impexes = await client.impex.list(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        impexes = client.impex.list(scenario_guid)
    ```

## impex.get { #method-impex-get }

```python
async def get(
    impex_type: Type1,
    impex_guid: str,
    *,
    scenario_variant_guid: str | None = None,
) -> ImportExportResponseDtoV2
```

Get import/export details.

REST operation: [`GET /sympheny-app/v2/impex/{type}/{guid}`](../../api/reference/impex.md#operation-getImpexByGuidV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `impex_type` | [`Type1`](models/energy.md#model-Type1) | yes | Whether the record is an import or an export. |
| `impex_guid` | `str` | yes | GUID of the impex. |
| `scenario_variant_guid` | `str`, optional | no | GUID of the scenario variant to read from. |

**Returns:** [`ImportExportResponseDtoV2`](models/energy.md#model-ImportExportResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        impex = await client.impex.get(impex_type, impex_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        impex = client.impex.get(impex_type, impex_guid)
    ```

## impex.update { #method-impex-update }

```python
async def update(impex_guid: str, request: ImportExportResponseDtoV2) -> ImportExportResponseDtoV2
```

Update an import/export.

REST operation: [`PUT /sympheny-app/v2_1/scenarios/impex/{guid}`](../../api/reference/impex.md#operation-editImpexV2_1)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `impex_guid` | `str` | yes | GUID of the impex. |
| `request` | [`ImportExportResponseDtoV2`](models/energy.md#model-ImportExportResponseDtoV2) | yes | Request body. |

**Returns:** [`ImportExportResponseDtoV2`](models/energy.md#model-ImportExportResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        impex = await client.impex.update(impex_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        impex = client.impex.update(impex_guid, request)
    ```

## impex.delete { #method-impex-delete }

```python
async def delete(impex_type: Type1, impex_guid: str) -> Status
```

Delete an import/export.

REST operation: [`DELETE /sympheny-app/impex/{type}/{guid}`](../../api/reference/impex.md#operation-deleteImpex)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `impex_type` | [`Type1`](models/energy.md#model-Type1) | yes | Whether the record is an import or an export. |
| `impex_guid` | `str` | yes | GUID of the impex. |

**Returns:** [`Status`](models/common.md#model-Status)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        status = await client.impex.delete(impex_type, impex_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        status = client.impex.delete(impex_type, impex_guid)
    ```

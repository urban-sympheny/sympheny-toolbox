<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/technologies.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Storage technologies

Operations on storage technologies. Available on the client as `client.storage_technologies`.

## storage_technologies.create { #method-storage_technologies-create }

```python
async def create(
    scenario_guid: str,
    request: StorageTechnologyRequestDtoV2,
) -> StorageTechnologyResponseDtoV2
```

Create a storage technology in a scenario.

REST operation: [`POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/storage-technologies`](../../api/reference/storage-technologies.md#operation-specifyStorageTechnologyV2_1)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `request` | [`StorageTechnologyRequestDtoV2`](models/technologies.md#model-StorageTechnologyRequestDtoV2) | yes | Request body. |

**Returns:** [`StorageTechnologyResponseDtoV2`](models/technologies.md#model-StorageTechnologyResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        technology = await client.storage_technologies.create(scenario_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        technology = client.storage_technologies.create(scenario_guid, request)
    ```

## storage_technologies.list { #method-storage_technologies-list }

```python
async def list(scenario_guid: str) -> StorageTechnologyListResponseDtoV2
```

List the storage technologies of a scenario.

REST operation: [`GET /sympheny-app/v2/scenarios/{scenarioGuid}/storage-technologies`](../../api/reference/storage-technologies.md#operation-getAllStorageTechnologiesByScenarioV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** [`StorageTechnologyListResponseDtoV2`](models/technologies.md#model-StorageTechnologyListResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        technologies = await client.storage_technologies.list(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        technologies = client.storage_technologies.list(scenario_guid)
    ```

## storage_technologies.get { #method-storage_technologies-get }

```python
async def get(technology_guid: str) -> StorageTechnologyDetailResponseDtoV2
```

Get storage technology details.

REST operation: [`GET /sympheny-app/v2/scenarios/storage-technologies/{guid}`](../../api/reference/storage-technologies.md#operation-getStorageTechDetailsV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `technology_guid` | `str` | yes | GUID of the technology. |

**Returns:** [`StorageTechnologyDetailResponseDtoV2`](models/technologies.md#model-StorageTechnologyDetailResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        technology = await client.storage_technologies.get(technology_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        technology = client.storage_technologies.get(technology_guid)
    ```

## storage_technologies.update { #method-storage_technologies-update }

```python
async def update(
    technology_guid: str,
    request: StorageTechnologyDetailResponseDtoV2,
) -> StorageTechnologyDetailResponseDtoV2
```

Update a storage technology.

REST operation: [`PUT /sympheny-app/v2_2/scenarios/storage-technologies/{guid}`](../../api/reference/storage-technologies.md#operation-updateStorageTechnologyV2_2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `technology_guid` | `str` | yes | GUID of the technology. |
| `request` | [`StorageTechnologyDetailResponseDtoV2`](models/technologies.md#model-StorageTechnologyDetailResponseDtoV2) | yes | Request body. |

**Returns:** [`StorageTechnologyDetailResponseDtoV2`](models/technologies.md#model-StorageTechnologyDetailResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        technology = await client.storage_technologies.update(technology_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        technology = client.storage_technologies.update(technology_guid, request)
    ```

## storage_technologies.delete { #method-storage_technologies-delete }

```python
async def delete(technology_guid: str) -> StorageTechnologyListResponseDto
```

Delete a storage technology; returns the remaining storage technologies.

REST operation: [`DELETE /sympheny-app/scenarios/storage-technologies/{guid}`](../../api/reference/storage-technologies.md#operation-deleteStorageTechnology)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `technology_guid` | `str` | yes | GUID of the technology. |

**Returns:** [`StorageTechnologyListResponseDto`](models/technologies.md#model-StorageTechnologyListResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        remaining = await client.storage_technologies.delete(technology_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        remaining = client.storage_technologies.delete(technology_guid)
    ```

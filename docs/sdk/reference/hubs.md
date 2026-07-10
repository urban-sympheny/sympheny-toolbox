<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/scenarios.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Hubs

Operations on hubs. Available on the client as `client.hubs`.

## hubs.list { #method-hubs-list }

```python
async def list(scenario_guid: str) -> list[HubResponseDto]
```

List the hubs of a scenario.

REST operation: [`GET /sympheny-app/scenarios/{scenarioGuid}/hubs`](../../api/reference/hubs.md#operation-findAllHubsByScenario)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** list of [`HubResponseDto`](models/common.md#model-HubResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        hubs = await client.hubs.list(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        hubs = client.hubs.list(scenario_guid)
    ```

## hubs.create { #method-hubs-create }

```python
async def create(scenario_guid: str, request: HubRequestDto) -> HubResponseDto
```

Create a new hub in a scenario.

REST operation: [`POST /sympheny-app/scenarios/{scenarioGuid}/hubs`](../../api/reference/hubs.md#operation-createNewHub)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `request` | [`HubRequestDto`](models/scenarios.md#model-HubRequestDto) | yes | Request body. |

**Returns:** [`HubResponseDto`](models/common.md#model-HubResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        hub = await client.hubs.create(scenario_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        hub = client.hubs.create(scenario_guid, request)
    ```

## hubs.get { #method-hubs-get }

```python
async def get(hub_guid: str) -> HubResponseDto
```

Get hub details.

REST operation: [`GET /sympheny-app/scenarios/hubs/{guid}`](../../api/reference/hubs.md#operation-getHub)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hub_guid` | `str` | yes | GUID of the hub. |

**Returns:** [`HubResponseDto`](models/common.md#model-HubResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        hub = await client.hubs.get(hub_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        hub = client.hubs.get(hub_guid)
    ```

## hubs.update { #method-hubs-update }

```python
async def update(hub_guid: str, request: HubResponseDto) -> HubResponseDto
```

Update a hub.

REST operation: [`PUT /sympheny-app/v2/scenarios/hubs/{guid}`](../../api/reference/hubs.md#operation-editHub)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hub_guid` | `str` | yes | GUID of the hub. |
| `request` | [`HubResponseDto`](models/common.md#model-HubResponseDto) | yes | Request body. |

**Returns:** [`HubResponseDto`](models/common.md#model-HubResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        hub = await client.hubs.update(hub_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        hub = client.hubs.update(hub_guid, request)
    ```

## hubs.delete { #method-hubs-delete }

```python
async def delete(hub_guid: str) -> builtins.list[HubResponseDto]
```

Delete a hub; returns the remaining hubs.

REST operation: [`DELETE /sympheny-app/scenarios/hubs/{guid}`](../../api/reference/hubs.md#operation-deleteHub)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `hub_guid` | `str` | yes | GUID of the hub. |

**Returns:** list of [`HubResponseDto`](models/common.md#model-HubResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        remaining = await client.hubs.delete(hub_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        remaining = client.hubs.delete(hub_guid)
    ```

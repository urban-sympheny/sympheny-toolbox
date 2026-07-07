<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/technologies.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Network technologies

Operations on network technologies. Available on the client as `client.network_technologies`.

## network_technologies.create { #method-network_technologies-create }

```python
async def create(
    scenario_guid: str,
    request: NetworkTechnologyRequestDtoV2,
) -> NetworkTechnologyResponseDtoV2
```

Create a network technology in a scenario.

REST operation: [`POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/network-technologies`](../../api/reference/network-technologies.md#operation-specifyNetworkTechnologyV2_1)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `request` | [`NetworkTechnologyRequestDtoV2`](models/technologies.md#model-NetworkTechnologyRequestDtoV2) | yes | Request body. |

**Returns:** [`NetworkTechnologyResponseDtoV2`](models/technologies.md#model-NetworkTechnologyResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        technology = await client.network_technologies.create(scenario_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        technology = client.network_technologies.create(scenario_guid, request)
    ```

## network_technologies.list { #method-network_technologies-list }

```python
async def list(scenario_guid: str) -> NetworkTechnologyListResponseDtoV2
```

List the network technologies of a scenario.

REST operation: [`GET /sympheny-app/v2/scenarios/{scenarioGuid}/network-technologies`](../../api/reference/network-technologies.md#operation-getAllNetworkTechnologiesByScenarioV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** [`NetworkTechnologyListResponseDtoV2`](models/technologies.md#model-NetworkTechnologyListResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        technologies = await client.network_technologies.list(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        technologies = client.network_technologies.list(scenario_guid)
    ```

## network_technologies.get { #method-network_technologies-get }

```python
async def get(technology_guid: str) -> NetworkTechnologyResponseDtoV2
```

Get network technology details.

REST operation: [`GET /sympheny-app/v2/scenarios/network-technologies/{guid}`](../../api/reference/network-technologies.md#operation-getNetworkTechDetailsV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `technology_guid` | `str` | yes | GUID of the technology. |

**Returns:** [`NetworkTechnologyResponseDtoV2`](models/technologies.md#model-NetworkTechnologyResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        technology = await client.network_technologies.get(technology_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        technology = client.network_technologies.get(technology_guid)
    ```

## network_technologies.update { #method-network_technologies-update }

```python
async def update(
    technology_guid: str,
    request: NetworkTechnologyResponseDtoV2,
) -> NetworkTechnologyResponseDtoV2
```

Update a network technology.

REST operation: [`PUT /sympheny-app/v2_1/scenarios/network-technologies/{guid}`](../../api/reference/network-technologies.md#operation-updateNetworkTechnologyV2_1)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `technology_guid` | `str` | yes | GUID of the technology. |
| `request` | [`NetworkTechnologyResponseDtoV2`](models/technologies.md#model-NetworkTechnologyResponseDtoV2) | yes | Request body. |

**Returns:** [`NetworkTechnologyResponseDtoV2`](models/technologies.md#model-NetworkTechnologyResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        technology = await client.network_technologies.update(technology_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        technology = client.network_technologies.update(technology_guid, request)
    ```

## network_technologies.delete { #method-network_technologies-delete }

```python
async def delete(technology_guid: str) -> NetworkTechnologyListResponseDto
```

Delete a network technology; returns the remaining network technologies.

REST operation: [`DELETE /sympheny-app/scenarios/network-technologies/{guid}`](../../api/reference/network-technologies.md#operation-deleteNetworkTechnology)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `technology_guid` | `str` | yes | GUID of the technology. |

**Returns:** [`NetworkTechnologyListResponseDto`](models/technologies.md#model-NetworkTechnologyListResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        remaining = await client.network_technologies.delete(technology_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        remaining = client.network_technologies.delete(technology_guid)
    ```

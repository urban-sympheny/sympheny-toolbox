<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/technologies.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Network links

Operations on network links. Available on the client as `client.network_links`.

## network_links.create { #method-network_links-create }

```python
async def create(scenario_guid: str, request: NetworkLinkRequestDtoV2) -> NetworkLinkResponseDtoV2
```

Create a network link in a scenario.

REST operation: [`POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/network-links`](../../api/reference/network-links.md#operation-specifyNetworkLinkV2_1)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `request` | [`NetworkLinkRequestDtoV2`](models/technologies.md#model-NetworkLinkRequestDtoV2) | yes | Request body. |

**Returns:** [`NetworkLinkResponseDtoV2`](models/technologies.md#model-NetworkLinkResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        link = await client.network_links.create(scenario_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        link = client.network_links.create(scenario_guid, request)
    ```

## network_links.list { #method-network_links-list }

```python
async def list(scenario_guid: str) -> list[NetworkLinkResponseDtoV2]
```

List the network links of a scenario.

REST operation: [`GET /sympheny-app/v2/scenarios/{scenarioGuid}/network-links`](../../api/reference/network-links.md#operation-getAllNetworkLinksByScenarioV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** list of [`NetworkLinkResponseDtoV2`](models/technologies.md#model-NetworkLinkResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        links = await client.network_links.list(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        links = client.network_links.list(scenario_guid)
    ```

## network_links.get { #method-network_links-get }

```python
async def get(link_guid: str) -> NetworkLinkResponseDtoV2
```

Get network link details.

REST operation: [`GET /sympheny-app/v2/network-links/{network-link-guid}`](../../api/reference/network-links.md#operation-getNetworkLinkDetailsV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `link_guid` | `str` | yes | GUID of the link. |

**Returns:** [`NetworkLinkResponseDtoV2`](models/technologies.md#model-NetworkLinkResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        link = await client.network_links.get(link_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        link = client.network_links.get(link_guid)
    ```

## network_links.update { #method-network_links-update }

```python
async def update(
    scenario_guid: str,
    link_guid: str,
    request: NetworkLinkResponseDtoV2,
) -> NetworkLinkResponseDtoV2
```

Update a network link.

REST operation: [`PUT /sympheny-app/v2_2/scenarios/{scenarioGuid}/network-links/{network-link-guid}`](../../api/reference/network-links.md#operation-updateNetworkLinkV2_2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `link_guid` | `str` | yes | GUID of the link. |
| `request` | [`NetworkLinkResponseDtoV2`](models/technologies.md#model-NetworkLinkResponseDtoV2) | yes | Request body. |

**Returns:** [`NetworkLinkResponseDtoV2`](models/technologies.md#model-NetworkLinkResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        link = await client.network_links.update(scenario_guid, link_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        link = client.network_links.update(scenario_guid, link_guid, request)
    ```

## network_links.delete { #method-network_links-delete }

```python
async def delete(scenario_guid: str, link_guid: str) -> NetworkLinkListResponseDto
```

Delete a network link; returns the remaining links.

REST operation: [`DELETE /sympheny-app/scenarios/{scenarioGuid}/network-links/{network-link-guid}`](../../api/reference/network-links.md#operation-deleteNetworkLink)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `link_guid` | `str` | yes | GUID of the link. |

**Returns:** [`NetworkLinkListResponseDto`](models/technologies.md#model-NetworkLinkListResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        remaining = await client.network_links.delete(scenario_guid, link_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        remaining = client.network_links.delete(scenario_guid, link_guid)
    ```

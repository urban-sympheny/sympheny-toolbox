<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/technologies.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Intra-hub network links

Operations on intra-hub network links. Available on the client as `client.intra_hub_network_links`.

## intra_hub_network_links.create { #method-intra_hub_network_links-create }

```python
async def create(
    scenario_guid: str,
    request: IntraHubNetworkLinkRequestDto,
) -> IntraHubNetworkLinkResponseDto
```

Create an intra-hub network link in a scenario.

REST operation: [`POST /sympheny-app/v2/scenarios/{scenarioGuid}/intra-hub-network-links`](../../api/reference/intra-hub-network-links.md#operation-specifyIntraHubNetworkLinkV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `request` | [`IntraHubNetworkLinkRequestDto`](models/technologies.md#model-IntraHubNetworkLinkRequestDto) | yes | Request body. |

**Returns:** [`IntraHubNetworkLinkResponseDto`](models/technologies.md#model-IntraHubNetworkLinkResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        link = await client.intra_hub_network_links.create(scenario_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        link = client.intra_hub_network_links.create(scenario_guid, request)
    ```

## intra_hub_network_links.list { #method-intra_hub_network_links-list }

```python
async def list(scenario_guid: str) -> IntraHubNetworkLinkListResponseDto
```

List the intra-hub network links of a scenario.

REST operation: [`GET /sympheny-app/scenarios/{scenarioGuid}/intra-hub-network-links`](../../api/reference/intra-hub-network-links.md#operation-getAllIntraHubNetworkLinks)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** [`IntraHubNetworkLinkListResponseDto`](models/technologies.md#model-IntraHubNetworkLinkListResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        links = await client.intra_hub_network_links.list(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        links = client.intra_hub_network_links.list(scenario_guid)
    ```

## intra_hub_network_links.get { #method-intra_hub_network_links-get }

```python
async def get(link_guid: str) -> IntraHubNetworkLinkResponseDto
```

Get intra-hub network link details.

REST operation: [`GET /sympheny-app/scenarios/intra-hub-network-links/{guid}`](../../api/reference/intra-hub-network-links.md#operation-getIntraHubNetworkLinkDetails)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `link_guid` | `str` | yes | GUID of the link. |

**Returns:** [`IntraHubNetworkLinkResponseDto`](models/technologies.md#model-IntraHubNetworkLinkResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        link = await client.intra_hub_network_links.get(link_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        link = client.intra_hub_network_links.get(link_guid)
    ```

## intra_hub_network_links.update { #method-intra_hub_network_links-update }

```python
async def update(
    link_guid: str,
    request: IntraHubNetworkLinkResponseDto,
) -> IntraHubNetworkLinkResponseDto
```

Update an intra-hub network link.

REST operation: [`PUT /sympheny-app/v2/scenarios/intra-hub-network-links/{guid}`](../../api/reference/intra-hub-network-links.md#operation-updateIntraHubNetworkLinkV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `link_guid` | `str` | yes | GUID of the link. |
| `request` | [`IntraHubNetworkLinkResponseDto`](models/technologies.md#model-IntraHubNetworkLinkResponseDto) | yes | Request body. |

**Returns:** [`IntraHubNetworkLinkResponseDto`](models/technologies.md#model-IntraHubNetworkLinkResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        link = await client.intra_hub_network_links.update(link_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        link = client.intra_hub_network_links.update(link_guid, request)
    ```

## intra_hub_network_links.delete { #method-intra_hub_network_links-delete }

```python
async def delete(link_guid: str) -> IntraHubNetworkLinkListResponseDto
```

Delete an intra-hub network link; returns the remaining links.

REST operation: [`DELETE /sympheny-app/scenarios/intra-hub-network-links/{guid}`](../../api/reference/intra-hub-network-links.md#operation-deleteIntraHubNetworkLink)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `link_guid` | `str` | yes | GUID of the link. |

**Returns:** [`IntraHubNetworkLinkListResponseDto`](models/technologies.md#model-IntraHubNetworkLinkListResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        remaining = await client.intra_hub_network_links.delete(link_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        remaining = client.intra_hub_network_links.delete(link_guid)
    ```

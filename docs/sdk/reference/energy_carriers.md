<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/energy.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Energy carriers

Operations on energy carriers. Available on the client as `client.energy_carriers`.

## energy_carriers.create { #method-energy_carriers-create }

```python
async def create(scenario_guid: str, request: EnergyCarrierRequestDtoV2) -> EnergyCarrierResponseDto
```

Create a new energy carrier in a scenario.

REST operation: [`POST /sympheny-app/v2/scenarios/{scenarioGuid}/carriers`](../../api/reference/energy-carriers.md#operation-createNewEnergyCarrierV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `request` | [`EnergyCarrierRequestDtoV2`](models/energy.md#model-EnergyCarrierRequestDtoV2) | yes | Request body. |

**Returns:** [`EnergyCarrierResponseDto`](models/common.md#model-EnergyCarrierResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        carrier = await client.energy_carriers.create(scenario_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        carrier = client.energy_carriers.create(scenario_guid, request)
    ```

## energy_carriers.list { #method-energy_carriers-list }

```python
async def list(scenario_guid: str) -> EnergyCarriersListResponseDto
```

List the energy carriers of a scenario.

REST operation: [`GET /sympheny-app/scenarios/{scenarioGuid}/carriers`](../../api/reference/energy-carriers.md#operation-findAllEnergyCarriersByScenario)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** [`EnergyCarriersListResponseDto`](models/energy.md#model-EnergyCarriersListResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        carriers = await client.energy_carriers.list(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        carriers = client.energy_carriers.list(scenario_guid)
    ```

## energy_carriers.get { #method-energy_carriers-get }

```python
async def get(carrier_guid: str) -> EnergyCarrierResponseDto
```

Get energy carrier details.

REST operation: [`GET /sympheny-app/carriers/{carrierGuid}`](../../api/reference/energy-carriers.md#operation-getEnergyCarrierByGuid)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `carrier_guid` | `str` | yes | GUID of the carrier. |

**Returns:** [`EnergyCarrierResponseDto`](models/common.md#model-EnergyCarrierResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        carrier = await client.energy_carriers.get(carrier_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        carrier = client.energy_carriers.get(carrier_guid)
    ```

## energy_carriers.update { #method-energy_carriers-update }

```python
async def update(carrier_guid: str, request: EnergyCarrierResponseDto) -> EnergyCarrierResponseDto
```

Update an energy carrier.

REST operation: [`PUT /sympheny-app/v2/carriers/{carrierGuid}`](../../api/reference/energy-carriers.md#operation-editEnergyCarrierV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `carrier_guid` | `str` | yes | GUID of the carrier. |
| `request` | [`EnergyCarrierResponseDto`](models/common.md#model-EnergyCarrierResponseDto) | yes | Request body. |

**Returns:** [`EnergyCarrierResponseDto`](models/common.md#model-EnergyCarrierResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        carrier = await client.energy_carriers.update(carrier_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        carrier = client.energy_carriers.update(carrier_guid, request)
    ```

## energy_carriers.delete { #method-energy_carriers-delete }

```python
async def delete(carrier_guid: str) -> EnergyCarriersListResponseDto
```

Delete an energy carrier; returns the remaining carriers.

REST operation: [`DELETE /sympheny-app/scenarios/carriers/{guid}`](../../api/reference/energy-carriers.md#operation-deleteEnergyCarrier)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `carrier_guid` | `str` | yes | GUID of the carrier. |

**Returns:** [`EnergyCarriersListResponseDto`](models/energy.md#model-EnergyCarriersListResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        remaining = await client.energy_carriers.delete(carrier_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        remaining = client.energy_carriers.delete(carrier_guid)
    ```

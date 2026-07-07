<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/energy.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Profiles

Operations on profiles. Available on the client as `client.profiles`.

## profiles.create { #method-profiles-create }

```python
async def create(scenario_guid: str, request: ProfileJsonRequestDto) -> ProfileResponseDto
```

Create a new profile in a scenario.

REST operation: [`POST /sympheny-app/scenarios/{scenarioGuid}/profiles-json`](../../api/reference/profiles.md#operation-createJson)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `request` | [`ProfileJsonRequestDto`](models/energy.md#model-ProfileJsonRequestDto) | yes | Request body. |

**Returns:** [`ProfileResponseDto`](models/energy.md#model-ProfileResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        profile = await client.profiles.create(scenario_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        profile = client.profiles.create(scenario_guid, request)
    ```

## profiles.list { #method-profiles-list }

```python
async def list(scenario_guid: str) -> list[ProfileResponseDto]
```

List the profiles of a scenario.

REST operation: [`GET /sympheny-app/scenarios/{scenarioGuid}/profiles`](../../api/reference/profiles.md#operation-list_1)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** list of [`ProfileResponseDto`](models/energy.md#model-ProfileResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        profiles = await client.profiles.list(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        profiles = client.profiles.list(scenario_guid)
    ```

## profiles.get { #method-profiles-get }

```python
async def get(scenario_guid: str, profile_id: int) -> ProfileDetailsResponseDto
```

Get profile details.

REST operation: [`GET /sympheny-app/scenarios/{scenarioGuid}/profiles/{profileId}`](../../api/reference/profiles.md#operation-get)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `profile_id` | `int` | yes | Numeric id of the profile. |

**Returns:** [`ProfileDetailsResponseDto`](models/energy.md#model-ProfileDetailsResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        profile = await client.profiles.get(scenario_guid, profile_id)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        profile = client.profiles.get(scenario_guid, profile_id)
    ```

## profiles.update { #method-profiles-update }

```python
async def update(
    scenario_guid: str,
    profile_id: int,
    request: ProfileDetailsResponseDto,
) -> ProfileDetailsResponseDto
```

Update a profile.

REST operation: [`PUT /sympheny-app/v2/scenarios/{scenarioGuid}/profiles-json/{profileId}`](../../api/reference/profiles.md#operation-editJsonV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `profile_id` | `int` | yes | Numeric id of the profile. |
| `request` | [`ProfileDetailsResponseDto`](models/energy.md#model-ProfileDetailsResponseDto) | yes | Request body. |

**Returns:** [`ProfileDetailsResponseDto`](models/energy.md#model-ProfileDetailsResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        profile = await client.profiles.update(scenario_guid, profile_id, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        profile = client.profiles.update(scenario_guid, profile_id, request)
    ```

## profiles.delete { #method-profiles-delete }

```python
async def delete(scenario_guid: str, profile_id: int) -> None
```

Delete a profile.

REST operation: [`DELETE /sympheny-app/scenarios/{scenarioGuid}/profiles/{profileId}`](../../api/reference/profiles.md#operation-delete_1)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `profile_id` | `int` | yes | Numeric id of the profile. |

**Returns:** `None`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        await client.profiles.delete(scenario_guid, profile_id)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        client.profiles.delete(scenario_guid, profile_id)
    ```

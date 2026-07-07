<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/projects.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Analyses

Operations on analyses. Available on the client as `client.analyses`.

## analyses.list { #method-analyses-list }

```python
async def list(project_guid: str) -> list[AnalysisResponseDto]
```

List the analyses of a project.

REST operation: [`GET /sympheny-app/projects/{guid}/analyses`](../../api/reference/analyses.md#operation-list_2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `project_guid` | `str` | yes | GUID of the project. |

**Returns:** list of [`AnalysisResponseDto`](models/projects.md#model-AnalysisResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        analyses = await client.analyses.list(project_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        analyses = client.analyses.list(project_guid)
    ```

## analyses.create { #method-analyses-create }

```python
async def create(project_guid: str, request: AnalysisRequestDto) -> AnalysisResponseDto
```

Create a new analysis in a project.

REST operation: [`POST /sympheny-app/projects/{guid}/analyses`](../../api/reference/analyses.md#operation-createNewAnalysis)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `project_guid` | `str` | yes | GUID of the project. |
| `request` | [`AnalysisRequestDto`](models/projects.md#model-AnalysisRequestDto) | yes | Request body. |

**Returns:** [`AnalysisResponseDto`](models/projects.md#model-AnalysisResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        analysis = await client.analyses.create(project_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        analysis = client.analyses.create(project_guid, request)
    ```

## analyses.get { #method-analyses-get }

```python
async def get(project_guid: str, analysis_guid: str) -> AnalysisDetailsResponseDto
```

Get analysis details.

REST operation: [`GET /sympheny-app/projects/{guid}/analysis/{analysisGuid}`](../../api/reference/analyses.md#operation-viewAnalysisDetails)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `project_guid` | `str` | yes | GUID of the project. |
| `analysis_guid` | `str` | yes | GUID of the analysis. |

**Returns:** [`AnalysisDetailsResponseDto`](models/projects.md#model-AnalysisDetailsResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        analysis = await client.analyses.get(project_guid, analysis_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        analysis = client.analyses.get(project_guid, analysis_guid)
    ```

## analyses.delete { #method-analyses-delete }

```python
async def delete(analysis_guid: str) -> Status
```

Delete an analysis.

REST operation: [`DELETE /sympheny-app/analysis/{analysisGuid}`](../../api/reference/analyses.md#operation-deleteAnalysis)

The API returns no `data` payload for this endpoint even on success, so a missing payload is treated as an empty [`Status`](models/common.md#model-Status) rather than an error.

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `analysis_guid` | `str` | yes | GUID of the analysis. |

**Returns:** [`Status`](models/common.md#model-Status)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        status = await client.analyses.delete(analysis_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        status = client.analyses.delete(analysis_guid)
    ```

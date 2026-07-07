<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/projects.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Projects

Operations on projects. Available on the client as `client.projects`.

## projects.list { #method-projects-list }

```python
async def list() -> list[ProjectResponseDto]
```

List all projects visible to the authenticated user.

REST operation: [`GET /sympheny-app/projects`](../../api/reference/projects.md#operation-viewMyProjects)

**Returns:** list of [`ProjectResponseDto`](models/projects.md#model-ProjectResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        projects = await client.projects.list()
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        projects = client.projects.list()
    ```

## projects.create { #method-projects-create }

```python
async def create(request: ProjectRequestDto) -> ProjectResponseDto
```

Create a new project. Only V2 projects are supported.

REST operation: [`POST /sympheny-app/projects`](../../api/reference/projects.md#operation-createNewProject)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [`ProjectRequestDto`](models/projects.md#model-ProjectRequestDto) | yes | Request body. |

**Returns:** [`ProjectResponseDto`](models/projects.md#model-ProjectResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        project = await client.projects.create(request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        project = client.projects.create(request)
    ```

## projects.get { #method-projects-get }

```python
async def get(
    project_guid: str,
    *,
    include_analyses: bool | None = None,
) -> ProjectDetailResponseDto
```

Get project details.

REST operation: [`GET /sympheny-app/projects/{guid}`](../../api/reference/projects.md#operation-viewProjectDetails)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `project_guid` | `str` | yes | GUID of the project. |
| `include_analyses` | `bool`, optional | no | Also return the project's analyses. |

**Returns:** [`ProjectDetailResponseDto`](models/projects.md#model-ProjectDetailResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        project = await client.projects.get(project_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        project = client.projects.get(project_guid)
    ```

## projects.delete { #method-projects-delete }

```python
async def delete(project_guid: str) -> ProjectSummaryResponseDto
```

Delete a project; returns the remaining projects.

REST operation: [`DELETE /sympheny-app/projects/{guid}`](../../api/reference/projects.md#operation-deleteProject)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `project_guid` | `str` | yes | GUID of the project. |

**Returns:** [`ProjectSummaryResponseDto`](models/projects.md#model-ProjectSummaryResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        remaining = await client.projects.delete(project_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        remaining = client.projects.delete(project_guid)
    ```

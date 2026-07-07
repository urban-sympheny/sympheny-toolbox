<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/solver.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Users

User account endpoints. Available on the client as `client.users`.

## users.profile { #method-users-profile }

```python
async def profile() -> GetUserProfileExt
```

Get the profile of the authenticated user.

REST operation: [`GET /backoffice/ext/users/profile`](../../api/reference/users.md#operation-get_user_profile_backoffice_ext_users_profile_get)

**Returns:** [`GetUserProfileExt`](models/solver.md#model-GetUserProfileExt)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        profile = await client.users.profile()
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        profile = client.users.profile()
    ```

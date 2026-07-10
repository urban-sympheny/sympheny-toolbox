<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Users

External API - users resource

## Get User Profile { #operation-get_user_profile_backoffice_ext_users_profile_get }

```
GET /backoffice/ext/users/profile
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.users.profile()`](../../sdk/reference/users.md#method-users-profile).

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/backoffice/ext/users/profile" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | Successful Response | `GetUserProfileExt` |
| 400 | Bad Request | `AppException` |
| 401 | Unauthorized | `AppException` |
| 404 | Not Found | `AppException` |
| 409 | Conflict | `AppException` |
| 500 | Internal Server Error | `AppException` |

**Example response** (200)

```json
{
  "account": {
    "email": "user@example.com",
    "planLimitationId": "string",
    "organizationId": "string",
    "subscriptionId": "string",
    "planExpiry": "2026-01-01",
    "numberOfExecutionsLeft": 0,
    "executionTimeWeekLeft": 0,
    "mfa": false,
    "deactivated": false,
    "superuser": false,
    "admin": false,
    "showMaintenanceInfo": false,
    "showGtc": false,
    "showUserGuide": false,
    "accountGuid": "string",
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z"
  },
  "preferences": {
    "exchangeCurrencyDefault": "string",
    "unitSystemDefault": "string",
    "languageDefault": "English",
    "interestRateDefault": 0.0,
    "firstName": "string",
    "lastName": "string",
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z"
  },
  "planLimitation": {
    "intraHubNetwork": false,
    "advancedCostComponents": false,
    "unitCommitment": false,
    "maxEnergyCarriersPerHub": 0,
    "maxEnergyDemands": 0,
    "maxHubs": 0,
    "maxStages": 1,
    "maxSolarResources": 0,
    "maxOtherResources": 0,
    "maxImports": 0,
    "maxExports": 0,
    "maxConversionTechs": 0,
    "maxConversionModes": 0,
    "maxStorageTechs": 0,
    "maxNetworkTechs": 0,
    "maxNetworkLinks": 0,
    "maxExecutions": 0,
    "maxSimultaneousExecutions": 0,
    "maxExecutionTime": 0,
    "maxExecutionTimeWeek": 0,
    "maxExecutionHistory": 100,
    "maxParetoPoints": 9,
    "fullTemporalResolution": false,
    "maxProjects": 0,
    "maxAnalyses": 0,
    "maxScenarios": 0,
    "shareProject": false,
    "organizationDb": false,
    "scenarioVariants": false,
    "maxScenarioVariants": 0,
    "name": "string",
    "id": "string",
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "sagemakerOn": true,
    "sagemakerRegions": [
      "eu-north-1"
    ]
  },
  "organization": {
    "name": "string",
    "gisOn": false,
    "sepOn": false,
    "sepBuildingsLimit": 0,
    "executionSlots": 0,
    "variableBilling": false,
    "maxExecutions": 0,
    "maxSimultaneousExecutions": 0,
    "maxExecutionTime": 0,
    "maxExecutionTimeWeek": 0,
    "numberOfExecutionsLeft": 0,
    "executionTimeWeekLeft": 0,
    "id": "string",
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "sepBuildingsConsumed": 0
  },
  "subscription": {
    "name": "string",
    "organizationId": "string",
    "startDate": "2026-01-01",
    "endDate": "2026-01-01",
    "billingCycle": "MONTHLY",
    "nextBillingDate": "2026-01-01",
    "variableBilling": false,
    "executionPriority": 0,
    "maxSimultaneousExecutions": 0,
    "maxExecutionsPerCycle": 0,
    "maxExecutionTimePerCycle": 0,
    "maxExecutionsPerWeek": 0,
    "maxExecutionTimePerWeek": 0,
    "userMaxExecutionsPerCycle": 0,
    "userMaxExecutionTimePerCycle": 0,
    "userMaxExecutionsPerWeek": 0,
    "userMaxExecutionTimePerWeek": 0,
    "id": "string",
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z"
  },
  "profilePicture": "string",
  "organizationPicture": "string"
}
```

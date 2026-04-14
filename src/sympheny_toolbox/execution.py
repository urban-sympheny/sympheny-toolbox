import time
from urllib.parse import quote, urlencode

import requests as r


def execute(s, scenario_guid):
    base_url = s.base_url
    be = s.be
    h = s.h

    scenario = r.get(f"{be}scenario/{scenario_guid}", headers=h).json()["data"]
    scenario_name = scenario["scenarioName"]

    data = [
        {
            "objective1": "MIN_LIFE_CYCLE_COST",
            "objective2": "MIN_CO2_EMISSIONS",
            "scenarioGuid": scenario_guid,
            "scenarioName": scenario_name,
            "name": "j",
            "clientType": "APP",
            "temporalResolution": "LOW",
            "points": 2,
            "timeLimit": 3,
            "mipGap": 1,
        }
    ]
    resp = r.post(f"{base_url}sense-api/ext/solver/jobs", headers=h, json=data)
    resp.raise_for_status()

    # wait
    # 7) wait for execution to terminate
    data = {"scenarioGuids": [scenario_guid], "limit": 200}

    sleep = 10
    for _ in range(100):
        resp = r.post(
            f"{base_url}sense-api/ext/solver/jobs/get-scenarios", headers=h, json=data
        )
        running_jobs = list(
            filter(
                lambda j: j["scenarioGuid"] == scenario_guid and not j["terminated"],
                resp.json(),
            )
        )
        if not running_jobs:
            print("job is done")
            break

        print(f"sleep {sleep}s")
        time.sleep(sleep)

    job = next(filter(lambda j: j["scenarioGuid"] == scenario_guid, resp.json()))
    infeasibility_info = job.get("infeasibilityInfo")
    if infeasibility_info:
        print("Execution failure:")
        raise Exception(infeasibility_info)

    # get execution result zip
    job_id = job["id"]
    resp = r.get(f"{base_url}sense-api/ext/solver/jobs/{job_id}", headers=h).json()
    execution_result_zip = resp["outputFile"]

    print("Execution success, result zip:")
    print(execution_result_zip)
    print("Result dashboard:")
    print(dashboard_url_v2(s, scenario_guid))


def dashboard_url_v2(s, scenario_id) -> str | None:
    base_url = s.base_url
    h = s.h

    be = f"{base_url}sympheny-app/"
    resp = r.get(f"{be}scenario/{scenario_id}", headers=h)
    if resp.status_code != 200:
        return None

    scenario = resp.json()["data"]
    analysis_id = scenario["analysisGuid"]
    project_id = scenario["projectGuid"]

    data = {"scenarioGuids": [scenario_id], "limit": 200}
    resp = r.post(
        f"{base_url}sense-api/ext/solver/jobs/get-scenarios", headers=h, json=data
    )

    done_jobs = list(
        filter(
            lambda j: j["scenarioGuid"] == scenario_id and j["status"] == "DONE",
            resp.json(),
        )
    )
    if not done_jobs:
        return None

    job_id = done_jobs[0]["id"]

    # hubs
    hubs = r.get(f"{be}scenarios/{scenario_id}/hubs", headers=h).json()["data"]
    hub = None
    if hubs:
        hub = hubs[0]["hubName"]

    # stages
    stages = r.get(f"{be}scenarios/{scenario_id}/stages", headers=h).json()["data"]
    stage = None
    if stages:
        stage = stages[0]["name"]

    domain = "app.dev.sympheny.com" if "dev" in be else "app.sympheny.com"
    url = f"https://{domain}/projects/{project_id}/analysis/{analysis_id}/execution/{job_id}/solution/1/general"

    if hub and stage:
        params = {"hub": hub, "stage": stage}
        url = f"{url}?{urlencode(params, quote_via=quote)}"

    return url

import requests as r

from sympheny_toolbox.utils import wait_until

tech_options = [
    "PV",
    "HEAT_PUMP",
    "GAS_BOILER",
    "CHILLER",
    "BATTERY",
    "HOT_WATER_STORAGE",
]
demand_options = ["HOT_WATER", "SPACE_HEATING", "ELECTRICITY", "COOLING"]
import_options = ["ELECTRICITY"]
export_options = ["HEAT_AMBIENT", "COOLING"]


def create_enymap(
    s,
    scenario_name,
    analysis_id,
    techs: list[str],
    demands: list[str],
    imports: list[str],
    exports: list[str],
    poly: list,
):
    pairs_to_validate = [
        (techs, tech_options),
        (demands, demand_options),
        (imports, import_options),
        (exports, export_options),
    ]
    for params, refs in pairs_to_validate:
        validate(params, refs)

    base_url = s.base_url
    be = s.be
    h = s.h

    post = {
        "scenarioName": scenario_name,
        "length": 4,
        "interestRate": 8.4,
        "exchangeCurrency": "CHF",
        "exchangeRate": 1.6,
        "scope": "REGIONAL_NATIONAL",
        "technologies": techs,
        "demands": demands,
        "imports": imports,
        "exports": exports,
    }
    resp = r.post(f"{be}analysis/{analysis_id}/scenario-enymap", json=post, headers=h)
    resp.raise_for_status()
    scenario_id = resp.json()["data"]["scenarioGuid"]

    # create hub and wait for api-services job
    # print(to_geojson_coords(poly))
    resp = r.post(
        f"{be}scenario-enymap/{scenario_id}/create-gis-hub",
        json={"polygon": poly},
        headers=h,
    )
    resp.raise_for_status()
    wait_until(
        request_fn=lambda: r.get(
            f"{base_url}api-services/gis/background", headers=h
        ).json(),
        check_fn=lambda resp: resp[0]["is_done"],
    )

    # create demands and solar
    resp = r.post(f"{be}scenario-enymap/{scenario_id}/create-demand-solar", headers=h)
    resp.raise_for_status()

    # prepare scenario for execution
    resp = r.put(f"{be}v2/scenarios/{scenario_id}/specs", headers=h)
    resp.raise_for_status()

    return scenario_id


def validate(params: list[str], refs: list[str]):
    params_set = set(params)
    if len(params_set) != len(params):
        raise ValueError(f"You have duplicate value in: {params}")

    missing_items = params_set - set(refs)
    if missing_items:
        raise ValueError(
            f"Invalid values found: {missing_items}. Acceptable values are: {refs}"
        )

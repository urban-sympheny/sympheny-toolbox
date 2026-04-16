import requests as r

def get_demand_profile(demand_type, building_type, construction_end, building_area_m2, base_url, h):
    url = f"{base_url}api-services/demand/hub_demand?demand_type={demand_type}&building_type={building_type}"
    data = [{"construction_end": construction_end, "building_ground_area": building_area_m2, "nbr_floor": 1}]
    d = r.post(url, headers=h, json=data).json()[0]
    total_demand, demand_guid = d["totalAnnualDemand"], d["energyDemandMetadataGuid"]

    profile = r.get(f"{base_url}sympheny-app/database-energy-demands/{demand_guid}/profile", headers=h).json()["data"]
    profile = [x["demandValue"] * total_demand for x in profile]
    return profile
"""Pydantic models generated from docs/sympheny_openapi.json — do NOT edit by hand.

Regenerate with: uv run python scripts/generate_models.py
"""

from __future__ import annotations

from datetime import date
from enum import Enum, StrEnum
from typing import Any
from uuid import UUID

from pydantic import (
    UUID4,
    AnyUrl,
    AwareDatetime,
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
)


class Version(StrEnum):
    v1 = "V1"
    v2 = "V2"


class ProjectRequestDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    project_name: str = Field(..., alias="projectName", max_length=100, min_length=0)
    version: Version
    webhook_url: str | None = Field(None, alias="webhookUrl")
    favorite: bool | None = None
    gis_centroid_x: float | None = Field(None, alias="gisCentroidX")
    gis_centroid_y: float | None = Field(None, alias="gisCentroidY")
    zoom_extent_xmin: float | None = Field(None, alias="zoomExtentXmin")
    zoom_extent_ymin: float | None = Field(None, alias="zoomExtentYmin")
    zoom_extent_xmax: float | None = Field(None, alias="zoomExtentXmax")
    zoom_extent_ymax: float | None = Field(None, alias="zoomExtentYmax")


class Version1(Enum):
    v1 = "V1"
    v2 = "V2"
    none_type_none = None


class SecondaryOwnerDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    email: str
    can_edit: bool | None = Field(None, alias="canEdit")
    favorite: bool | None = None


class Status(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    code: str | None = None
    desc: str | None = None
    message: str | None = None


class ImageResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    url: str | None = None
    guid: str | None = None
    cover: bool | None = None


class ProjectOwnerHistoryResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    owned_at: AwareDatetime | None = Field(None, alias="ownedAt")
    owner_email: str | None = Field(None, alias="ownerEmail")


class Scope(Enum):
    building_developments = "BUILDING_DEVELOPMENTS"
    regional_national = "REGIONAL_NATIONAL"
    industrial_parks = "INDUSTRIAL_PARKS"
    none_type_none = None


class Technology(StrEnum):
    pv = "PV"
    heat_pump = "HEAT_PUMP"
    gas_boiler = "GAS_BOILER"
    hot_water_storage = "HOT_WATER_STORAGE"
    chiller = "CHILLER"
    battery = "BATTERY"


class Demand(StrEnum):
    hot_water = "HOT_WATER"
    space_heating = "SPACE_HEATING"
    electricity = "ELECTRICITY"
    cooling = "COOLING"


class Import(StrEnum):
    electricity = "ELECTRICITY"


class Export(StrEnum):
    heat_ambient = "HEAT_AMBIENT"
    cooling = "COOLING"


class ScenarioEnymapResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    length: int | None = None
    interest_rate: float | None = Field(None, alias="interestRate")
    exchange_currency: str | None = Field(None, alias="exchangeCurrency")
    exchange_rate: float | None = Field(None, alias="exchangeRate")
    scope: Scope | None = None
    technologies: list[Technology] | None = None
    demands: list[Demand] | None = None
    imports: list[Import] | None = None
    exports: list[Export] | None = None
    multi_hubs: bool | None = Field(None, alias="multiHubs")


class AnalysisRequestDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    analysis_name: str = Field(..., alias="analysisName", max_length=100, min_length=0)


class ExecutionStatus(Enum):
    in_specification = "IN_SPECIFICATION"
    ready_to_submit = "READY_TO_SUBMIT"
    picked = "PICKED"
    failed = "FAILED"
    aborted = "ABORTED"
    running = "RUNNING"
    done = "DONE"
    none_type_none = None


class ExecutionOptionsResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    objective1: str | None = None
    objective2: str | None = None
    number_of_pareto_points: int | None = Field(None, alias="numberOfParetoPoints")
    scenarios: list[str] | None = None


class Status1(Enum):
    in_specification = "IN_SPECIFICATION"
    submitted = "SUBMITTED"
    aborted = "ABORTED"
    validating = "VALIDATING"
    valid = "VALID"
    invalid = "INVALID"
    pending = "PENDING"
    running = "RUNNING"
    done_optimization = "DONE_OPTIMIZATION"
    generating_results = "GENERATING_RESULTS"
    done = "DONE"
    failed = "FAILED"
    stopped = "STOPPED"
    none_type_none = None


class ResultsScenarioResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    scenario_name: str | None = Field(None, alias="scenarioName")
    status: Status1 | None = None
    status_message: str | None = Field(None, alias="statusMessage")
    pareto_points_completed: str | None = Field(None, alias="paretoPointsCompleted")
    input_filepath: str | None = Field(None, alias="inputFilepath")
    output_filepath: str | None = Field(None, alias="outputFilepath")


class ScenarioRequestDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    scenario_name: str = Field(..., alias="scenarioName", max_length=100, min_length=0)


class StageRequestDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str
    length: int
    interest_rate: float | None = Field(None, alias="interestRate")
    inflation_rate: float | None = Field(None, alias="inflationRate")
    index: int


class StageResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str
    length: int
    interest_rate: float | None = Field(None, alias="interestRate")
    inflation_rate: float | None = Field(None, alias="inflationRate")
    index: int
    guid: UUID | None = None


class ResponseDtoListStageResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: list[StageResponseDto] | None = None
    status: Status | None = None


class HubRequestDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    hub_name: str = Field(..., alias="hubName", max_length=100, min_length=0)


class HubResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    hub_guid: str = Field(..., alias="hubGuid")
    hub_name: str = Field(..., alias="hubName")
    updated: AwareDatetime
    created: AwareDatetime


class ResponseDtoListFHubResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: list[HubResponseDto] | None = None
    status: Status | None = None


class SubType(StrEnum):
    electricity = "ELECTRICITY"
    electricity_renewable = "ELECTRICITY_RENEWABLE"
    wood_chips = "WOOD_CHIPS"
    wood_pellets = "WOOD_PELLETS"
    coal = "COAL"
    oil = "OIL"
    gas = "GAS"
    biogas = "BIOGAS"
    hydrogen = "HYDROGEN"
    hydrogen_pressurized = "HYDROGEN_PRESSURIZED"
    cooling_1 = "COOLING_1"
    cooling_2 = "COOLING_2"
    cooling_3 = "COOLING_3"
    cooling_4 = "COOLING_4"
    ice = "ICE"
    heat_1 = "HEAT_1"
    heat_2 = "HEAT_2"
    heat_3 = "HEAT_3"
    heat_4 = "HEAT_4"
    heat_5 = "HEAT_5"
    heat_6 = "HEAT_6"
    heat_7 = "HEAT_7"
    heat_8 = "HEAT_8"
    heat_9 = "HEAT_9"
    heat_ambient = "HEAT_AMBIENT"
    steam_low_pressure = "STEAM_LOW_PRESSURE"
    solar_roof = "SOLAR_ROOF"
    solar_facade = "SOLAR_FACADE"
    solar_parapet = "SOLAR_PARAPET"
    wind = "WIND"
    hydro = "HYDRO"
    biomass = "BIOMASS"
    geothermal = "GEOTHERMAL"
    tidal = "TIDAL"
    process_waste_heat = "PROCESS_WASTE_HEAT"
    custom = "CUSTOM"


class EnergyCarrierRequestDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    sub_type: SubType = Field(..., alias="subType")
    energy_carrier_name: str = Field(..., alias="energyCarrierName", max_length=100, min_length=0)
    color_hex_code: str | None = Field(None, alias="colorHexCode")
    allow_virtual_load: bool | None = Field(None, alias="allowVirtualLoad")


class Month(Enum):
    january = "JANUARY"
    february = "FEBRUARY"
    march = "MARCH"
    april = "APRIL"
    may = "MAY"
    june = "JUNE"
    july = "JULY"
    august = "AUGUST"
    september = "SEPTEMBER"
    october = "OCTOBER"
    november = "NOVEMBER"
    december = "DECEMBER"
    none_type_none = None


class CustomSeasonalityResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    month: Month | None = None
    value: float | None = None


class MustBeInstalledInHubs(StrEnum):
    can_be_installed = "canBeInstalled"
    must_be_installed = "mustBeInstalled"
    must_be_installed_in_at_least_one_hub = "mustBeInstalledInAtLeastOneHub"


class SeasonalOperation(StrEnum):
    all_seasons = "ALL_SEASONS"
    winter = "WINTER"
    non_winter = "NON_WINTER"
    summer = "SUMMER"
    non_summer = "NON_SUMMER"


class Type(StrEnum):
    input = "INPUT"
    output = "OUTPUT"


class CustomSeasonalityRequestDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    month: Month | None = None
    value: float | None = None


class AdvancedCostComponentRequestDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str
    value: float | None = None
    category: str | None = Field(
        None,
        pattern="FIXED_INVESTMENT_COSTS_CHF|VARIABLE_INVESTMENT_COSTS_CHF_KW|FIXED_OM_COSTS_CHF_YEAR|VARIABLE_OM_COSTS_CHF_KW_YEAR|VARIABLE_OM_COSTS_CHF_KWH|VARIABLE_OM_COSTS_PERCENT|NETWORK_RELATED_COST_CHF|PIPE|MEASUREMENT_CONTROL_REGULATION|PUMPS",
    )
    lifetime: float | None = Field(None, ge=0.0)
    interest_rate: float | None = Field(None, alias="interestRate", ge=0.0, le=100.0)
    length: float | None = None
    complexity_factor: float | None = Field(None, alias="complexityFactor")
    data_points: float | None = Field(None, alias="dataPoints")
    number_of_pumps: float | None = Field(None, alias="numberOfPumps")


class MustBeInstalledInHubs1(Enum):
    can_be_installed = "canBeInstalled"
    must_be_installed = "mustBeInstalled"
    must_be_installed_in_at_least_one_hub = "mustBeInstalledInAtLeastOneHub"
    none_type_none = None


class EnergyCarrierResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    energy_carrier_guid: str | None = Field(None, alias="energyCarrierGuid")
    type_key: str | None = Field(None, alias="typeKey")
    type_display_name: str | None = Field(None, alias="typeDisplayName")
    subtype_key: str | None = Field(None, alias="subtypeKey")
    subtype_display_name: str | None = Field(None, alias="subtypeDisplayName")
    energy_carrier_name: str | None = Field(None, alias="energyCarrierName")
    color_hex_code: str | None = Field(None, alias="colorHexCode")
    output_efficiency: float | None = Field(None, alias="outputEfficiency")
    fixed_input_share: float | None = Field(None, alias="fixedInputShare")
    custom_output_efficiency_activated: bool | None = Field(None, alias="customOutputEfficiencyActivated")
    custom_input_share_activated: bool | None = Field(None, alias="customInputShareActivated")
    custom_seasonality_values: list[CustomSeasonalityResponseDto] | None = Field(None, alias="customSeasonalityValues")
    input_share_profile_id: int | None = Field(None, alias="inputShareProfileId")
    output_efficiency_profile_id: int | None = Field(None, alias="outputEfficiencyProfileId")
    created: AwareDatetime | None = None
    primary: bool | None = None


class MustBeInstalledInHubs2(StrEnum):
    can_be_installed = "canBeInstalled"
    must_be_installed = "mustBeInstalled"
    must_be_installed_in_at_least_one_hub = "mustBeInstalledInAtLeastOneHub"


class AdvancedCostComponentResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str
    value: float | None = None
    category: str | None = Field(
        None,
        pattern="FIXED_INVESTMENT_COSTS_CHF|VARIABLE_INVESTMENT_COSTS_CHF_KW|FIXED_OM_COSTS_CHF_YEAR|VARIABLE_OM_COSTS_CHF_KW_YEAR|VARIABLE_OM_COSTS_CHF_KWH|VARIABLE_OM_COSTS_PERCENT|NETWORK_RELATED_COST_CHF|PIPE|MEASUREMENT_CONTROL_REGULATION|PUMPS",
    )
    lifetime: float | None = Field(None, ge=0.0)
    interest_rate: float | None = Field(None, alias="interestRate", ge=0.0, le=100.0)
    length: float | None = None
    complexity_factor: float | None = Field(None, alias="complexityFactor")
    data_points: float | None = Field(None, alias="dataPoints")
    number_of_pumps: float | None = Field(None, alias="numberOfPumps")
    guid: str | None = None
    category_id: str | None = Field(None, alias="categoryId")


class TypeOfCharging(Enum):
    smart = "Smart"
    dump = "Dump"
    v2_g = "V2G"
    none = "None"
    none_type_none = None


class LocalTime(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    hour: int | None = None
    minute: int | None = None
    second: int | None = None
    nano: int | None = None


class MustBeInstalled(StrEnum):
    can_be_installed = "canBeInstalled"
    must_be_installed = "mustBeInstalled"
    must_be_installed_in_at_least_one_hub = "mustBeInstalledInAtLeastOneHub"


class TechnologyPackageRequestDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    maximum_conversions: int | None = Field(None, alias="maximumConversions", ge=1)
    maximum_storages: int | None = Field(None, alias="maximumStorages", ge=1)
    must_be_installed: MustBeInstalled = Field(..., alias="mustBeInstalled")
    mutually_exclusive_group: str | None = Field(None, alias="mutuallyExclusiveGroup")
    name: str
    conversion_technologies: list[str] = Field(..., alias="conversionTechnologies")
    storage_technologies: list[str] = Field(..., alias="storageTechnologies")


class GuidNameDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    guid: str
    name: str


class TechnologyPackageResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str | None = None
    guid: str | None = None
    conversion_technologies: list[str] | None = Field(None, alias="conversionTechnologies")
    storage_technologies: list[str] | None = Field(None, alias="storageTechnologies")
    db_organization: str | None = Field(None, alias="dbOrganization")


class NetworkTechnologyRequestDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    fixed_investment_cost: float | None = Field(None, alias="fixedInvestmentCost", ge=0.0)
    variable_investment_cost: float | None = Field(None, alias="variableInvestmentCost", ge=0.0)
    fixed_om_cost_chf: float | None = Field(None, alias="fixedOmCostChf", ge=0.0)
    variable_om_cost_percent: float | None = Field(None, alias="variableOmCostPercent")
    variable_om_cost_year: float | None = Field(None, alias="variableOmCostYear", ge=0.0)
    variable_om_cost_ch_fk_wh: float | None = Field(None, alias="variableOmCostCHFkWh", ge=0.0)
    fixed_embodied_co2: float | None = Field(None, alias="fixedEmbodiedCo2", ge=0.0)
    variable_embodied_co2: float | None = Field(None, alias="variableEmbodiedCo2", ge=0.0)
    fixed_replacement_cost: float | None = Field(None, alias="fixedReplacementCost")
    variable_replacement_cost_percent: float | None = Field(None, alias="variableReplacementCostPercent")
    variable_replacement_cost_chf: float | None = Field(None, alias="variableReplacementCostCHF")
    fixed_salvage_value: float | None = Field(None, alias="fixedSalvageValue")
    variable_salvage_value_percent: float | None = Field(None, alias="variableSalvageValuePercent")
    variable_salvage_value_chf: float | None = Field(None, alias="variableSalvageValueCHF")
    network_technology_name: str = Field(..., alias="networkTechnologyName", max_length=100, min_length=0)
    lifetime: int
    energy_carrier_guid: str = Field(..., alias="energyCarrierGuid")
    cost_components: list[AdvancedCostComponentRequestDto] | None = Field(None, alias="costComponents")
    suggested: bool | None = None
    technology_category: str | None = Field(None, alias="technologyCategory")
    network_size: str | None = Field(None, alias="networkSize")
    notes: str | None = None
    source: str | None = None
    comes_from_db: str | None = Field(None, alias="comesFromDb")
    exchange_currency: str | None = Field(None, alias="exchangeCurrency", max_length=3, min_length=0)
    exchange_rate: float | None = Field(None, alias="exchangeRate", ge=0.0)
    stages: list[UUID]


class TechnologyCapacity(StrEnum):
    optimize = "optimize"
    specify = "specify"


class NetworkLinkRequestDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    installed_capacity: float | None = Field(None, alias="installedCapacity", ge=0.0)
    maximum_capacity: float | None = Field(None, alias="maximumCapacity", ge=0.0)
    name: str
    length: float = Field(..., ge=0.0)
    technology_capacity: TechnologyCapacity = Field(..., alias="technologyCapacity")
    uni_directional_flow: bool = Field(..., alias="uniDirectionalFlow")
    must_be_installed: bool = Field(..., alias="mustBeInstalled")
    node1_guid: str = Field(..., alias="node1Guid")
    node2_guid: str = Field(..., alias="node2Guid")
    network_technology_guid: str = Field(..., alias="networkTechnologyGuid")
    cost_components: list[AdvancedCostComponentRequestDto] | None = Field(None, alias="costComponents")
    minimum_capacity: float | None = Field(None, alias="minimumCapacity", ge=0.0)
    network_loss: float = Field(..., alias="networkLoss", ge=0.0)
    network_loss_profile_id: int | None = Field(None, alias="networkLossProfileId")


class NetworkLinkResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    installed_capacity: float | None = Field(None, alias="installedCapacity", ge=0.0)
    maximum_capacity: float | None = Field(None, alias="maximumCapacity", ge=0.0)
    network_link_guid: str | None = Field(None, alias="networkLinkGuid")
    name: str
    length: float
    technology_capacity: TechnologyCapacity = Field(..., alias="technologyCapacity")
    uni_directional_flow: bool = Field(..., alias="uniDirectionalFlow")
    must_be_installed: bool = Field(..., alias="mustBeInstalled")
    node1_guid: str = Field(..., alias="node1Guid")
    node1_name: str = Field(..., alias="node1Name")
    node2_guid: str = Field(..., alias="node2Guid")
    node2_name: str = Field(..., alias="node2Name")
    network_technology_name: str = Field(..., alias="networkTechnologyName")
    network_technology_guid: str = Field(..., alias="networkTechnologyGuid")
    cost_components: list[AdvancedCostComponentResponseDto] = Field(..., alias="costComponents")
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    minimum_capacity: float | None = Field(None, alias="minimumCapacity")
    network_loss: float = Field(..., alias="networkLoss")
    network_loss_profile_id: int | None = Field(None, alias="networkLossProfileId")


class ResponseDtoListNetworkLinkResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: list[NetworkLinkResponseDtoV2] | None = None
    status: Status | None = None


class TechnologyCapacity2(Enum):
    optimize = "optimize"
    specify = "specify"
    none_type_none = None


class NetworkLinkResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    network_link_guid: str | None = Field(None, alias="networkLinkGuid")
    length: float | None = None
    technology_capacity: TechnologyCapacity2 | None = Field(None, alias="technologyCapacity")
    installed_capacity: float | None = Field(None, alias="installedCapacity")
    uni_directional_flow: bool | None = Field(None, alias="uniDirectionalFlow")
    must_be_installed: bool | None = Field(None, alias="mustBeInstalled")
    node1_guid: str | None = Field(None, alias="node1Guid")
    node1_name: str | None = Field(None, alias="node1Name")
    node2_guid: str | None = Field(None, alias="node2Guid")
    node2_name: str | None = Field(None, alias="node2Name")
    network_technology_name: str | None = Field(None, alias="networkTechnologyName")
    network_technology_guid: str | None = Field(None, alias="networkTechnologyGuid")
    cost_components: list[AdvancedCostComponentResponseDto] | None = Field(None, alias="costComponents")
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None


class IntraHubNetworkLinkRequestDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str
    network_loss: float | None = Field(None, alias="networkLoss")
    fixed_embodied_co2: float | None = Field(None, alias="fixedEmbodiedCo2")
    input_energy_carrier_guid: str = Field(..., alias="inputEnergyCarrierGuid")
    output_energy_carrier_guid: str = Field(..., alias="outputEnergyCarrierGuid")
    hub_guids: list[str] = Field(..., alias="hubGuids")
    advanced_cost_components: list[AdvancedCostComponentRequestDto] | None = Field(None, alias="advancedCostComponents")
    stages: list[UUID]


class Type1(StrEnum):
    import_ = "IMPORT"
    export = "EXPORT"


class ImpexHubRequestDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    hub_guid: str = Field(..., alias="hubGuid")


class PriceCategory(StrEnum):
    energy_delivery = "ENERGY_DELIVERY"
    network_use = "NETWORK_USE"
    taxes = "TAXES"
    refunds_and_rebates = "REFUNDS_AND_REBATES"
    total = "TOTAL"


class PriceDimension(StrEnum):
    energy_price_chf_kwh = "ENERGY_PRICE_CHF_KWH"
    capacity_price_chf_kw_month = "CAPACITY_PRICE_CHF_KW_MONTH"
    capacity_price_chf_kw_year = "CAPACITY_PRICE_CHF_KW_YEAR"
    fixed_om_price_chf_year = "FIXED_OM_PRICE_CHF_YEAR"


class Type2(Enum):
    time_of_use = "TIME_OF_USE"
    fixed = "FIXED"
    none_type_none = None


class PriceCategoryId(Enum):
    energy_delivery = "ENERGY_DELIVERY"
    network_use = "NETWORK_USE"
    taxes = "TAXES"
    refunds_and_rebates = "REFUNDS_AND_REBATES"
    total = "TOTAL"
    none_type_none = None


class PriceDimensionId(Enum):
    energy_price_chf_kwh = "ENERGY_PRICE_CHF_KWH"
    capacity_price_chf_kw_month = "CAPACITY_PRICE_CHF_KW_MONTH"
    capacity_price_chf_kw_year = "CAPACITY_PRICE_CHF_KW_YEAR"
    fixed_om_price_chf_year = "FIXED_OM_PRICE_CHF_YEAR"
    none_type_none = None


class AdvancedPriceComponentRequestDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str
    value: float | None = None
    price_category: PriceCategory = Field(..., alias="priceCategory")
    price_dimension: PriceDimension = Field(..., alias="priceDimension")
    type: Type2 | None = None
    time_of_uses: list[str] | None = Field(None, alias="timeOfUses")
    price_category_id: PriceCategoryId | None = Field(None, alias="priceCategoryId")
    price_dimension_id: PriceDimensionId | None = Field(None, alias="priceDimensionId")


class TimeOfUseRequestDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str | None = None
    months: list[str] | None = None
    days: list[str] | None = None
    start_time: str | None = Field(None, alias="startTime")
    end_time: str | None = Field(None, alias="endTime")


class ImpexHubResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    hub_guid: str = Field(..., alias="hubGuid")
    hub_name: str = Field(..., alias="hubName")
    hub_updated: AwareDatetime = Field(..., alias="hubUpdated")
    hub_created: AwareDatetime = Field(..., alias="hubCreated")
    impex_guid: str | None = Field(None, alias="impexGuid")


class AdvancedPriceComponentResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str | None = None
    guid: str | None = None
    value: float | None = None
    price_category: str | None = Field(None, alias="priceCategory")
    price_category_id: PriceCategoryId | None = Field(None, alias="priceCategoryId")
    price_dimension: str | None = Field(None, alias="priceDimension")
    price_dimension_id: PriceDimensionId | None = Field(None, alias="priceDimensionId")
    type: Type2 | None = None
    time_of_uses: list[str] | None = Field(None, alias="timeOfUses")


class TimeOfUseResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str | None = None
    months: list[str] | None = None
    days: list[str] | None = None
    start_time: str | None = Field(None, alias="startTime")
    end_time: str | None = Field(None, alias="endTime")


class ResponseDtoStatus(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: Status | None = None
    status: Status | None = None


class ProfilePeriodValueDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    period: int
    demand_value: float = Field(..., alias="demandValue")


class ProfileResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: int | None = None
    name: str | None = None


class ResponseDtoListProfileResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: list[ProfileResponseDto] | None = None
    status: Status | None = None


class ProfileDetailsResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: int | None = None
    name: str
    values: list[ProfilePeriodValueDto]


class EnergyDemandRequestDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    hub_guids: list[str] = Field(..., alias="hubGuids")
    energy_carrier_guid: str = Field(..., alias="energyCarrierGuid")
    demand_profile_id: int = Field(..., alias="demandProfileId")
    demand_scaling_factor: float | None = Field(None, alias="demandScalingFactor")
    name: str = Field(..., max_length=100, min_length=0)
    demand_sale_price: float | None = Field(None, alias="demandSalePrice")
    demand_sale_price_profile_id: int | None = Field(None, alias="demandSalePriceProfileId")
    demand_sale_price_scaling_factor: float | None = Field(None, alias="demandSalePriceScalingFactor")
    stages: list[UUID]
    multiplication_factor: int | None = Field(None, alias="multiplicationFactor")
    reverse: bool | None = None


class EnergyDemandMetadataType(Enum):
    electricity = "ELECTRICITY"
    space_heating = "SPACE_HEATING"
    hot_water = "HOT_WATER"
    cooling = "COOLING"
    none_type_none = None


class EnergyDemandMetadataBuildingType(Enum):
    residence_mfh = "RESIDENCE_MFH"
    residence_sfh = "RESIDENCE_SFH"
    administration = "ADMINISTRATION"
    offices = "OFFICES"
    schools = "SCHOOLS"
    retail = "RETAIL"
    restaurant = "RESTAURANT"
    assembly = "ASSEMBLY"
    hospitals = "HOSPITALS"
    industry = "INDUSTRY"
    warehouse = "WAREHOUSE"
    sports_center = "SPORTS_CENTER"
    indoor_pool = "INDOOR_POOL"
    hotel = "HOTEL"
    industry_1_shift_fabricated_metals = "INDUSTRY_1_SHIFT_FABRICATED_METALS"
    industry_2_shift_fabricated_metals = "INDUSTRY_2_SHIFT_FABRICATED_METALS"
    industry_food_processing = "INDUSTRY_FOOD_PROCESSING"
    industry_general_manufacturer = "INDUSTRY_GENERAL_MANUFACTURER"
    industry_pharmaceutical = "INDUSTRY_PHARMACEUTICAL"
    industry_plastic_manufacturer = "INDUSTRY_PLASTIC_MANUFACTURER"
    industry_services = "INDUSTRY_SERVICES"
    industry_warehouse = "INDUSTRY_WAREHOUSE"
    none_type_none = None


class EnergyDemandMetadataBuildingAge(Enum):
    age_under_1970 = "AGE_UNDER_1970"
    age_1970_1980 = "AGE_1970_1980"
    age_1980_1995 = "AGE_1980_1995"
    age_1995_2005 = "AGE_1995_2005"
    age_2005_2015 = "AGE_2005_2015"
    age_over_2015 = "AGE_OVER_2015"
    sia_2024_existing_mfh = "SIA_2024_EXISTING_MFH"
    sia_2024_existing_sfh = "SIA_2024_EXISTING_SFH"
    sia_2024_existing_hotel_room = "SIA_2024_EXISTING_HOTEL_ROOM"
    sia_2024_existing_lobby = "SIA_2024_EXISTING_LOBBY"
    sia_2024_existing_single_group_office = "SIA_2024_EXISTING_SINGLE_GROUP_OFFICE"
    sia_2024_existing_open_plan_office = "SIA_2024_EXISTING_OPEN_PLAN_OFFICE"
    sia_2024_existing_meeting_room = "SIA_2024_EXISTING_MEETING_ROOM"
    sia_2024_existing_counter_hall = "SIA_2024_EXISTING_COUNTER_HALL"
    sia_2024_existing_class_room = "SIA_2024_EXISTING_CLASS_ROOM"
    sia_2024_existing_teachers_lounge = "SIA_2024_EXISTING_TEACHERS_LOUNGE"
    sia_2024_existing_library = "SIA_2024_EXISTING_LIBRARY"
    sia_2024_existing_auditorium = "SIA_2024_EXISTING_AUDITORIUM"
    sia_2024_existing_school_subject_room = "SIA_2024_EXISTING_SCHOOL_SUBJECT_ROOM"
    sia_2024_existing_food_sale_store = "SIA_2024_EXISTING_FOOD_SALE_STORE"
    sia_2024_existing_specialty_store = "SIA_2024_EXISTING_SPECIALTY_STORE"
    sia_2024_existing_sales_furniture_diy_garden = "SIA_2024_EXISTING_SALES_FURNITURE_DIY_GARDEN"
    sia_2024_existing_patient_room = "SIA_2024_EXISTING_PATIENT_ROOM"
    sia_2024_existing_ward_room = "SIA_2024_EXISTING_WARD_ROOM"
    sia_2024_existing_treatment_room = "SIA_2024_EXISTING_TREATMENT_ROOM"
    sia_2024_existing_warehouse = "SIA_2024_EXISTING_WAREHOUSE"
    sia_2024_existing_gymnasium = "SIA_2024_EXISTING_GYMNASIUM"
    sia_2024_existing_fitness_room = "SIA_2024_EXISTING_FITNESS_ROOM"
    sia_2024_existing_indoor_swimming_pool = "SIA_2024_EXISTING_INDOOR_SWIMMING_POOL"
    sia_2024_standard_mfh = "SIA_2024_STANDARD_MFH"
    sia_2024_standard_sfh = "SIA_2024_STANDARD_SFH"
    sia_2024_standard_hotel_room = "SIA_2024_STANDARD_HOTEL_ROOM"
    sia_2024_standard_lobby = "SIA_2024_STANDARD_LOBBY"
    sia_2024_standard_single_group_office = "SIA_2024_STANDARD_SINGLE_GROUP_OFFICE"
    sia_2024_standard_open_plan_office = "SIA_2024_STANDARD_OPEN_PLAN_OFFICE"
    sia_2024_standard_meeting_room = "SIA_2024_STANDARD_MEETING_ROOM"
    sia_2024_standard_counter_hall = "SIA_2024_STANDARD_COUNTER_HALL"
    sia_2024_standard_class_room = "SIA_2024_STANDARD_CLASS_ROOM"
    sia_2024_standard_teachers_lounge = "SIA_2024_STANDARD_TEACHERS_LOUNGE"
    sia_2024_standard_library = "SIA_2024_STANDARD_LIBRARY"
    sia_2024_standard_auditorium = "SIA_2024_STANDARD_AUDITORIUM"
    sia_2024_standard_school_subject_room = "SIA_2024_STANDARD_SCHOOL_SUBJECT_ROOM"
    sia_2024_standard_food_sale_store = "SIA_2024_STANDARD_FOOD_SALE_STORE"
    sia_2024_standard_specialty_store = "SIA_2024_STANDARD_SPECIALTY_STORE"
    sia_2024_standard_sales_furniture_diy_garden = "SIA_2024_STANDARD_SALES_FURNITURE_DIY_GARDEN"
    sia_2024_standard_patient_room = "SIA_2024_STANDARD_PATIENT_ROOM"
    sia_2024_standard_ward_room = "SIA_2024_STANDARD_WARD_ROOM"
    sia_2024_standard_treatment_room = "SIA_2024_STANDARD_TREATMENT_ROOM"
    sia_2024_standard_warehouse = "SIA_2024_STANDARD_WAREHOUSE"
    sia_2024_standard_gymnasium = "SIA_2024_STANDARD_GYMNASIUM"
    sia_2024_standard_fitness_room = "SIA_2024_STANDARD_FITNESS_ROOM"
    sia_2024_standard_indoor_swimming_pool = "SIA_2024_STANDARD_INDOOR_SWIMMING_POOL"
    sia_2024_target_mfh = "SIA_2024_TARGET_MFH"
    sia_2024_target_sfh = "SIA_2024_TARGET_SFH"
    sia_2024_target_hotel_room = "SIA_2024_TARGET_HOTEL_ROOM"
    sia_2024_target_lobby = "SIA_2024_TARGET_LOBBY"
    sia_2024_target_single_group_office = "SIA_2024_TARGET_SINGLE_GROUP_OFFICE"
    sia_2024_target_open_plan_office = "SIA_2024_TARGET_OPEN_PLAN_OFFICE"
    sia_2024_target_meeting_room = "SIA_2024_TARGET_MEETING_ROOM"
    sia_2024_target_counter_hall = "SIA_2024_TARGET_COUNTER_HALL"
    sia_2024_target_class_room = "SIA_2024_TARGET_CLASS_ROOM"
    sia_2024_target_teachers_lounge = "SIA_2024_TARGET_TEACHERS_LOUNGE"
    sia_2024_target_library = "SIA_2024_TARGET_LIBRARY"
    sia_2024_target_auditorium = "SIA_2024_TARGET_AUDITORIUM"
    sia_2024_target_school_subject_room = "SIA_2024_TARGET_SCHOOL_SUBJECT_ROOM"
    sia_2024_target_food_sale_store = "SIA_2024_TARGET_FOOD_SALE_STORE"
    sia_2024_target_specialty_store = "SIA_2024_TARGET_SPECIALTY_STORE"
    sia_2024_target_sales_furniture_diy_garden = "SIA_2024_TARGET_SALES_FURNITURE_DIY_GARDEN"
    sia_2024_target_patient_room = "SIA_2024_TARGET_PATIENT_ROOM"
    sia_2024_target_ward_room = "SIA_2024_TARGET_WARD_ROOM"
    sia_2024_target_treatment_room = "SIA_2024_TARGET_TREATMENT_ROOM"
    sia_2024_target_warehouse = "SIA_2024_TARGET_WAREHOUSE"
    sia_2024_target_gymnasium = "SIA_2024_TARGET_GYMNASIUM"
    sia_2024_target_fitness_room = "SIA_2024_TARGET_FITNESS_ROOM"
    sia_2024_target_indoor_swimming_pool = "SIA_2024_TARGET_INDOOR_SWIMMING_POOL"
    minergie_new_construction = "MINERGIE_NEW_CONSTRUCTION"
    minergie_renovation = "MINERGIE_RENOVATION"
    minergie_a = "MINERGIE_A"
    minergie_p_new_construction = "MINERGIE_P_NEW_CONSTRUCTION"
    minergie_p_renovation = "MINERGIE_P_RENOVATION"
    others = "OTHERS"
    none_type_none = None


class EnergyDemandMetadataOption(Enum):
    option_1 = "OPTION_1"
    option_2 = "OPTION_2"
    option_3 = "OPTION_3"
    none_type_none = None


class EnergyDemandResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    energy_demand_guid: str | None = Field(None, alias="energyDemandGuid")
    energy_carrier_name: str = Field(..., alias="energyCarrierName")
    hubs: list[HubResponseDto]
    energy_demand_name: str = Field(..., alias="energyDemandName")
    energy_carrier_guid: str = Field(..., alias="energyCarrierGuid")
    demand_sale_price: float | None = Field(None, alias="demandSalePrice")
    stages: list[UUID]
    demand_profile_id: int = Field(..., alias="demandProfileId")
    demand_scaling_factor: float | None = Field(None, alias="demandScalingFactor")
    demand_sale_price_profile_id: int | None = Field(None, alias="demandSalePriceProfileId")
    demand_sale_price_scaling_factor: float | None = Field(None, alias="demandSalePriceScalingFactor")
    energy_demand_user_saved_metadata_guid: str | None = Field(None, alias="energyDemandUserSavedMetadataGuid")
    energy_demand_user_saved_metadata_name: str | None = Field(None, alias="energyDemandUserSavedMetadataName")
    energy_demand_user_saved_metadata_reference_area: float | None = Field(None, alias="energyDemandUserSavedMetadataReferenceArea")
    scaling_factor: float | None = Field(None, alias="scalingFactor")
    energy_demand_metadata_guid: str | None = Field(None, alias="energyDemandMetadataGuid")
    energy_demand_metadata_name: str | None = Field(None, alias="energyDemandMetadataName")
    energy_demand_metadata_db_organization: str | None = Field(None, alias="energyDemandMetadataDbOrganization")
    energy_demand_metadata_type: EnergyDemandMetadataType | None = Field(None, alias="energyDemandMetadataType")
    energy_demand_metadata_building_type: EnergyDemandMetadataBuildingType | None = Field(None, alias="energyDemandMetadataBuildingType")
    energy_demand_metadata_building_age: EnergyDemandMetadataBuildingAge | None = Field(None, alias="energyDemandMetadataBuildingAge")
    energy_demand_metadata_option: EnergyDemandMetadataOption | None = Field(None, alias="energyDemandMetadataOption")
    energy_demand_metadata_referenced_area_m2: float | None = Field(None, alias="energyDemandMetadataReferencedAreaM2")
    energy_demand_metadata_specific_energy_demand_value_k_wh_m2: float | None = Field(
        None, alias="energyDemandMetadataSpecificEnergyDemandValueKWhM2"
    )
    energy_demand_metadata_total_annual_demand: float | None = Field(None, alias="energyDemandMetadataTotalAnnualDemand")
    multiplication_factor_preview: int | None = Field(None, alias="multiplicationFactorPreview")
    multiplication_factor: int | None = Field(None, alias="multiplicationFactor")
    reverse: bool


class ResponseDtoListEnergyDemandResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: list[EnergyDemandResponseDtoV2] | None = None
    status: Status | None = None


class EnergyDemandDetailResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    energy_demand_guid: str | None = Field(None, alias="energyDemandGuid")
    energy_demand_name: str | None = Field(None, alias="energyDemandName")
    energy_carrier_guid: str | None = Field(None, alias="energyCarrierGuid")
    energy_carrier_name: str | None = Field(None, alias="energyCarrierName")
    hubs: list[HubResponseDto] | None = None
    demand_sale_price: float | None = Field(None, alias="demandSalePrice")
    stages: list[UUID] | None = None
    demand_profile_id: int | None = Field(None, alias="demandProfileId")
    demand_scaling_factor: float | None = Field(None, alias="demandScalingFactor")
    demand_sale_price_profile_id: int | None = Field(None, alias="demandSalePriceProfileId")
    demand_sale_price_scaling_factor: float | None = Field(None, alias="demandSalePriceScalingFactor")
    energy_demand_user_saved_metadata_guid: str | None = Field(None, alias="energyDemandUserSavedMetadataGuid")
    energy_demand_user_saved_metadata_name: str | None = Field(None, alias="energyDemandUserSavedMetadataName")
    energy_demand_user_saved_metadata_reference_area: float | None = Field(None, alias="energyDemandUserSavedMetadataReferenceArea")
    scaling_factor: float | None = Field(None, alias="scalingFactor")
    energy_demand_metadata_guid: str | None = Field(None, alias="energyDemandMetadataGuid")
    energy_demand_metadata_name: str | None = Field(None, alias="energyDemandMetadataName")
    energy_demand_metadata_db_organization: str | None = Field(None, alias="energyDemandMetadataDbOrganization")
    energy_demand_metadata_type: EnergyDemandMetadataType | None = Field(None, alias="energyDemandMetadataType")
    energy_demand_metadata_building_type: EnergyDemandMetadataBuildingType | None = Field(None, alias="energyDemandMetadataBuildingType")
    energy_demand_metadata_building_age: EnergyDemandMetadataBuildingAge | None = Field(None, alias="energyDemandMetadataBuildingAge")
    energy_demand_metadata_option: EnergyDemandMetadataOption | None = Field(None, alias="energyDemandMetadataOption")
    energy_demand_metadata_referenced_area_m2: float | None = Field(None, alias="energyDemandMetadataReferencedAreaM2")
    energy_demand_metadata_specific_energy_demand_value_k_wh_m2: float | None = Field(
        None, alias="energyDemandMetadataSpecificEnergyDemandValueKWhM2"
    )
    energy_demand_metadata_total_annual_demand: float | None = Field(None, alias="energyDemandMetadataTotalAnnualDemand")
    multiplication_factor_preview: int | None = Field(None, alias="multiplicationFactorPreview")
    multiplication_factor: int | None = Field(None, alias="multiplicationFactor")
    reverse: bool | None = None


class EnergyDemandResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    energy_demand_guid: str | None = Field(None, alias="energyDemandGuid")
    energy_carrier_name: str | None = Field(None, alias="energyCarrierName")
    hub_name: str | None = Field(None, alias="hubName")
    energy_demand_name: str | None = Field(None, alias="energyDemandName")
    energy_carrier_guid: str | None = Field(None, alias="energyCarrierGuid")
    hub_guid: str | None = Field(None, alias="hubGuid")
    demand_sale_price: float | None = Field(None, alias="demandSalePrice")
    energy_demand_user_saved_metadata_guid: str | None = Field(None, alias="energyDemandUserSavedMetadataGuid")
    energy_demand_user_saved_metadata_name: str | None = Field(None, alias="energyDemandUserSavedMetadataName")
    energy_demand_user_saved_metadata_reference_area: float | None = Field(None, alias="energyDemandUserSavedMetadataReferenceArea")
    scaling_factor: float | None = Field(None, alias="scalingFactor")
    energy_demand_metadata_guid: str | None = Field(None, alias="energyDemandMetadataGuid")
    energy_demand_metadata_name: str | None = Field(None, alias="energyDemandMetadataName")
    energy_demand_metadata_db_organization: str | None = Field(None, alias="energyDemandMetadataDbOrganization")
    energy_demand_metadata_type: EnergyDemandMetadataType | None = Field(None, alias="energyDemandMetadataType")
    energy_demand_metadata_building_type: EnergyDemandMetadataBuildingType | None = Field(None, alias="energyDemandMetadataBuildingType")
    energy_demand_metadata_building_age: EnergyDemandMetadataBuildingAge | None = Field(None, alias="energyDemandMetadataBuildingAge")
    energy_demand_metadata_option: EnergyDemandMetadataOption | None = Field(None, alias="energyDemandMetadataOption")
    energy_demand_metadata_referenced_area_m2: float | None = Field(None, alias="energyDemandMetadataReferencedAreaM2")
    energy_demand_metadata_specific_energy_demand_value_k_wh_m2: float | None = Field(
        None, alias="energyDemandMetadataSpecificEnergyDemandValueKWhM2"
    )
    energy_demand_metadata_total_annual_demand: float | None = Field(None, alias="energyDemandMetadataTotalAnnualDemand")
    multiplication_factor_preview: int | None = Field(None, alias="multiplicationFactorPreview")
    multiplication_factor: int | None = Field(None, alias="multiplicationFactor")


class AvailableResourceType(StrEnum):
    area = "Area"
    generic = "Generic"
    power = "Power"


class SolarOnSiteResourcesHubRequestDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    hub_guid: str = Field(..., alias="hubGuid")
    available_solar_collector_area: float = Field(..., alias="availableSolarCollectorArea", gt=0.0)
    available_resource_type: AvailableResourceType = Field(..., alias="availableResourceType")


class IrradianceProfileType(StrEnum):
    generated = "GENERATED"
    uploaded = "UPLOADED"
    saved = "SAVED"


class HubSolarOnSiteResourceResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    hub_name: str = Field(..., alias="hubName")
    hub_guid: str = Field(..., alias="hubGuid")
    available_solar_collector_area: float = Field(..., alias="availableSolarCollectorArea")
    available_resource_type: AvailableResourceType = Field(..., alias="availableResourceType")


class IrradianceProfileType1(Enum):
    generated = "GENERATED"
    uploaded = "UPLOADED"
    saved = "SAVED"
    none_type_none = None


class HubSolarOnSiteResourceResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    hub_name: str | None = Field(None, alias="hubName")
    hub_guid: str | None = Field(None, alias="hubGuid")
    available_solar_collector_area: float | None = Field(None, alias="availableSolarCollectorArea")
    available_resource_type: str | None = Field(None, alias="availableResourceType")
    technology_dimensioning_std_value: float | None = Field(None, alias="technologyDimensioningStdValue")


class ResponseDtoListHubResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: list[HubResponseDto] | None = None
    status: Status | None = None


class AppException(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    detail: str = Field(..., title="Detail")


class Auth0UserAccessToken(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    access_token: str = Field(..., title="Access Token")
    token_type: str = Field(..., title="Token Type")
    expires_in: int = Field(..., title="Expires In")


class Auth0UserCredentials(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    email: str = Field(..., title="Email")
    password: str = Field(..., title="Password")


class AwsRegion(StrEnum):
    eu_north_1 = "eu-north-1"
    eu_central_2 = "eu-central-2"


class BillingCycle(StrEnum):
    monthly = "MONTHLY"
    quarterly = "QUARTERLY"
    annually = "ANNUALLY"


class GetOrganizationExt(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str = Field(..., title="Name")
    gis_on: bool | None = Field(False, alias="gisOn", title="Gison")
    sep_on: bool | None = Field(False, alias="sepOn", title="Sepon")
    sep_buildings_limit: int | None = Field(0, alias="sepBuildingsLimit", title="Sepbuildingslimit")
    execution_slots: int | None = Field(0, alias="executionSlots", title="Executionslots")
    variable_billing: bool | None = Field(False, alias="variableBilling", title="Variablebilling")
    max_executions: int | None = Field(None, alias="maxExecutions", title="Maxexecutions")
    max_simultaneous_executions: int | None = Field(None, alias="maxSimultaneousExecutions", title="Maxsimultaneousexecutions")
    max_execution_time: int | None = Field(None, alias="maxExecutionTime", title="Maxexecutiontime")
    max_execution_time_week: int | None = Field(None, alias="maxExecutionTimeWeek", title="Maxexecutiontimeweek")
    number_of_executions_left: int | None = Field(None, alias="numberOfExecutionsLeft", title="Numberofexecutionsleft")
    execution_time_week_left: int | None = Field(None, alias="executionTimeWeekLeft", title="Executiontimeweekleft")
    id: UUID4 = Field(..., title="Id")
    created: AwareDatetime = Field(..., title="Created")
    updated: AwareDatetime = Field(..., title="Updated")
    sep_buildings_consumed: int | None = Field(0, alias="sepBuildingsConsumed", title="Sepbuildingsconsumed")


class GetPlanExt(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    intra_hub_network: bool | None = Field(False, alias="intraHubNetwork", title="Intrahubnetwork")
    advanced_cost_components: bool | None = Field(False, alias="advancedCostComponents", title="Advancedcostcomponents")
    unit_commitment: bool | None = Field(False, alias="unitCommitment", title="Unitcommitment")
    max_energy_carriers_per_hub: int | None = Field(None, alias="maxEnergyCarriersPerHub", title="Maxenergycarriersperhub")
    max_energy_demands: int | None = Field(None, alias="maxEnergyDemands", title="Maxenergydemands")
    max_hubs: int | None = Field(None, alias="maxHubs", title="Maxhubs")
    max_stages: int | None = Field(1, alias="maxStages", le=8, title="Maxstages")
    max_solar_resources: int | None = Field(None, alias="maxSolarResources", title="Maxsolarresources")
    max_other_resources: int | None = Field(None, alias="maxOtherResources", title="Maxotherresources")
    max_imports: int | None = Field(None, alias="maxImports", title="Maximports")
    max_exports: int | None = Field(None, alias="maxExports", title="Maxexports")
    max_conversion_techs: int | None = Field(None, alias="maxConversionTechs", title="Maxconversiontechs")
    max_conversion_modes: int | None = Field(None, alias="maxConversionModes", title="Maxconversionmodes")
    max_storage_techs: int | None = Field(None, alias="maxStorageTechs", title="Maxstoragetechs")
    max_network_techs: int | None = Field(None, alias="maxNetworkTechs", title="Maxnetworktechs")
    max_network_links: int | None = Field(None, alias="maxNetworkLinks", title="Maxnetworklinks")
    max_executions: int | None = Field(None, alias="maxExecutions", title="Maxexecutions")
    max_simultaneous_executions: int | None = Field(None, alias="maxSimultaneousExecutions", title="Maxsimultaneousexecutions")
    max_execution_time: int | None = Field(None, alias="maxExecutionTime", title="Maxexecutiontime")
    max_execution_time_week: int | None = Field(None, alias="maxExecutionTimeWeek", title="Maxexecutiontimeweek")
    max_execution_history: int | None = Field(100, alias="maxExecutionHistory", le=500, title="Maxexecutionhistory")
    max_pareto_points: int | None = Field(9, alias="maxParetoPoints", le=9, title="Maxparetopoints")
    full_temporal_resolution: bool | None = Field(False, alias="fullTemporalResolution", title="Fulltemporalresolution")
    max_projects: int | None = Field(None, alias="maxProjects", title="Maxprojects")
    max_analyses: int | None = Field(None, alias="maxAnalyses", title="Maxanalyses")
    max_scenarios: int | None = Field(None, alias="maxScenarios", title="Maxscenarios")
    share_project: bool | None = Field(False, alias="shareProject", title="Shareproject")
    organization_db: bool | None = Field(False, alias="organizationDb", title="Organizationdb")
    scenario_variants: bool | None = Field(False, alias="scenarioVariants", title="Scenariovariants")
    max_scenario_variants: int | None = Field(None, alias="maxScenarioVariants", title="Maxscenariovariants")
    name: str = Field(..., title="Name")
    id: UUID4 = Field(..., title="Id")
    created: AwareDatetime = Field(..., title="Created")
    updated: AwareDatetime | None = Field(..., title="Updated")
    sagemaker_on: bool = Field(..., alias="sagemakerOn", title="Sagemakeron")
    sagemaker_regions: list[AwsRegion] = Field(..., alias="sagemakerRegions", title="Sagemakerregions")


class GetSubscriptionExt(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str = Field(..., title="Name")
    organization_id: UUID4 = Field(..., alias="organizationId", title="Organizationid")
    start_date: date = Field(..., alias="startDate", title="Startdate")
    end_date: date | None = Field(None, alias="endDate", title="Enddate")
    billing_cycle: BillingCycle | None = Field(None, alias="billingCycle")
    next_billing_date: date | None = Field(None, alias="nextBillingDate", title="Nextbillingdate")
    variable_billing: bool | None = Field(False, alias="variableBilling", title="Variablebilling")
    execution_priority: int | None = Field(0, alias="executionPriority", title="Executionpriority")
    max_simultaneous_executions: int | None = Field(None, alias="maxSimultaneousExecutions", title="Maxsimultaneousexecutions")
    max_executions_per_cycle: int | None = Field(None, alias="maxExecutionsPerCycle", title="Maxexecutionspercycle")
    max_execution_time_per_cycle: int | None = Field(None, alias="maxExecutionTimePerCycle", title="Maxexecutiontimepercycle")
    max_executions_per_week: int | None = Field(None, alias="maxExecutionsPerWeek", title="Maxexecutionsperweek")
    max_execution_time_per_week: int | None = Field(None, alias="maxExecutionTimePerWeek", title="Maxexecutiontimeperweek")
    user_max_executions_per_cycle: int | None = Field(None, alias="userMaxExecutionsPerCycle", title="Usermaxexecutionspercycle")
    user_max_execution_time_per_cycle: int | None = Field(None, alias="userMaxExecutionTimePerCycle", title="Usermaxexecutiontimepercycle")
    user_max_executions_per_week: int | None = Field(None, alias="userMaxExecutionsPerWeek", title="Usermaxexecutionsperweek")
    user_max_execution_time_per_week: int | None = Field(None, alias="userMaxExecutionTimePerWeek", title="Usermaxexecutiontimeperweek")
    id: UUID4 = Field(..., title="Id")
    created: AwareDatetime = Field(..., title="Created")
    updated: AwareDatetime = Field(..., title="Updated")


class Language(StrEnum):
    english = "English"
    german = "German"


class Preferences(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    exchange_currency_default: str = Field(..., alias="exchangeCurrencyDefault", title="Exchangecurrencydefault")
    unit_system_default: str = Field(..., alias="unitSystemDefault", title="Unitsystemdefault")
    language_default: Language = Field(..., alias="languageDefault")
    interest_rate_default: float | None = Field(None, alias="interestRateDefault", title="Interestratedefault")
    first_name: str | None = Field(None, alias="firstName", title="Firstname")
    last_name: str | None = Field(None, alias="lastName", title="Lastname")
    created: AwareDatetime = Field(..., title="Created")
    updated: AwareDatetime = Field(..., title="Updated")


class User(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    email: str = Field(..., title="Email")
    plan_limitation_id: UUID4 = Field(..., alias="planLimitationId", title="Planlimitationid")
    organization_id: UUID4 = Field(..., alias="organizationId", title="Organizationid")
    subscription_id: UUID4 = Field(..., alias="subscriptionId", title="Subscriptionid")
    plan_expiry: date | None = Field(None, alias="planExpiry", title="Planexpiry")
    number_of_executions_left: int | None = Field(None, alias="numberOfExecutionsLeft", title="Numberofexecutionsleft")
    execution_time_week_left: int | None = Field(None, alias="executionTimeWeekLeft", title="Executiontimeweekleft")
    mfa: bool | None = Field(False, title="Mfa")
    deactivated: bool | None = Field(False, title="Deactivated")
    superuser: bool | None = Field(False, title="Superuser")
    admin: bool | None = Field(False, title="Admin")
    show_maintenance_info: bool | None = Field(False, alias="showMaintenanceInfo", title="Showmaintenanceinfo")
    show_gtc: bool | None = Field(False, alias="showGtc", title="Showgtc")
    show_user_guide: bool | None = Field(False, alias="showUserGuide", title="Showuserguide")
    account_guid: str = Field(..., alias="accountGuid", title="Accountguid")
    created: AwareDatetime = Field(..., title="Created")
    updated: AwareDatetime = Field(..., title="Updated")


class ValidationError(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    loc: list[str | int] = Field(..., title="Location")
    msg: str = Field(..., title="Message")
    type: str = Field(..., title="Error Type")
    input: Any | None = Field(None, title="Input")
    ctx: dict[str, Any] | None = Field(None, title="Context")


class CustomHTTPException(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    detail: str = Field(..., title="Detail")


class GetScenarioGuidsPage(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    scenario_guids: list[str] = Field(..., alias="scenarioGuids", title="Scenarioguids")
    limit: int | None = Field(200, title="Limit")


class InputFile(RootModel[AnyUrl]):
    root: AnyUrl = Field(..., title="Inputfile")


class OutputFile(RootModel[AnyUrl]):
    root: AnyUrl = Field(..., title="Outputfile")


class JobStatus(StrEnum):
    validating = "VALIDATING"
    valid = "VALID"
    pending = "PENDING"
    queued = "QUEUED"
    running = "RUNNING"
    done = "DONE"
    stopped = "STOPPED"
    failed = "FAILED"
    invalid = "INVALID"


class ObjectiveFunction(StrEnum):
    min_life_cycle_cost = "MIN_LIFE_CYCLE_COST"
    min_annualized_cost = "MIN_ANNUALIZED_COST"
    min_co2_emissions = "MIN_CO2_EMISSIONS"
    min_investment = "MIN_INVESTMENT"
    min_om = "MIN_OM"
    min_fuel_imports = "MIN_FUEL_IMPORTS"
    min_replacement = "MIN_REPLACEMENT"
    max_exports = "MAX_EXPORTS"
    max_salvage = "MAX_SALVAGE"


class SubscriptionUsage(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    total_count_overage: int = Field(..., alias="totalCountOverage", title="Totalcountoverage")
    total_minutes_overage: int = Field(..., alias="totalMinutesOverage", title="Totalminutesoverage")
    weekly_count_overage: int = Field(..., alias="weeklyCountOverage", title="Weeklycountoverage")
    weekly_minutes_overage: int = Field(..., alias="weeklyMinutesOverage", title="Weeklyminutesoverage")
    total_count: int = Field(..., alias="totalCount", title="Totalcount")
    total_minutes: int = Field(..., alias="totalMinutes", title="Totalminutes")
    current_week_count: int = Field(..., alias="currentWeekCount", title="Currentweekcount")
    current_week_minutes: int = Field(..., alias="currentWeekMinutes", title="Currentweekminutes")


class TemporalResolution(StrEnum):
    low = "LOW"
    medium = "MEDIUM"
    high = "HIGH"
    full = "FULL"


class UserUsage(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    total_count: int = Field(..., alias="totalCount", title="Totalcount")
    total_minutes: int = Field(..., alias="totalMinutes", title="Totalminutes")
    current_week_count: int = Field(..., alias="currentWeekCount", title="Currentweekcount")
    current_week_minutes: int = Field(..., alias="currentWeekMinutes", title="Currentweekminutes")
    history_count: int | None = Field(0, alias="historyCount", title="Historycount")


class ProjectResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    project_name: str | None = Field(None, alias="projectName")
    project_guid: str | None = Field(None, alias="projectGuid")
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    cover_image: str | None = Field(None, alias="coverImage")
    project_owner_email: str | None = Field(None, alias="projectOwnerEmail")
    secondary_owners: list[SecondaryOwnerDto] | None = Field(None, alias="secondaryOwners")
    lock_user_email: str | None = Field(None, alias="lockUserEmail")
    lock: bool | None = None
    lock_time: AwareDatetime | None = Field(None, alias="lockTime")
    owned_by_current_user: bool | None = Field(None, alias="ownedByCurrentUser")
    editable_by_current_user: bool | None = Field(None, alias="editableByCurrentUser")
    original_default_project_guid: str | None = Field(None, alias="originalDefaultProjectGuid")
    version: Version1 | None = None
    favorite: bool | None = None
    gis_centroid_x: float | None = Field(None, alias="gisCentroidX")
    gis_centroid_y: float | None = Field(None, alias="gisCentroidY")
    zoom_extent_xmin: float | None = Field(None, alias="zoomExtentXmin")
    zoom_extent_ymin: float | None = Field(None, alias="zoomExtentYmin")
    zoom_extent_xmax: float | None = Field(None, alias="zoomExtentXmax")
    zoom_extent_ymax: float | None = Field(None, alias="zoomExtentYmax")
    processing: bool | None = None


class ProjectSummaryResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    projects: list[ProjectResponseDto] | None = None


class ScenarioResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    scenario_guid: str | None = Field(None, alias="scenarioGuid")
    scenario_name: str | None = Field(None, alias="scenarioName")
    updated: AwareDatetime | None = None
    ready_for_execution: bool | None = Field(None, alias="readyForExecution")
    preparing_execution_v2: bool | None = Field(None, alias="preparingExecutionV2")
    master_scenario_guid: str | None = Field(None, alias="masterScenarioGuid")
    project_guid: str | None = Field(None, alias="projectGuid")
    project_name: str | None = Field(None, alias="projectName")
    analysis_guid: str | None = Field(None, alias="analysisGuid")
    analysis_name: str | None = Field(None, alias="analysisName")
    enymap: ScenarioEnymapResponseDto | None = None
    variant: bool | None = None


class ResultsResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    execution_submitted: AwareDatetime | None = Field(None, alias="executionSubmitted")
    scenarios: list[ResultsScenarioResponseDto] | None = None
    dashboard_url: str | None = Field(None, alias="dashboardUrl")


class ResponseDtoScenarioResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: ScenarioResponseDto | None = None
    status: Status | None = None


class ResponseDtoListFScenarioResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: list[ScenarioResponseDto] | None = None
    status: Status | None = None


class ResponseDtoStageResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: StageResponseDto | None = None
    status: Status | None = None


class ResponseDtoHubResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: HubResponseDto | None = None
    status: Status | None = None


class EnergyCarrierResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    energy_carrier_guid: str = Field(..., alias="energyCarrierGuid")
    type_key: str = Field(..., alias="typeKey")
    type_display_name: str = Field(..., alias="typeDisplayName")
    subtype_key: str = Field(..., alias="subtypeKey")
    subtype_display_name: str = Field(..., alias="subtypeDisplayName")
    energy_carrier_name: str = Field(..., alias="energyCarrierName")
    color_hex_code: str = Field(..., alias="colorHexCode")
    fixed_input_share: float | None = Field(None, alias="fixedInputShare")
    output_efficiency: float | None = Field(None, alias="outputEfficiency")
    custom_output_efficiency_activated: bool = Field(..., alias="customOutputEfficiencyActivated")
    custom_input_efficiency_activated: bool = Field(..., alias="customInputEfficiencyActivated")
    custom_seasonality_values: list[CustomSeasonalityResponseDto] | None = Field(None, alias="customSeasonalityValues")
    output_efficiency_profile_id: int | None = Field(None, alias="outputEfficiencyProfileId")
    created: AwareDatetime
    primary: bool | None = None


class EnergyCarriersListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    energy_carriers: list[EnergyCarrierResponseDto] | None = Field(None, alias="energyCarriers")


class ConversionCarrierRequestDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    energy_carrier_guid: str = Field(..., alias="energyCarrierGuid")
    fixed_input_share: float = Field(..., alias="fixedInputShare", ge=0.0)
    output_efficiency: float = Field(..., alias="outputEfficiency", ge=0.0)
    custom_input_share_activated: bool | None = Field(None, alias="customInputShareActivated")
    custom_output_efficiency_activated: bool | None = Field(None, alias="customOutputEfficiencyActivated")
    input_share_profile_id: int | None = Field(None, alias="inputShareProfileId")
    output_efficiency_profile_id: int | None = Field(None, alias="outputEfficiencyProfileId")
    custom_seasonality_values: list[CustomSeasonalityRequestDto] | None = Field(None, alias="customSeasonalityValues")
    type: Type
    primary: bool


class TechnologyModeResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    capacity: float | None = Field(None, ge=0.0)
    minimum_annual_output: float | None = Field(None, alias="minimumAnnualOutput", ge=0.0)
    maximum_annual_output: float | None = Field(None, alias="maximumAnnualOutput", ge=0.0)
    curtailment_limitation: float | None = Field(None, alias="curtailmentLimitation", ge=0.0)
    peak_power: float | None = Field(None, alias="peakPower")
    min_part_load: float | None = Field(None, alias="minPartLoad", ge=0.0, le=100.0)
    minimum_up_time: int | None = Field(None, alias="minimumUpTime", ge=1, le=8760)
    minimum_down_time: int | None = Field(None, alias="minimumDownTime", ge=1, le=8760)
    technology_mode_guid: str | None = Field(None, alias="technologyModeGuid")
    input_energy_carriers: list[EnergyCarrierResponseDtoV2] | None = Field(None, alias="inputEnergyCarriers")
    output_energy_carriers: list[EnergyCarrierResponseDtoV2] | None = Field(None, alias="outputEnergyCarriers")
    seasonal_operation_name: str | None = Field(None, alias="seasonalOperationName")
    seasonal_operation_value: str | None = Field(None, alias="seasonalOperationValue")
    allowed_operation_profile_id: int | None = Field(None, alias="allowedOperationProfileId")
    primary: bool | None = None
    maximum_capacity: float | None = Field(None, alias="maximumCapacity")
    minimum_capacity: float | None = Field(None, alias="minimumCapacity")
    simultaneous_operation: bool | None = Field(None, alias="simultaneousOperation")


class ConversionTechnologyDetailResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    fixed_investment_cost: float | None = Field(None, alias="fixedInvestmentCost", ge=0.0)
    fixed_om_cost_chf: float | None = Field(None, alias="fixedOmCostChf", ge=0.0)
    variable_om_cost_percent: float | None = Field(None, alias="variableOmCostPercent")
    variable_om_cost_year: float | None = Field(None, alias="variableOmCostYear", ge=0.0)
    variable_om_cost: float | None = Field(None, alias="variableOmCost", ge=0.0)
    fixed_embodied_co2: float | None = Field(None, alias="fixedEmbodiedCo2", ge=0.0)
    variable_embodied_co2: float | None = Field(None, alias="variableEmbodiedCo2", ge=0.0)
    variable_emitted_co2: float | None = Field(None, alias="variableEmittedCo2", ge=0.0)
    variable_captured_co2: float | None = Field(None, alias="variableCapturedCo2", ge=0.0)
    fixed_replacement_cost: float | None = Field(None, alias="fixedReplacementCost", ge=0.0)
    variable_replacement_cost_percent: float | None = Field(None, alias="variableReplacementCostPercent", ge=0.0)
    variable_replacement_cost_chf: float | None = Field(None, alias="variableReplacementCostCHF", ge=0.0)
    fixed_salvage_value: float | None = Field(None, alias="fixedSalvageValue", ge=0.0)
    variable_salvage_value_percent: float | None = Field(None, alias="variableSalvageValuePercent", ge=0.0)
    variable_salvage_value_chf: float | None = Field(None, alias="variableSalvageValueCHF", ge=0.0)
    must_be_installed_in_hubs: MustBeInstalledInHubs2 = Field(..., alias="mustBeInstalledInHubs")
    conversion_technology_guid: str | None = Field(None, alias="conversionTechnologyGuid")
    process_name: str = Field(..., alias="processName")
    exchange_currency: str | None = Field(None, alias="exchangeCurrency")
    exchange_rate: float | None = Field(None, alias="exchangeRate")
    variable_investment_cost: float | None = Field(None, alias="variableInvestmentCost")
    lifetime: float
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    hubs: list[HubResponseDto]
    technology_modes: list[TechnologyModeResponseDtoV2] | None = Field(None, alias="technologyModes")
    category: str | None = None
    technology_category: str | None = Field(None, alias="technologyCategory")
    mutually_exclusive_group: str | None = Field(None, alias="mutuallyExclusiveGroup")
    notes: str | None = None
    virtual: bool
    technology_optional: bool | None = Field(None, alias="technologyOptional")
    part_of_technology_package: bool | None = Field(None, alias="partOfTechnologyPackage")
    technology_capacity: str | None = Field(None, alias="technologyCapacity")
    cost_components: list[AdvancedCostComponentResponseDto] | None = Field(None, alias="costComponents")
    comes_from_db: str | None = Field(None, alias="comesFromDb")
    stages: list[UUID]


class StorageTechnologyRequestDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    variable_om_cost_percent: float | None = Field(None, alias="variableOmCostPercent")
    variable_om_energy_flow_cost: float | None = Field(None, alias="variableOmEnergyFlowCost", ge=0.0)
    capacity: float | None = Field(None, ge=0.0)
    maximum_capacity: float | None = Field(None, alias="maximumCapacity", ge=0.0)
    minimum_capacity: float | None = Field(None, alias="minimumCapacity", ge=0.0)
    fixed_investment_cost: float | None = Field(None, alias="fixedInvestmentCost", ge=0.0)
    fixed_embodied_co2: float | None = Field(None, alias="fixedEmbodiedCo2", ge=0.0)
    variable_om_cost: float | None = Field(None, alias="variableOmCost", ge=0.0)
    maximum_charging_rate: float | None = Field(None, alias="maximumChargingRate", ge=0.0, le=100.0)
    maximum_discharging_rate: float | None = Field(None, alias="maximumDischargingRate", ge=0.0, le=100.0)
    variable_embodied_co2: float | None = Field(None, alias="variableEmbodiedCo2", ge=0.0)
    fixed_replacement_cost: float | None = Field(None, alias="fixedReplacementCost")
    variable_replacement_cost_percent: float | None = Field(None, alias="variableReplacementCostPercent")
    variable_replacement_cost_chf: float | None = Field(None, alias="variableReplacementCostCHF")
    fixed_salvage_value: float | None = Field(None, alias="fixedSalvageValue")
    variable_salvage_value_percent: float | None = Field(None, alias="variableSalvageValuePercent")
    variable_salvage_value_chf: float | None = Field(None, alias="variableSalvageValueCHF")
    must_be_installed: str = Field(
        ...,
        alias="mustBeInstalled",
        pattern="canBeInstalled|mustBeInstalled|mustBeInstalledInAtLeastOneHub",
    )
    storage_name: str = Field(..., alias="storageName", max_length=100, min_length=0)
    variable_investment_cost: float | None = Field(None, alias="variableInvestmentCost", ge=0.0)
    fixed_om_cost_chf: float | None = Field(None, alias="fixedOmCostChf", ge=0.0)
    lifetime: int
    standby_loss: float | None = Field(None, alias="standbyLoss", ge=0.0, le=100.0)
    stand_by_loss_profile_id: int | None = Field(None, alias="standByLossProfileId")
    minimum_soc: float | None = Field(None, alias="minimumSoc", ge=0.0, le=100.0)
    hub_guids: list[str] = Field(..., alias="hubGuids")
    energy_carrier_guid: str = Field(..., alias="energyCarrierGuid")
    storage_charging_efficiency: float = Field(..., alias="storageChargingEfficiency", ge=0.0, le=100.0)
    storage_discharging_efficiency: float = Field(..., alias="storageDischargingEfficiency", ge=0.0, le=100.0)
    technology_capacity: str = Field(..., alias="technologyCapacity", pattern="optimize|specify")
    cost_components: list[AdvancedCostComponentRequestDto] | None = Field(None, alias="costComponents")
    suggested: bool | None = None
    technology_category: str | None = Field(None, alias="technologyCategory")
    notes: str | None = None
    source: str | None = None
    comes_from_db: str | None = Field(None, alias="comesFromDb")
    exchange_currency: str | None = Field(None, alias="exchangeCurrency", max_length=3, min_length=0)
    exchange_rate: float | None = Field(None, alias="exchangeRate", ge=0.0)
    stages: list[UUID]
    ev_plug_in_time: LocalTime | None = Field(None, alias="evPlugInTime")
    ev_plug_out_time: LocalTime | None = Field(None, alias="evPlugOutTime")
    ev_plug_in_duration_hours: float | None = Field(None, alias="evPlugInDurationHours")
    driving_distance_kms: float | None = Field(None, alias="drivingDistanceKms")
    ev_soc_start_percent: float | None = Field(None, alias="evSocStartPercent")
    ev_battery_size_k_wh: float | None = Field(None, alias="evBatterySizeKWh")
    maximum_soc_percent: float | None = Field(None, alias="maximumSocPercent")
    ev_average_k_wh_per_km: float | None = Field(None, alias="evAverageKWhPerKm")
    ev_plug_in_power_kw: float | None = Field(None, alias="evPlugInPowerKW")
    is_ev_battery: bool | None = Field(None, alias="isEvBattery")
    type_of_charging: TypeOfCharging | None = Field(None, alias="typeOfCharging")


class StorageTechnologyResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    storage_technology_guid: str | None = Field(None, alias="storageTechnologyGuid")
    storage_name: str | None = Field(None, alias="storageName")
    lifetime: int | None = None
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    energy_carrier: EnergyCarrierResponseDto | None = Field(None, alias="energyCarrier")
    hubs: list[HubResponseDto] | None = None
    stages: list[UUID] | None = None
    stand_by_loss_profile_id: int | None = Field(None, alias="standByLossProfileId")


class StorageTechnologyListResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    storage_technologies: list[StorageTechnologyResponseDtoV2] | None = Field(None, alias="storageTechnologies")


class StorageTechnologyDetailResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    variable_om_cost_percent: float | None = Field(None, alias="variableOmCostPercent")
    variable_om_energy_flow_cost: float | None = Field(None, alias="variableOmEnergyFlowCost", ge=0.0)
    capacity: float | None = Field(None, ge=0.0)
    maximum_capacity: float | None = Field(None, alias="maximumCapacity", ge=0.0)
    minimum_capacity: float | None = Field(None, alias="minimumCapacity", ge=0.0)
    fixed_investment_cost: float | None = Field(None, alias="fixedInvestmentCost", ge=0.0)
    fixed_embodied_co2: float | None = Field(None, alias="fixedEmbodiedCo2", ge=0.0)
    variable_om_cost: float | None = Field(None, alias="variableOmCost", ge=0.0)
    maximum_charging_rate: float | None = Field(None, alias="maximumChargingRate", ge=0.0, le=100.0)
    maximum_discharging_rate: float | None = Field(None, alias="maximumDischargingRate", ge=0.0, le=100.0)
    variable_embodied_co2: float | None = Field(None, alias="variableEmbodiedCo2", ge=0.0)
    fixed_replacement_cost: float | None = Field(None, alias="fixedReplacementCost")
    variable_replacement_cost_percent: float = Field(..., alias="variableReplacementCostPercent")
    variable_replacement_cost_chf: float | None = Field(None, alias="variableReplacementCostCHF")
    fixed_salvage_value: float | None = Field(None, alias="fixedSalvageValue")
    variable_salvage_value_percent: float = Field(..., alias="variableSalvageValuePercent")
    variable_salvage_value_chf: float | None = Field(None, alias="variableSalvageValueCHF")
    must_be_installed: str = Field(
        ...,
        alias="mustBeInstalled",
        pattern="canBeInstalled|mustBeInstalled|mustBeInstalledInAtLeastOneHub",
    )
    storage_technology_guid: str | None = Field(None, alias="storageTechnologyGuid")
    storage_name: str = Field(..., alias="storageName")
    exchange_currency: str = Field(..., alias="exchangeCurrency")
    exchange_rate: float = Field(..., alias="exchangeRate")
    variable_investment_cost: float | None = Field(None, alias="variableInvestmentCost")
    fixed_om_cost_chf: float | None = Field(None, alias="fixedOmCostChf")
    lifetime: int
    standby_loss: float | None = Field(None, alias="standbyLoss")
    stand_by_loss_profile_id: int | None = Field(None, alias="standByLossProfileId")
    minimum_soc: float | None = Field(None, alias="minimumSoc")
    storage_charging_efficiency: float = Field(..., alias="storageChargingEfficiency")
    storage_discharging_efficiency: float = Field(..., alias="storageDischargingEfficiency")
    technology_capacity: str = Field(..., alias="technologyCapacity")
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    storage_carrier: EnergyCarrierResponseDto = Field(..., alias="storageCarrier")
    hubs: list[HubResponseDto]
    category: str
    technology_category: str | None = Field(None, alias="technologyCategory")
    mutually_exclusive_group: str | None = Field(None, alias="mutuallyExclusiveGroup")
    notes: str | None = None
    source: str | None = None
    technology_optional: bool | None = Field(None, alias="technologyOptional")
    cost_components: list[AdvancedCostComponentResponseDto] = Field(..., alias="costComponents")
    comes_from_db: str | None = Field(None, alias="comesFromDb")
    stages: list[UUID]
    ev_plug_in_time: LocalTime | None = Field(None, alias="evPlugInTime")
    ev_plug_out_time: LocalTime | None = Field(None, alias="evPlugOutTime")
    ev_plug_in_duration_hours: float | None = Field(None, alias="evPlugInDurationHours")
    driving_distance_kms: float | None = Field(None, alias="drivingDistanceKms")
    ev_soc_start_percent: float | None = Field(None, alias="evSocStartPercent")
    ev_battery_size_k_wh: float | None = Field(None, alias="evBatterySizeKWh")
    maximum_soc_percent: float | None = Field(None, alias="maximumSocPercent")
    ev_average_k_wh_per_km: float | None = Field(None, alias="evAverageKWhPerKm")
    ev_plug_in_power_kw: float | None = Field(None, alias="evPlugInPowerKW")
    is_ev_battery: bool | None = Field(None, alias="isEvBattery")
    type_of_charging: TypeOfCharging | None = Field(None, alias="typeOfCharging")


class TechnologyPackageResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    maximum_conversions: int | None = Field(None, alias="maximumConversions", ge=1)
    maximum_storages: int | None = Field(None, alias="maximumStorages", ge=1)
    must_be_installed: MustBeInstalled = Field(..., alias="mustBeInstalled")
    mutually_exclusive_group: str | None = Field(None, alias="mutuallyExclusiveGroup")
    name: str
    guid: str | None = None
    conversion_technologies: list[GuidNameDto] = Field(..., alias="conversionTechnologies")
    storage_technologies: list[GuidNameDto] = Field(..., alias="storageTechnologies")


class TechnologyPackageListResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    technology_packages: list[TechnologyPackageResponseDtoV2] | None = Field(None, alias="technologyPackages")


class TechnologyPackageListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    technology_packages: list[TechnologyPackageResponseDto] | None = Field(None, alias="technologyPackages")


class NetworkTechnologyResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    fixed_investment_cost: float | None = Field(None, alias="fixedInvestmentCost", ge=0.0)
    variable_investment_cost: float | None = Field(None, alias="variableInvestmentCost", ge=0.0)
    fixed_om_cost_chf: float | None = Field(None, alias="fixedOmCostChf", ge=0.0)
    variable_om_cost_percent: float | None = Field(None, alias="variableOmCostPercent")
    variable_om_cost_year: float | None = Field(None, alias="variableOmCostYear", ge=0.0)
    variable_om_cost_ch_fk_wh: float | None = Field(None, alias="variableOmCostCHFkWh", ge=0.0)
    fixed_embodied_co2: float | None = Field(None, alias="fixedEmbodiedCo2", ge=0.0)
    variable_embodied_co2: float | None = Field(None, alias="variableEmbodiedCo2", ge=0.0)
    fixed_replacement_cost: float | None = Field(None, alias="fixedReplacementCost")
    variable_replacement_cost_percent: float = Field(..., alias="variableReplacementCostPercent")
    variable_replacement_cost_chf: float | None = Field(None, alias="variableReplacementCostCHF")
    fixed_salvage_value: float | None = Field(None, alias="fixedSalvageValue")
    variable_salvage_value_percent: float = Field(..., alias="variableSalvageValuePercent")
    variable_salvage_value_chf: float | None = Field(None, alias="variableSalvageValueCHF")
    network_technology_guid: str | None = Field(None, alias="networkTechnologyGuid")
    network_technology_name: str = Field(..., alias="networkTechnologyName")
    exchange_currency: str = Field(..., alias="exchangeCurrency")
    exchange_rate: float = Field(..., alias="exchangeRate")
    lifetime: int
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    energy_carrier: EnergyCarrierResponseDto = Field(..., alias="energyCarrier")
    category: str
    technology_category: str | None = Field(None, alias="technologyCategory")
    notes: str | None = None
    source: str | None = None
    network_size: str | None = Field(None, alias="networkSize")
    comes_from_db: str | None = Field(None, alias="comesFromDb")
    cost_components: list[AdvancedCostComponentResponseDto] = Field(..., alias="costComponents")
    stages: list[UUID]


class NetworkTechnologyListResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    network_technologies: list[NetworkTechnologyResponseDtoV2] | None = Field(None, alias="networkTechnologies")


class ResponseDtoNetworkLinkResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: NetworkLinkResponseDtoV2 | None = None
    status: Status | None = None


class NetworkLinkListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    network_links: list[NetworkLinkResponseDto] | None = Field(None, alias="networkLinks")


class IntraHubNetworkLinkResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    intra_hub_network_link_guid: str | None = Field(None, alias="intraHubNetworkLinkGuid")
    name: str
    network_loss: float | None = Field(None, alias="networkLoss")
    fixed_embodied_co2: float | None = Field(None, alias="fixedEmbodiedCo2")
    input_energy_carrier: EnergyCarrierResponseDto = Field(..., alias="inputEnergyCarrier")
    output_energy_carrier: EnergyCarrierResponseDto = Field(..., alias="outputEnergyCarrier")
    hubs: list[HubResponseDto]
    advanced_cost_components: list[AdvancedCostComponentResponseDto] = Field(..., alias="advancedCostComponents")
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    stages: list[UUID]


class IntraHubNetworkLinkListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    intra_hub_network_links: list[IntraHubNetworkLinkResponseDto] | None = Field(None, alias="intraHubNetworkLinks")


class ImportExportRequestDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    energy_price_ch_fk_wh: float | None = Field(None, alias="energyPriceCHFkWh")
    max_capacity_kw: float | None = Field(None, alias="maxCapacityKW")
    total_annual_energy_available_k_wh_a: float | None = Field(None, alias="totalAnnualEnergyAvailableKWhA")
    capacity_price_ch_fk_w_year: float | None = Field(None, alias="capacityPriceCHFkWYear")
    name: str
    hourly_energy_price_profile_id: int | None = Field(None, alias="hourlyEnergyPriceProfileId")
    capacity_price_ch_fk_w_month: float | None = Field(None, alias="capacityPriceCHFkWMonth")
    fixed_om_price_chf_year: float | None = Field(None, alias="fixedOmPriceCHFYear")
    co2_intensity_kg_co2k_wh_co2_compensation_kg_co2k_wh: float | None = Field(None, alias="co2IntensityKgCo2kWhCo2CompensationKgCo2kWh")
    dynamic_co2_profile_id: int | None = Field(None, alias="dynamicCo2ProfileId")
    maximum_hourly_energy_available_profile_id: int | None = Field(None, alias="maximumHourlyEnergyAvailableProfileId")
    energy_carrier_guid: str = Field(..., alias="energyCarrierGuid")
    type: Type1
    hubs: list[ImpexHubRequestDto]
    product: str | None = None
    year: int | None = None
    notes: str | None = None
    source: str | None = None
    suggested: bool | None = None
    price_components: list[AdvancedPriceComponentRequestDtoV2] | None = Field(None, alias="priceComponents")
    time_of_uses: list[TimeOfUseRequestDto] | None = Field(None, alias="timeOfUses")
    stages: list[UUID]


class ImportExportResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    energy_price_ch_fk_wh: float | None = Field(None, alias="energyPriceCHFkWh")
    max_capacity_kw: float | None = Field(None, alias="maxCapacityKW")
    total_annual_energy_available_k_wh_a: float | None = Field(None, alias="totalAnnualEnergyAvailableKWhA")
    capacity_price_ch_fk_w_year: float | None = Field(None, alias="capacityPriceCHFkWYear")
    name: str
    hourly_energy_price_profile_id: int | None = Field(None, alias="hourlyEnergyPriceProfileId")
    capacity_price_ch_fk_w_month: float | None = Field(None, alias="capacityPriceCHFkWMonth")
    fixed_om_price_chf_year: float | None = Field(None, alias="fixedOmPriceCHFYear")
    co2_intensity_kg_co2k_wh_co2_compensation_kg_co2k_wh: float | None = Field(None, alias="co2IntensityKgCo2kWhCo2CompensationKgCo2kWh")
    dynamic_co2_profile_id: int | None = Field(None, alias="dynamicCo2ProfileId")
    maximum_hourly_energy_available_profile_id: int | None = Field(None, alias="maximumHourlyEnergyAvailableProfileId")
    energy_carrier: EnergyCarrierResponseDto = Field(..., alias="energyCarrier")
    type: str
    hubs: list[ImpexHubResponseDto]
    guid: str | None = None
    updated: AwareDatetime | None = None
    created: AwareDatetime | None = None
    price_components: list[AdvancedPriceComponentResponseDtoV2] = Field(..., alias="priceComponents")
    time_of_uses: list[TimeOfUseResponseDto] = Field(..., alias="timeOfUses")
    product: str | None = None
    year: int | None = None
    notes: str | None = None
    source: str | None = None
    suggested: bool | None = None
    stages: list[UUID]


class ResponseDtoListImportExportResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: list[ImportExportResponseDtoV2] | None = None
    status: Status | None = None


class ProfileJsonRequestDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str
    values: list[ProfilePeriodValueDto]


class ResponseDtoProfileResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: ProfileResponseDto | None = None
    status: Status | None = None


class ResponseDtoProfileDetailsResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: ProfileDetailsResponseDto | None = None
    status: Status | None = None


class ResponseDtoEnergyDemandResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: EnergyDemandResponseDtoV2 | None = None
    status: Status | None = None


class ResponseDtoEnergyDemandDetailResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: EnergyDemandDetailResponseDtoV2 | None = None
    status: Status | None = None


class EnergyDemandListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    energy_demands: list[EnergyDemandResponseDto] | None = Field(None, alias="energyDemands")


class SolarOnSiteResourceRequestDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str
    energy_carrier_guid: str = Field(..., alias="energyCarrierGuid")
    hubs: list[SolarOnSiteResourcesHubRequestDtoV2]
    profile_id: int = Field(..., alias="profileId")
    stages: list[UUID]


class SolarOnSiteResourceResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str
    solar_resource_guid: str | None = Field(None, alias="solarResourceGuid")
    energy_carrier_guid: str = Field(..., alias="energyCarrierGuid")
    energy_carrier_name: str = Field(..., alias="energyCarrierName")
    hubs: list[HubSolarOnSiteResourceResponseDtoV2]
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    irradiance_profile_type: IrradianceProfileType = Field(..., alias="irradianceProfileType")
    solar_resource_metadata_name: str | None = Field(None, alias="solarResourceMetadataName")
    solar_resource_metadata_db_organization: str | None = Field(None, alias="solarResourceMetadataDbOrganization")
    solar_resource_metadata_guid: str | None = Field(None, alias="solarResourceMetadataGuid")
    solar_resource_metadata_location: str | None = Field(None, alias="solarResourceMetadataLocation")
    solar_resource_metadata_type: str | None = Field(None, alias="solarResourceMetadataType")
    solar_resource_metadata_slope: float | None = Field(None, alias="solarResourceMetadataSlope")
    solar_resource_metadata_orientation: str | None = Field(None, alias="solarResourceMetadataOrientation")
    stages: list[UUID]
    profile_id: int = Field(..., alias="profileId")


class ResponseDtoListSolarOnSiteResourceResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: list[SolarOnSiteResourceResponseDtoV2] | None = None
    status: Status | None = None


class SolarOnSiteResourceResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    solar_resource_guid: str | None = Field(None, alias="solarResourceGuid")
    energy_carrier_guid: str | None = Field(None, alias="energyCarrierGuid")
    energy_carrier_name: str | None = Field(None, alias="energyCarrierName")
    hubs: list[HubSolarOnSiteResourceResponseDto] | None = None
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    irradiance_profile_type: IrradianceProfileType1 | None = Field(None, alias="irradianceProfileType")
    solar_resource_metadata_name: str | None = Field(None, alias="solarResourceMetadataName")
    solar_resource_metadata_db_organization: str | None = Field(None, alias="solarResourceMetadataDbOrganization")
    solar_resource_metadata_guid: str | None = Field(None, alias="solarResourceMetadataGuid")
    solar_resource_metadata_location: str | None = Field(None, alias="solarResourceMetadataLocation")
    solar_resource_metadata_type: str | None = Field(None, alias="solarResourceMetadataType")
    solar_resource_metadata_slope: float | None = Field(None, alias="solarResourceMetadataSlope")
    solar_resource_metadata_orientation: str | None = Field(None, alias="solarResourceMetadataOrientation")


class StorageTechnologyResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    storage_technology_guid: str | None = Field(None, alias="storageTechnologyGuid")
    storage_name: str | None = Field(None, alias="storageName")
    lifetime: float | None = None
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    energy_carrier: EnergyCarrierResponseDto | None = Field(None, alias="energyCarrier")
    hubs: list[HubResponseDto] | None = None


class NetworkTechnologyResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    network_technology_guid: str | None = Field(None, alias="networkTechnologyGuid")
    network_technology_name: str | None = Field(None, alias="networkTechnologyName")
    network_loss: float | None = Field(None, alias="networkLoss")
    fixed_investment_cost: float | None = Field(None, alias="fixedInvestmentCost")
    variable_investment_cost: float | None = Field(None, alias="variableInvestmentCost")
    variable_om_cost_year: float | None = Field(None, alias="variableOmCostYear")
    fixed_om_cost_chf: float | None = Field(None, alias="fixedOmCostChf")
    fixed_om_cost_percent: float | None = Field(None, alias="fixedOmCostPercent")
    lifetime: float | None = None
    maximum_capacity: float | None = Field(None, alias="maximumCapacity")
    minimum_capacity: float | None = Field(None, alias="minimumCapacity")
    variable_embodied_co2: float | None = Field(None, alias="variableEmbodiedCo2")
    fixed_embodied_co2: float | None = Field(None, alias="fixedEmbodiedCo2")
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    energy_carrier: EnergyCarrierResponseDto | None = Field(None, alias="energyCarrier")
    category: str | None = None
    technology_category: str | None = Field(None, alias="technologyCategory")
    notes: str | None = None
    source: str | None = None
    network_size: str | None = Field(None, alias="networkSize")
    comes_from_db: str | None = Field(None, alias="comesFromDb")
    cost_components: list[AdvancedCostComponentResponseDto] | None = Field(None, alias="costComponents")


class GetUserProfileExt(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    account: User
    preferences: Preferences
    plan_limitation: GetPlanExt = Field(..., alias="planLimitation")
    organization: GetOrganizationExt
    subscription: GetSubscriptionExt
    profile_picture: str | None = Field(None, alias="profilePicture", title="Profilepicture")
    organization_picture: str | None = Field(None, alias="organizationPicture", title="Organizationpicture")


class HTTPValidationError(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    detail: list[ValidationError] | None = Field(None, title="Detail")


class GetSolverJobExt(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    status: JobStatus | None = JobStatus.validating
    status_msg: str | None = Field("Validating", alias="statusMsg", title="Statusmsg")
    batch_id: str | None = Field(None, alias="batchId", title="Batchid")
    points_completed: int | None = Field(0, alias="pointsCompleted", title="Pointscompleted")
    started: AwareDatetime | None = Field(None, title="Started")
    terminated: AwareDatetime | None = Field(None, title="Terminated")
    infeasibility_info: str | None = Field(None, alias="infeasibilityInfo", title="Infeasibilityinfo")
    name: str = Field(..., title="Name")
    objective1: ObjectiveFunction
    objective2: ObjectiveFunction | None = None
    scenario_guid: str | None = Field(None, alias="scenarioGuid", title="Scenarioguid")
    scenario_name: str | None = Field(None, alias="scenarioName", title="Scenarioname")
    temporal_resolution: TemporalResolution = Field(..., alias="temporalResolution")
    points: int = Field(..., ge=1, le=10, title="Points")
    time_limit: int = Field(..., alias="timeLimit", ge=1, le=18720, title="Timelimit")
    mip_gap: float = Field(..., alias="mipGap", ge=0.1, lt=100.0, title="Mipgap")
    account_guid: str = Field(..., alias="accountGuid", title="Accountguid")
    organization_id: UUID4 = Field(..., alias="organizationId", title="Organizationid")
    subscription_id: UUID4 = Field(..., alias="subscriptionId", title="Subscriptionid")
    id: UUID4 = Field(..., title="Id")
    created: AwareDatetime = Field(..., title="Created")
    input_file: InputFile | None = Field(None, alias="inputFile", title="Inputfile")
    output_file: OutputFile | None = Field(None, alias="outputFile", title="Outputfile")


class GetUsageExt(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    subscription: SubscriptionUsage
    user: UserUsage


class PostSolverJobExt(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str = Field(..., title="Name")
    objective1: ObjectiveFunction
    objective2: ObjectiveFunction | None = None
    scenario_guid: str | None = Field(None, alias="scenarioGuid", title="Scenarioguid")
    scenario_name: str | None = Field(None, alias="scenarioName", title="Scenarioname")
    temporal_resolution: TemporalResolution = Field(..., alias="temporalResolution")
    points: int = Field(..., ge=1, le=10, title="Points")
    time_limit: int = Field(..., alias="timeLimit", ge=1, le=18720, title="Timelimit")
    mip_gap: float = Field(..., alias="mipGap", ge=0.1, lt=100.0, title="Mipgap")
    input_file_id: UUID4 | None = Field(None, alias="inputFileId", title="Inputfileid")


class SolverJob(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    status: JobStatus | None = JobStatus.validating
    status_msg: str | None = Field("Validating", alias="statusMsg", title="Statusmsg")
    batch_id: str | None = Field(None, alias="batchId", title="Batchid")
    points_completed: int | None = Field(0, alias="pointsCompleted", title="Pointscompleted")
    started: AwareDatetime | None = Field(None, title="Started")
    terminated: AwareDatetime | None = Field(None, title="Terminated")
    infeasibility_info: str | None = Field(None, alias="infeasibilityInfo", title="Infeasibilityinfo")
    name: str = Field(..., title="Name")
    objective1: ObjectiveFunction
    objective2: ObjectiveFunction | None = None
    scenario_guid: str | None = Field(None, alias="scenarioGuid", title="Scenarioguid")
    scenario_name: str | None = Field(None, alias="scenarioName", title="Scenarioname")
    temporal_resolution: TemporalResolution = Field(..., alias="temporalResolution")
    points: int = Field(..., ge=1, le=10, title="Points")
    time_limit: int = Field(..., alias="timeLimit", ge=1, le=18720, title="Timelimit")
    mip_gap: float = Field(..., alias="mipGap", ge=0.1, lt=100.0, title="Mipgap")
    account_guid: str = Field(..., alias="accountGuid", title="Accountguid")
    organization_id: UUID4 = Field(..., alias="organizationId", title="Organizationid")
    subscription_id: UUID4 = Field(..., alias="subscriptionId", title="Subscriptionid")
    id: UUID4 = Field(..., title="Id")
    created: AwareDatetime = Field(..., title="Created")


class ResponseDtoProjectResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: ProjectResponseDto | None = None
    status: Status | None = None


class ResponseDtoProjectSummaryResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: ProjectSummaryResponseDto | None = None
    status: Status | None = None


class AnalysisResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    analysis_guid: str | None = Field(None, alias="analysisGuid")
    analysis_name: str | None = Field(None, alias="analysisName")
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    scenarios: list[ScenarioResponseDto] | None = None


class ResponseDtoAnalysisResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: AnalysisResponseDto | None = None
    status: Status | None = None


class PagedResponseAnalysisResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: list[AnalysisResponseDto] | None = None
    status: Status | None = None
    total_elements: int | None = Field(None, alias="totalElements")
    total_pages: int | None = Field(None, alias="totalPages")
    has_next: bool | None = Field(None, alias="hasNext")


class AnalysisDetailsResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    analysis_guid: str | None = Field(None, alias="analysisGuid")
    analysis_name: str | None = Field(None, alias="analysisName")
    execution_status: ExecutionStatus | None = Field(None, alias="executionStatus")
    execution_in_progress: bool | None = Field(None, alias="executionInProgress")
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    cover_image: str | None = Field(None, alias="coverImage")
    project_name: str | None = Field(None, alias="projectName")
    scenarios: list[ScenarioResponseDto] | None = None
    execution_options: ExecutionOptionsResponseDto | None = Field(None, alias="executionOptions")
    results: ResultsResponseDto | None = None
    project_guid: str | None = Field(None, alias="projectGuid")


class ResponseDtoEnergyCarrierResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: EnergyCarrierResponseDto | None = None
    status: Status | None = None


class ResponseDtoEnergyCarriersListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: EnergyCarriersListResponseDto | None = None
    status: Status | None = None


class TechnologyModeRequestDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    capacity: float | None = Field(None, ge=0.0)
    minimum_annual_output: float | None = Field(None, alias="minimumAnnualOutput", ge=0.0)
    maximum_annual_output: float | None = Field(None, alias="maximumAnnualOutput", ge=0.0)
    curtailment_limitation: float | None = Field(None, alias="curtailmentLimitation", ge=0.0)
    peak_power: float | None = Field(None, alias="peakPower")
    min_part_load: float | None = Field(None, alias="minPartLoad", ge=0.0, le=100.0)
    minimum_up_time: int | None = Field(None, alias="minimumUpTime", ge=1, le=8760)
    minimum_down_time: int | None = Field(None, alias="minimumDownTime", ge=1, le=8760)
    primary: bool | None = None
    seasonal_operation: SeasonalOperation = Field(..., alias="seasonalOperation")
    allowed_operation_profile_id: int | None = Field(None, alias="allowedOperationProfileId")
    energy_carriers: list[ConversionCarrierRequestDtoV2] = Field(..., alias="energyCarriers")
    maximum_capacity: float | None = Field(None, alias="maximumCapacity", ge=0.0)
    minimum_capacity: float | None = Field(None, alias="minimumCapacity", ge=0.0)
    simultaneous_operation: bool | None = Field(None, alias="simultaneousOperation")


class ConversionTechnologyResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    conversion_technology_guid: str | None = Field(None, alias="conversionTechnologyGuid")
    process_name: str | None = Field(None, alias="processName")
    lifetime: int | None = None
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    conversion_technology_modes: list[TechnologyModeResponseDtoV2] | None = Field(None, alias="conversionTechnologyModes")
    hubs: list[HubResponseDto] | None = None
    virtual: bool | None = None
    must_be_installed_in_hubs: MustBeInstalledInHubs1 | None = Field(None, alias="mustBeInstalledInHubs")
    stages: list[UUID] | None = None


class ConversionTechnologyListResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    conversion_technologies: list[ConversionTechnologyResponseDtoV2] | None = Field(None, alias="conversionTechnologies")


class ResponseDtoConversionTechnologyDetailResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: ConversionTechnologyDetailResponseDtoV2 | None = None
    status: Status | None = None


class ResponseDtoStorageTechnologyResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: StorageTechnologyResponseDtoV2 | None = None
    status: Status | None = None


class ResponseDtoStorageTechnologyListResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: StorageTechnologyListResponseDtoV2 | None = None
    status: Status | None = None


class ResponseDtoStorageTechnologyDetailResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: StorageTechnologyDetailResponseDtoV2 | None = None
    status: Status | None = None


class ResponseDtoTechnologyPackageResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: TechnologyPackageResponseDtoV2 | None = None
    status: Status | None = None


class ResponseDtoTechnologyPackageListResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: TechnologyPackageListResponseDtoV2 | None = None
    status: Status | None = None


class ResponseDtoTechnologyPackageListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: TechnologyPackageListResponseDto | None = None
    status: Status | None = None


class ResponseDtoNetworkTechnologyResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: NetworkTechnologyResponseDtoV2 | None = None
    status: Status | None = None


class ResponseDtoNetworkTechnologyListResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: NetworkTechnologyListResponseDtoV2 | None = None
    status: Status | None = None


class ResponseDtoNetworkLinkListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: NetworkLinkListResponseDto | None = None
    status: Status | None = None


class ResponseDtoIntraHubNetworkLinkResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: IntraHubNetworkLinkResponseDto | None = None
    status: Status | None = None


class ResponseDtoIntraHubNetworkLinkListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: IntraHubNetworkLinkListResponseDto | None = None
    status: Status | None = None


class ResponseDtoImportExportResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: ImportExportResponseDtoV2 | None = None
    status: Status | None = None


class ResponseDtoEnergyDemandListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: EnergyDemandListResponseDto | None = None
    status: Status | None = None


class ResponseDtoSolarOnSiteResourceResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: SolarOnSiteResourceResponseDtoV2 | None = None
    status: Status | None = None


class SolarOnSiteResourceListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    solar_resources: list[SolarOnSiteResourceResponseDto] | None = Field(None, alias="solarResources")


class StorageTechnologyListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    storage_technologies: list[StorageTechnologyResponseDto] | None = Field(None, alias="storageTechnologies")


class NetworkTechnologyListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    network_technologies: list[NetworkTechnologyResponseDto] | None = Field(None, alias="networkTechnologies")


class ProjectDetailResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    images: list[ImageResponseDto] | None = None
    project_name: str | None = Field(None, alias="projectName")
    project_guid: str | None = Field(None, alias="projectGuid")
    created: AwareDatetime | None = None
    updated: AwareDatetime | None = None
    project_owner: str | None = Field(None, alias="projectOwner")
    project_owner_email: str | None = Field(None, alias="projectOwnerEmail")
    secondary_owners: list[SecondaryOwnerDto] | None = Field(None, alias="secondaryOwners")
    lock_user_email: str | None = Field(None, alias="lockUserEmail")
    lock: bool | None = None
    lock_time: AwareDatetime | None = Field(None, alias="lockTime")
    owned_by_current_user: bool | None = Field(None, alias="ownedByCurrentUser")
    editable_by_current_user: bool | None = Field(None, alias="editableByCurrentUser")
    owner_history: list[ProjectOwnerHistoryResponseDto] | None = Field(None, alias="ownerHistory")
    analyses: list[AnalysisResponseDto] | None = None
    cover_image: str | None = Field(None, alias="coverImage")
    original_default_project_guid: str | None = Field(None, alias="originalDefaultProjectGuid")
    version: Version1 | None = None
    webhook_url: str | None = Field(None, alias="webhookUrl")
    favorite: bool | None = None
    gis_centroid_x: float | None = Field(None, alias="gisCentroidX")
    gis_centroid_y: float | None = Field(None, alias="gisCentroidY")
    zoom_extent_xmin: float | None = Field(None, alias="zoomExtentXmin")
    zoom_extent_ymin: float | None = Field(None, alias="zoomExtentYmin")
    zoom_extent_xmax: float | None = Field(None, alias="zoomExtentXmax")
    zoom_extent_ymax: float | None = Field(None, alias="zoomExtentYmax")


class ResponseDtoAnalysisDetailsResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: AnalysisDetailsResponseDto | None = None
    status: Status | None = None


class ConversionTechnologyRequestDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    fixed_investment_cost: float | None = Field(None, alias="fixedInvestmentCost", ge=0.0)
    fixed_om_cost_chf: float | None = Field(None, alias="fixedOmCostChf", ge=0.0)
    variable_om_cost_percent: float | None = Field(None, alias="variableOmCostPercent")
    variable_om_cost_year: float | None = Field(None, alias="variableOmCostYear", ge=0.0)
    variable_om_cost: float | None = Field(None, alias="variableOmCost", ge=0.0)
    fixed_embodied_co2: float | None = Field(None, alias="fixedEmbodiedCo2", ge=0.0)
    variable_embodied_co2: float | None = Field(None, alias="variableEmbodiedCo2", ge=0.0)
    variable_emitted_co2: float | None = Field(None, alias="variableEmittedCo2", ge=0.0)
    variable_captured_co2: float | None = Field(None, alias="variableCapturedCo2", ge=0.0)
    fixed_replacement_cost: float | None = Field(None, alias="fixedReplacementCost", ge=0.0)
    variable_replacement_cost_percent: float | None = Field(None, alias="variableReplacementCostPercent", ge=0.0)
    variable_replacement_cost_chf: float | None = Field(None, alias="variableReplacementCostCHF", ge=0.0)
    fixed_salvage_value: float | None = Field(None, alias="fixedSalvageValue", ge=0.0)
    variable_salvage_value_percent: float | None = Field(None, alias="variableSalvageValuePercent", ge=0.0)
    variable_salvage_value_chf: float | None = Field(None, alias="variableSalvageValueCHF", ge=0.0)
    must_be_installed_in_hubs: MustBeInstalledInHubs = Field(..., alias="mustBeInstalledInHubs")
    process_name: str = Field(..., alias="processName", max_length=100, min_length=0)
    variable_investment_cost: float | None = Field(None, alias="variableInvestmentCost", ge=0.0)
    lifetime: int
    hub_guids: list[str] = Field(..., alias="hubGuids")
    conversion_technology_modes: list[TechnologyModeRequestDtoV2] = Field(..., alias="conversionTechnologyModes", max_length=3, min_length=1)
    virtual: bool
    cost_components: list[AdvancedCostComponentRequestDto] | None = Field(None, alias="costComponents")
    suggested: bool | None = None
    technology_category: str | None = Field(None, alias="technologyCategory")
    notes: str | None = None
    source: str | None = None
    comes_from_db: str | None = Field(None, alias="comesFromDb")
    exchange_currency: str = Field(..., alias="exchangeCurrency", max_length=3, min_length=0)
    exchange_rate: float = Field(..., alias="exchangeRate", ge=0.0)
    stages: list[UUID]


class ResponseDtoConversionTechnologyResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: ConversionTechnologyResponseDtoV2 | None = None
    status: Status | None = None


class ResponseDtoConversionTechnologyListResponseDtoV2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: ConversionTechnologyListResponseDtoV2 | None = None
    status: Status | None = None


class ResponseDtoSolarOnSiteResourceListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: SolarOnSiteResourceListResponseDto | None = None
    status: Status | None = None


class ResponseDtoStorageTechnologyListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: StorageTechnologyListResponseDto | None = None
    status: Status | None = None


class ResponseDtoNetworkTechnologyListResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: NetworkTechnologyListResponseDto | None = None
    status: Status | None = None


class ResponseDtoProjectDetailResponseDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: ProjectDetailResponseDto | None = None
    status: Status | None = None

<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/models.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# GIS models

GeoJSON models used by `client.buildings`.

## Address { #model-Address }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `street` | `str`, optional | yes |  |
| `house_number` | `str`, optional | yes |  |
| `postcode` | `str`, optional | yes |  |
| `locality` | `str`, optional | yes |  |
| `country` | `str`, optional | yes |  |
| `formatted` | `str` | yes |  |
| `source` | `str` | yes |  |

## BuildingFeature { #model-BuildingFeature }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | [`FeatureEnum`](#model-FeatureEnum), optional | no |  |
| `geometry` | [`Geometry`](#model-Geometry) | yes |  |
| `properties` | [`BuildingProperties`](#model-BuildingProperties) | yes |  |

## BuildingFeatureCollection { #model-BuildingFeatureCollection }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | [`FeatureCollectionEnum`](#model-FeatureCollectionEnum), optional | no |  |
| `features` | list of [`BuildingFeature`](#model-BuildingFeature) | yes |  |
| `properties` | `dict[str, Any]`, optional | no |  |

## BuildingProperties { #model-BuildingProperties }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | `str` | yes |  |
| `area_m2` | `int` | yes |  |
| `floors` | `int`, optional | yes |  |
| `height_m` | `float`, optional | yes |  |
| `building_type` | [`BuildingTypeEnum`](#model-BuildingTypeEnum), optional | yes |  |
| `construction_year` | `int`, optional | yes |  |
| `addresses` | list of [`Address`](#model-Address) | yes |  |

## BuildingTypeEnum { #model-BuildingTypeEnum }

| Member | Value |
| --- | --- |
| `BuildingTypeEnum.residence_mfh` | `'RESIDENCE_MFH'` |
| `BuildingTypeEnum.residence_sfh` | `'RESIDENCE_SFH'` |
| `BuildingTypeEnum.administration` | `'ADMINISTRATION'` |
| `BuildingTypeEnum.schools` | `'SCHOOLS'` |
| `BuildingTypeEnum.retail` | `'RETAIL'` |
| `BuildingTypeEnum.assembly` | `'ASSEMBLY'` |
| `BuildingTypeEnum.hospitals` | `'HOSPITALS'` |
| `BuildingTypeEnum.industry` | `'INDUSTRY'` |
| `BuildingTypeEnum.warehouse` | `'WAREHOUSE'` |
| `BuildingTypeEnum.sports_center` | `'SPORTS_CENTER'` |
| `BuildingTypeEnum.hotel` | `'HOTEL'` |

## FeatureCollectionEnum { #model-FeatureCollectionEnum }

| Member | Value |
| --- | --- |
| `FeatureCollectionEnum.feature_collection` | `'FeatureCollection'` |

## FeatureEnum { #model-FeatureEnum }

| Member | Value |
| --- | --- |
| `FeatureEnum.feature` | `'Feature'` |

## FeatureGeoTypeEnum { #model-FeatureGeoTypeEnum }

| Member | Value |
| --- | --- |
| `FeatureGeoTypeEnum.point` | `'Point'` |
| `FeatureGeoTypeEnum.line_string` | `'LineString'` |
| `FeatureGeoTypeEnum.polygon` | `'Polygon'` |
| `FeatureGeoTypeEnum.multi_point` | `'MultiPoint'` |
| `FeatureGeoTypeEnum.multi_line_string` | `'MultiLineString'` |
| `FeatureGeoTypeEnum.multi_polygon` | `'MultiPolygon'` |

## Geometry { #model-Geometry }

A class representing a geojson geometry.

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | [`FeatureGeoTypeEnum`](#model-FeatureGeoTypeEnum) | yes |  |
| `coordinates` | list of `Any` | yes |  |

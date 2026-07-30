---
tags:
  - web-app
  - concepts
---

# Demand profiles methodology

The demand profiles in Sympheny are based on different sources depending on the
building use. They are stored in three levels, each contributing to the overall shape
of the demand profile:

- **Demand type** refers to the energy carrier. Space heating and cooling depend on a
  normalized weather profile, while the other profiles are stochastic: they depend on
  the time of use of different appliances.
- **Building use** affects the shape of the profile. For example, an office building is
  generally closed on weekends and less occupied in summer, while a hospital operates
  at high capacity throughout the year.
- **Building age or standard** is used to derive an energy intensity (kWh/m2/year), to
  estimate annual demand in kWh from the energy reference area (m2). The SIA standards
  include values of peak load in kW. When you select SIA standards, profiles are
  slightly reshaped to match the annual demand in kWh and the peak load in kW.

In the database, all profiles are normalized for annual energy demand, meaning the sum
of annual energy demand is 1 kWh. The profile is then "scaled": multiplied by the
actual energy demand.

The demand profiles in Sympheny are based on different sources depending on the
building use:

- [Fraunhofer-Gesellschaft](https://www.fraunhofer.de/en.html), a German applied
  research institute, provided data for:
    - Administration / office
    - Hospitals
    - Multi-family house
    - Retail
    - Schools
    - Single-family house
- Open-source data provided by
  [Rutgers, The State University of New Jersey](https://data.mendeley.com/datasets/rfnp2d3kjp/1)
  provided profile data for:
    - Hotel
    - Indoor swimming pool
    - Industry 2-shift fabricated metals
    - Industry warehouse
- Swiss building standards SIA 380 and SIA 2024 provided additional data for the
  remaining profiles:
    - Assembly
    - Industry
    - Sports center
    - Warehouse

## Fraunhofer-Gesellschaft profiles

The Fraunhofer-Gesellschaft residential profiles (multi-family house, MFH, and
single-family house, SFH) were generated using the
[SynPro tool](https://synpro-lastprofile.de/) in 2020. The four non-residential
profiles were generated using their
[synGHD tool](https://www.ise.fraunhofer.de/de/forschungsprojekte/synghd.html) in 2020.
All profiles were generated using
[weather data for Zürich, 2018](https://prod-eu-north-1-sympheny-public.s3.eu-north-1.amazonaws.com/docs/data/weather-data-zurich-2018.csv).

### Residential profiles

#### Multi-family house (MFH)

The simulation is based on a renovated building constructed up until 1978, with a
typical use of a small multi-family dwelling (up to 10 units). U-values for walls,
windows, and roof are 0.3 W/m2·K, 0.5 W/m2·K, and 0.2 W/m2·K, respectively.

The following parameters are used:

- Window-to-wall ratio: 0.23
- Area-to-volume ratio: 0.43
- Set-points:
    - Heating: 20°C
    - Cooling: 24°C

#### Single-family house (SFH)

The simulation is based on a one-occupant renovated building constructed up until 1978.
U-values for walls, windows, and roof are 0.3 W/m2·K, 0.5 W/m2·K, and 0.2 W/m2·K,
respectively.

The following parameters are used:

- Window-to-wall ratio: 0.19
- Area-to-volume ratio: 0.92
- Set-points:
    - Heating: 20°C
    - Cooling: 24°C

### Non-residential profiles

The simulation is based on the following building age classes:

- Offices: 2002 until today.
- Hospitals, restaurants, schools, and shops: until 1978, renovated.

The following parameters are used:

- Set-points:
    - Heating: 20°C
    - Cooling: 26°C

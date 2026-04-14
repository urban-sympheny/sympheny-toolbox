[![PyPI - Version](https://img.shields.io/pypi/v/sympheny-toolbox.svg)](https://pypi.org/project/sympheny-toolbox)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sympheny-toolbox.svg)](https://pypi.org/project/sympheny-toolbox)

# Sympheny Toolbox

A lightweight Python wrapper for the [Sympheny](https://www.sympheny.com) SaaS API to automate common workflows — create scenarios, run optimizations, manage variants, and more.

## Install

```bash
pip install sympheny-toolbox
```

Requires **Python 3.11+**.

## Authentication

Create a `.properties` file with your Sympheny credentials:

```properties
username=you@example.com
password=your-password
```

Then load and connect:

```python
from sympheny_toolbox.sympheny import Sympheny
from sympheny_toolbox.utils import load_creds_basic

username, password = load_creds_basic("creds.properties")
s = Sympheny(username, password)

# Use is_dev=True for the dev environment
```

> **Tip:** Don't commit credential files — use a secrets manager or `.gitignore`.

## Usage

### Find projects, analyses, and scenarios

```python
project = s.find_project("My Project")
analysis = s.find_analysis("My Analysis", project["projectGuid"])
scenario = s.find_scenario("Base", analysis["analysisGuid"])
```

### Create a scenario from Excel

```python
scenario_guid = s.create_scenario_from_excel(
    excel_path="scenario.xlsx",
    scenario_name="demo",
    analysis_guid=analysis_guid,
)
print(s.scenario_url(scenario_guid))
```

### Create scenario variants from Excel

```python
variants = s.create_variants_from_excel(
    excel_path="variants.xlsx",
    master_scenario_id=scenario_guid,
)
```

### Generate and read an input file

```python
from sympheny_toolbox.utils import load_sheet_from_presigned_url

url = s.generate_input_file(scenario_guid)
rows = load_sheet_from_presigned_url(url, sheet="Conversion Techs")
```

### Execute a scenario

```python
s.execute_scenario(scenario_guid)
```

### Create an EnyMap scenario

```python
scenario_guid = s.create_scenario_enymap(
    scenario_name="enymap_demo",
    analysis_id=analysis_guid,
    techs=["PV", "HEAT_PUMP"],
    demands=["ELECTRICITY", "SPACE_HEATING"],
    imports=["ELECTRICITY"],
    exports=["HEAT_AMBIENT"],
    poly=[[lon, lat], ...],
)
```

Available EnyMap options are defined in `sympheny_toolbox.enymap`:

| Parameter | Options |
|-----------|---------|
| `techs` | `PV`, `HEAT_PUMP`, `GAS_BOILER`, `CHILLER`, `BATTERY`, `HOT_WATER_STORAGE` |
| `demands` | `HOT_WATER`, `SPACE_HEATING`, `ELECTRICITY`, `COOLING` |
| `imports` | `ELECTRICITY` |
| `exports` | `HEAT_AMBIENT`, `COOLING` |
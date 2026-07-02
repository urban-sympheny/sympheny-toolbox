"""Tests for the openpyxl-based Excel helpers."""

from __future__ import annotations

import io

from openpyxl import Workbook

from sympheny_toolbox import excel


def _workbook_bytes(workbook: Workbook) -> bytes:
    buffer = io.BytesIO()
    workbook.save(buffer)
    return buffer.getvalue()


def test_build_variants_workbook_round_trip() -> None:
    variants = [
        {"Variant name": "V1", "Parameter": "PV capacity", "Value": 10},
        {"Variant name": "V2", "Parameter": "PV capacity", "Value": 20, "Comment": "extra column"},
    ]

    content = excel.build_variants_workbook(variants)

    assert excel.sheet_names(content) == ["Variants"]
    records = excel.read_records(content, ["Variants"])["Variants"]
    assert records == [
        {"Variant name": "V1", "Parameter": "PV capacity", "Value": 10, "Comment": None},
        {"Variant name": "V2", "Parameter": "PV capacity", "Value": 20, "Comment": "extra column"},
    ]


def test_build_variants_workbook_with_profiles_round_trip() -> None:
    profiles = {"Heat demand": [1.0, 2.0, 3.0], "Electricity": [0.5] * excel.PROFILE_LENGTH}

    content = excel.build_variants_workbook([{"Variant name": "V1"}], profiles)

    assert excel.sheet_names(content) == ["Variants", "Profiles"]
    result = excel.read_profile_input_sheet(content, "Profiles")
    assert set(result) == {"Heat demand", "Electricity"}
    assert all(len(values) == excel.PROFILE_LENGTH for values in result.values())
    assert result["Heat demand"][:4] == [1.0, 2.0, 3.0, 0.0]  # short profiles are zero-padded
    assert result["Electricity"] == [0.5] * excel.PROFILE_LENGTH


def test_read_records_skips_blank_rows() -> None:
    workbook = Workbook()
    sheet = workbook.active
    assert sheet is not None
    sheet.title = "Data"
    sheet.append(["Name", "Value"])
    sheet.append(["a", 1])
    sheet.append([None, None])
    sheet.append(["b", None])

    records = excel.read_records(_workbook_bytes(workbook), ["Data"])["Data"]

    assert records == [{"Name": "a", "Value": 1}, {"Name": "b", "Value": None}]


def test_read_profile_sheets_excludes_time_step_column() -> None:
    workbook = Workbook()
    sheet = workbook.active
    assert sheet is not None
    sheet.title = "Mode 1"
    sheet.append(["Result profiles", None, None])  # title row
    sheet.append(["Time step", "Gas boiler", "PV"])
    sheet.append([1, 10.0, 0.0])
    sheet.append([2, 12.5, 3.5])

    result = excel.read_profile_sheets(_workbook_bytes(workbook), ["Mode 1"])

    assert result == {"Mode 1": {"Gas boiler": [10.0, 12.5], "PV": [0.0, 3.5]}}


def test_read_profile_input_sheet_pads_missing_values_and_truncates() -> None:
    workbook = Workbook()
    sheet = workbook.active
    assert sheet is not None
    sheet.title = "Profiles"
    sheet.append(["Profile name", "Long", "Short"])
    sheet.append(["Time step", None, None])
    for step in range(excel.PROFILE_LENGTH + 5):
        sheet.append([step + 1, 1.5, 2.5 if step < 10 else None])

    profiles = excel.read_profile_input_sheet(_workbook_bytes(workbook), "Profiles")

    assert len(profiles["Long"]) == excel.PROFILE_LENGTH  # extra rows are truncated
    assert profiles["Long"] == [1.5] * excel.PROFILE_LENGTH
    assert profiles["Short"][:10] == [2.5] * 10
    assert profiles["Short"][10:] == [0.0] * (excel.PROFILE_LENGTH - 10)  # missing cells become 0.0

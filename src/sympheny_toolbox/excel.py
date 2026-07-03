"""Excel helpers for Sympheny input/output files, based on openpyxl.

These helpers replicate the sheet layouts used by the Sympheny platform:
plain record sheets (header row + data rows) and profile sheets
(name header row, ``Time step`` sub-header row, then 8760 hourly values).
"""

from __future__ import annotations

import io
import warnings
from pathlib import Path
from typing import IO, TYPE_CHECKING, Any

from openpyxl import Workbook, load_workbook


if TYPE_CHECKING:
    from openpyxl.worksheet.worksheet import Worksheet

ExcelSource = str | Path | bytes | IO[bytes]

PROFILE_LENGTH = 8760


def _load(source: ExcelSource) -> Any:
    buffer: str | Path | IO[bytes] = io.BytesIO(source) if isinstance(source, bytes) else source
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return load_workbook(buffer, read_only=True, data_only=True)


def sheet_names(source: ExcelSource) -> list[str]:
    """Return the sheet names of an Excel workbook."""
    workbook = _load(source)
    try:
        return list(workbook.sheetnames)
    finally:
        workbook.close()


def read_records(source: ExcelSource, sheets: list[str]) -> dict[str, list[dict[str, Any]]]:
    """Read record sheets (first row = header) into ``{sheet: [row dicts]}``."""
    workbook = _load(source)
    try:
        result: dict[str, list[dict[str, Any]]] = {}
        for sheet in sheets:
            rows = workbook[sheet].iter_rows(values_only=True)
            header = [str(cell) if cell is not None else "" for cell in next(rows, ())]
            result[sheet] = [dict(zip(header, row)) for row in rows if any(cell is not None for cell in row)]
        return result
    finally:
        workbook.close()


def read_profile_sheets(source: ExcelSource, sheets: list[str]) -> dict[str, dict[str, list[Any]]]:
    """Read profile sheets (header on the second row) into ``{sheet: {column: values}}``.

    The ``Time step`` index column is excluded, matching the layout of Sympheny
    result files.
    """
    workbook = _load(source)
    try:
        result: dict[str, dict[str, list[Any]]] = {}
        for sheet in sheets:
            rows = workbook[sheet].iter_rows(values_only=True)
            next(rows, None)  # title row above the header
            header = [str(cell) if cell is not None else "" for cell in next(rows, ())]
            columns: dict[str, list[Any]] = {name: [] for name in header if name != "Time step"}
            for row in rows:
                for name, cell in zip(header, row):
                    if name != "Time step":
                        columns[name].append(cell)
            result[sheet] = columns
        return result
    finally:
        workbook.close()


def read_profile_input_sheet(source: ExcelSource, sheet: str) -> dict[str, list[float]]:
    """Read a variants ``Profiles`` input sheet into ``{profile name: 8760 hourly values}``.

    The first column (time step index) and the sub-header row are skipped; missing
    values are filled with ``0.0`` and every profile is padded/truncated to 8760 values.
    """
    workbook = _load(source)
    try:
        rows = workbook[sheet].iter_rows(values_only=True)
        header = [str(cell) if cell is not None else "" for cell in next(rows, ())]
        next(rows, None)  # "Time step" sub-header row
        profiles: dict[str, list[float]] = {name: [] for name in header[1:]}
        for row in rows:
            for name, cell in zip(header[1:], row[1:]):
                profiles[name].append(float(cell) if cell is not None else 0.0)
        for values in profiles.values():
            if len(values) < PROFILE_LENGTH:
                values.extend([0.0] * (PROFILE_LENGTH - len(values)))
            del values[PROFILE_LENGTH:]
        return profiles
    finally:
        workbook.close()


def _write_records(worksheet: Worksheet, records: list[dict[str, Any]]) -> None:
    header: list[str] = []
    for record in records:
        header.extend(key for key in record if key not in header)
    worksheet.append(header)
    for record in records:
        worksheet.append([record.get(key) for key in header])


def build_variants_workbook(variants: list[dict[str, Any]], profiles: dict[str, list[float]] | None = None) -> bytes:
    """Build a scenario-variants Excel workbook (``Variants`` + optional ``Profiles`` sheet) in memory."""
    workbook = Workbook()
    default_sheet = workbook.active
    variants_sheet = workbook.create_sheet("Variants")
    if default_sheet is not None:
        workbook.remove(default_sheet)
    _write_records(variants_sheet, variants)

    if profiles:
        profiles_sheet = workbook.create_sheet("Profiles")
        names = list(profiles)
        profiles_sheet.append(["Profile name", *names])
        profiles_sheet.append(["Time step", *[""] * len(names)])
        for step in range(PROFILE_LENGTH):
            profiles_sheet.append([step + 1, *(profiles[name][step] if step < len(profiles[name]) else 0.0 for name in names)])

    buffer = io.BytesIO()
    workbook.save(buffer)
    return buffer.getvalue()

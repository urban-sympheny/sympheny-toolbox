import os
import tempfile
import zipfile
from io import BytesIO

import pandas as pd
import requests as r

from sympheny_toolbox.utils import excel_to_dict, excel_to_dict_profile


def list_jobs(s, scenario_id, status):
    base_url = s.base_url
    h = s.h

    data = {"scenarioGuids": [scenario_id], "limit": 200}
    resp = r.post(
        f"{base_url}sense-api/ext/solver/jobs/get-scenarios", headers=h, json=data
    )
    jobs = list(filter(lambda j: j["scenarioGuid"] == scenario_id, resp.json()))
    if status:
        jobs = [x for x in jobs if x["status"] == status]
    return jobs


def get_job(s, job_id):
    base_url = s.base_url
    h = s.h
    return r.get(f"{base_url}sense-api/ext/solver/jobs/{job_id}", headers=h).json()


def read_output_file(solution, presigned_url):
    sheets = ["Cost & CO2"]
    sheet_prefixes = ["Mode "]
    resp = r.get(presigned_url)

    # 2. Create the temporary directory
    with tempfile.TemporaryDirectory() as extract_path:
        # Unzip directly into the temp folder
        with zipfile.ZipFile(BytesIO(resp.content)) as z:
            z.extractall(extract_path)

        # 3. Find the Excel file inside the temp folder
        target_file = None
        for file in os.listdir(extract_path):
            if file.startswith(solution) and file.endswith(".xlsx"):
                target_file = os.path.join(extract_path, file)
                break

        if not target_file:
            raise FileNotFoundError(
                f"Could not find Excel file starting with {solution}"
            )

        dict1 = excel_to_dict(target_file, sheets)
        sheet_names = pd.ExcelFile(target_file).sheet_names
        sheets = [
            sheet
            for sheet in sheet_names
            if any(sheet.startswith(s) for s in sheet_prefixes)
        ]
        dict2 = excel_to_dict_profile(target_file, sheets)

        return dict1 | dict2


def get_output_file_dict(s, job_id, solution_num):
    job = s.get_job(job_id)
    solution = f"Solution {solution_num}"
    return read_output_file(solution, job["outputFile"])

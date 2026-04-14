import io
import time

import pandas as pd
import requests as r

from sympheny_toolbox import enymap, execution, execution_results
from sympheny_toolbox.utils import excel_to_dict


class Sympheny:
    def __init__(self, username, password, is_dev=False):
        self.base_url = (
            "https://eu-north-1-api.dev.sympheny.com/"
            if is_dev
            else "https://eu-north-1-api.sympheny.com/"
        )
        self.is_dev = is_dev
        self.be = f"{self.base_url}sympheny-app/"
        self.username = username
        self.password = password
        self.h = self._authenticate()

    def _authenticate(self):
        auth_url = f"{self.base_url}backoffice/auth/ext/token"
        response = r.post(
            auth_url, json={"email": self.username, "password": self.password}
        )
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        jwt = response.json()["access_token"]
        return {"authorization": f"Bearer {jwt}"}

    def list_projects(self):
        url = f"{self.be}projects"
        response = r.get(url, headers=self.h)
        response.raise_for_status()
        projects = response.json()["data"]["projects"]
        project_names = [x["projectName"] for x in projects]
        return project_names

    def list_variants(self, scenario_guid):
        return r.get(
            f"{self.be}master-scenario/{scenario_guid}/scenario-variants",
            headers=self.h,
        ).json()["data"]

    def delete_all_variants(self, master_scenario_id):
        resp = r.delete(
            f"{self.be}master-scenario/" + master_scenario_id + "/scenario-variants",
            headers=self.h,
        )
        if resp.status_code != 200:
            raise Exception(resp.text)

    def find_project(self, project_name):
        url = f"{self.be}projects"
        response = r.get(url, headers=self.h)
        response.raise_for_status()
        projects = response.json()["data"]["projects"]
        project = next((x for x in projects if x["projectName"] == project_name), None)
        if not project:
            return None

        project_guid = project["projectGuid"]
        return r.get(f"{self.be}projects/{project_guid}", headers=self.h).json()["data"]

    def get_analysis(self, analysis_id):
        return r.get(f"{self.be}analysis/{analysis_id}", headers=self.h).json()["data"]

    def find_analysis(self, analysis_name, projectGuid):
        analyses = r.get(f"{self.be}projects/{projectGuid}", headers=self.h).json()[
            "data"
        ]["analyses"]
        analysis = next(
            (x for x in analyses if x["analysisName"] == analysis_name), None
        )
        if not analysis:
            return None

        analysis_guid = analysis["analysisGuid"]
        return r.get(f"{self.be}analysis/{analysis_guid}", headers=self.h).json()[
            "data"
        ]

    def find_scenario(self, scenario_name, analysis_guid):
        scenarios = r.get(f"{self.be}analysis/{analysis_guid}", headers=self.h).json()[
            "data"
        ]["scenarios"]
        scenario = next(
            (x for x in scenarios if x["scenarioName"] == scenario_name), None
        )
        if not scenario:
            return None

        scenario_guid = scenario["scenarioGuid"]
        return r.get(f"{self.be}scenario/{scenario_guid}", headers=self.h).json()[
            "data"
        ]

    def create_project(self, project_name):
        data = r.post(
            f"{self.be}projects",
            json={"projectName": project_name, "version": "V2"},
            headers=self.h,
        ).json()["data"]
        return data["projectGuid"]

    def create_analysis(self, analysis_name, project_guid):
        data = r.post(
            f"{self.be}projects/{project_guid}/analyses",
            json={"analysisName": analysis_name},
            headers=self.h,
        ).json()["data"]
        return data["analysisGuid"]

    def create_scenario_from_excel(
        self, excel_path, scenario_name, analysis_guid
    ) -> str:
        # get presigned urls
        presigned = r.get(
            f"{self.be}db-update/s3-presigned-url", headers=self.h
        ).json()["data"]
        presigned_url = presigned["s3PresignedUrl"]

        # upload excels to presigned urls
        with open(excel_path, "rb") as f:
            r.put(presigned_url, data=f)

        # create single scenario
        post = {"s3PresignedUrl": presigned_url, "scenarioName": scenario_name}
        data = r.post(
            f"{self.be}v2/analysis/{analysis_guid}/scenario/excel",
            json=post,
            headers=self.h,
        ).json()["data"]
        return data["scenarioGuid"]

    def create_scenario_enymap(
        self,
        scenario_name,
        analysis_id,
        techs: list[str],
        demands: list[str],
        imports: list[str],
        exports: list[str],
        poly: list,
    ):
        return enymap.create_enymap(
            self, scenario_name, analysis_id, techs, demands, imports, exports, poly
        )

    def create_variants_from_excel(self, excel_path, master_scenario_id):
        presigned_url = r.get(
            f"{self.be}db-update/s3-presigned-url", headers=self.h
        ).json()["data"]["s3PresignedUrl"]
        with open(excel_path, "rb") as f:
            r.put(presigned_url, data=f)

        data = {
            "s3PresignedUrl": presigned_url,
            "masterScenarioGuid": master_scenario_id,
            "deleteExisting": True,
        }
        resp = r.put(
            f"{self.be}scenario-variants-excel", json=data, headers=self.h
        ).json()
        return resp["data"]

    def create_variants_from_excel_dict(self, excel_dict, master_scenario_id):
        # 1. Convert the list of dicts to an Excel file in memory
        excel_buffer = io.BytesIO()
        df = pd.DataFrame(excel_dict)

        # We use 'xlsxwriter' or 'openpyxl' as the engine
        with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Variants")

        # Seek back to the start of the buffer so r.put can read it
        excel_buffer.seek(0)

        # 2. Get the presigned URL
        presigned_url_resp = r.get(
            f"{self.be}db-update/s3-presigned-url", headers=self.h
        )
        presigned_url_resp.raise_for_status()
        presigned_url = presigned_url_resp.json()["data"]["s3PresignedUrl"]

        # 3. Upload the in-memory buffer to S3
        r.put(presigned_url, data=excel_buffer)

        # 4. Trigger the existing scenario-variants-excel logic
        data = {
            "s3PresignedUrl": presigned_url,
            "masterScenarioGuid": master_scenario_id,
            "deleteExisting": True,
        }

        resp = r.put(f"{self.be}scenario-variants-excel", json=data, headers=self.h)
        if resp.status_code != 201:
            raise Exception(resp.text)

    def get_variants_excel(self, master_scenario_id):
        return r.get(
            f"{self.be}master-scenario/{master_scenario_id}/scenario-variants-excel",
            headers=self.h,
        ).json()["data"]["s3PresignedUrl"]

    def get_variants_dict(self, master_scenario_id):
        excel_url = self.get_variants_excel(master_scenario_id)
        return excel_to_dict(excel_url, ["A"])["A"]

    def delete_scenario(self, scenario_guid) -> int:
        resp = r.delete(f"{self.be}scenario/{scenario_guid}", headers=self.h)
        return resp.status_code

    def scenario_url(self, scenario_guid):
        domain = "app.dev.sympheny.com" if self.is_dev else "app.sympheny.com"
        resp = r.get(f"{self.be}scenario/{scenario_guid}", headers=self.h).json()[
            "data"
        ]
        project_id = resp["projectGuid"]
        analysis_id = resp["analysisGuid"]
        return f"https://{domain}/projects/{project_id}/analysis/{analysis_id}/scenario/{scenario_guid}"

    def close_diagram(self, scenario_guid):
        resp = r.put(
            f"{self.be}scenarios/{scenario_guid}/close-diagram", headers=self.h, data={}
        )
        return resp.status_code

    # returns presigned_url
    def generate_input_file(self, scenario_guid):
        r.put(
            f"{self.be}v2/specs",
            headers=self.h,
            json={"scenarioGuids": [scenario_guid]},
        )
        analysis_id = r.get(
            f"{self.be}scenario/{scenario_guid}", headers=self.h
        ).json()["data"]["analysisGuid"]

        scenario_name = r.get(
            f"{self.be}scenario/{scenario_guid}", headers=self.h
        ).json()["data"]["scenarioName"]
        sleep_time = 5
        for _ in range(20):
            results = r.get(f"{self.be}analysis/{analysis_id}", headers=self.h).json()[
                "data"
            ]["results"]["scenarios"]
            result_scenar = next(
                filter(lambda s: s["scenarioName"] == scenario_name, results)
            )

            if result_scenar["inputFilepath"]:
                return result_scenar["inputFilepath"]

            print(f"generate_input_file() sleep {sleep_time} sec")
            time.sleep(sleep_time)

        return None

    def get_input_file_dict(self, job_id):
        sheets = [
            "Stages",
            "Hubs",
            "Energy Carriers",
            "Imports",
            "Exports",
            "On-site Resources",
            "Demands",
            "Conversion Techs",
            "Conversion Tech Modes",
            "Storage Techs",
            "Network Techs",
            "Network Links",
        ]
        job = self.get_job(job_id)
        input_file = job["inputFile"]

        resp = r.get(input_file, timeout=30)
        file_content = io.BytesIO(resp.content)

        return excel_to_dict(file_content, sheets)

    def get_output_file_dict(self, job_id, solution_num):
        return execution_results.get_output_file_dict(self, job_id, solution_num)

    def execute_scenario(self, scenario_guid):
        execution.execute(self, scenario_guid)

    def list_jobs(self, scenario_id, status=None):
        return execution_results.list_jobs(self, scenario_id, status)

    def get_job(self, job_id):
        return execution_results.get_job(self, job_id)

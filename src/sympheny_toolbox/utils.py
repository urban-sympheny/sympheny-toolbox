import io
import time
import warnings

import pandas as pd
import requests as r
from jproperties import Properties


def load_creds_basic(path: str) -> tuple[str, str]:
    configs = load_config(path)

    username = configs.get("username").data
    password = configs.get("password").data

    return username, password


def load_config(path: str) -> Properties:
    configs = Properties()
    with open(path, "rb") as f:
        configs.load(f)

    return configs


def load_sheet_from_presigned_url(url: str, sheet: str) -> list[dict]:
    resp = r.get(url, timeout=30)
    resp.raise_for_status()

    df = pd.read_excel(io.BytesIO(resp.content), sheet_name=sheet)
    return df.to_dict(orient="records")

def get_excel_sheets(excel):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return pd.ExcelFile(excel).sheet_names

def excel_to_dict(excel, sheets):
    excel_dict = {}
    for sheet in sheets:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            df = pd.read_excel(excel, sheet_name=sheet)
            excel_dict[sheet] = df.to_dict(orient="records")

    return excel_dict


def excel_to_dict_profile(excel, sheets):
    excel_dict = {}

    for sheet in sheets:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            df = pd.read_excel(excel, sheet_name=sheet, header=1)
            profiles = {
                col: df[col].tolist()
                for col in df.columns
                if col != "Time step"  # We exclude the index column
            }
            excel_dict[sheet] = profiles

    return excel_dict

def excel_to_dict_profile_input(excel, sheet):
    profiles_dict = {}
    TARGET_LENGTH = 8760

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        # skip line 2 (idx=1)
        df = pd.read_excel(
            excel,
            sheet_name=sheet,
            header=0,
            skiprows=[1],
            index_col=0
        )

        df = df.fillna(0)

        for col_name in df.columns:
            data = df[col_name].values.tolist()
            current_len = len(data)
            if current_len < TARGET_LENGTH:
                data.extend([0.0] * (TARGET_LENGTH - current_len))
            else:
                data = data[:TARGET_LENGTH]

            profiles_dict[col_name] = data

    return profiles_dict

def wait_until(request_fn, check_fn, wait_sec: int = 5, max_retries: int = 100):
    for _ in range(max_retries):
        resp = request_fn()
        is_done = check_fn(resp)
        if is_done:
            print("background job done")
            return resp

        print(f"not done, sleep {wait_sec} sec")
        time.sleep(wait_sec)
    raise TimeoutError("Background job did not complete in time.")

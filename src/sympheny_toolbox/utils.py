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

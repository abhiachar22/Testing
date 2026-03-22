import os
import pandas as pd

def read_excel_as_dicts(relative_path: str, sheet_name: str):
    """
    Reads an Excel sheet and returns list of dicts.
    relative_path example: "data/Testcase.xlsx"
    sheet_name example: "Login"
    """
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    excel_path = os.path.join(project_root, relative_path)

    df = pd.read_excel(excel_path, sheet_name=sheet_name, engine="openpyxl")
    df = df.fillna("")  # replace NaN with empty strings
    return df.to_dict(orient="records")
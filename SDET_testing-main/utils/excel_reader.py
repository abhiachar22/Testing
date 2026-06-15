import os
import pandas as pd

def read_excel(relative_path, sheet="Login"):
    path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        relative_path
    )

    xl = pd.ExcelFile(path, engine="openpyxl")
    sheet = next((s for s in xl.sheet_names if s.strip().lower() == sheet.lower()), None)

    if not sheet:
        raise ValueError(f"Sheet not found. Available sheets: {xl.sheet_names}")

    return pd.read_excel(path, sheet_name=sheet, engine="openpyxl")\
             .fillna("")\
             .to_dict(orient="records")
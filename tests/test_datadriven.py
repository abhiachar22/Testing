import re
from playwright.sync_api import Page, expect
import pytest


from pathlib import Path
import json, csv, pytest

def get_test_data():
    base = Path(__file__).parent
    csv_path = base / "data" / "data.csv"
    json_path = base / "data" / "credentials.json"
    data = []
    if csv_path.exists():
        with csv_path.open(newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append((row.get('username'), row.get('password')))
        return data
    if json_path.exists():
        with json_path.open() as f:
            j = json.load(f)
            creds = j.get('user_credentials', [])
            for c in creds:
                data.append((c.get('username'), c.get('password')))
        return data
    return []

@pytest.mark.parametrize("username,password", get_test_data())


def test_example(page: Page,username,password) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Performance")).to_be_visible()
import pytest
from playwright.sync_api import expect
from utils.excel_reader import read_excel_as_dicts

TEST_DATA = read_excel_as_dicts("data/Testcase.xlsx", "Login")

@pytest.mark.parametrize("row", TEST_DATA, ids=lambda r: r.get("test_case", "TC"))
def test_login_with_excel_data(page, row):
    # ✅ Always open real login route
    page.goto("https://rahulshettyacademy.com/client/auth/login")

    # ✅ Stable locators (avoid placeholder mismatch issues)
    email = page.placeholder("email@example.com")
    password = page.placeholder("enter your password")
    login_btn = page.get_by_role("button", name="Login")

    expect(email).to_be_visible(timeout=10000)
    expect(password).to_be_visible(timeout=10000)

    email.fill(str(row.get("username", "")))
    password.fill(str(row.get("password", "")))
    login_btn.click()

    expected = str(row.get("expected_result", "")).strip().lower()

    if expected == "passed":
        # ✅ Successful login check
        expect(page.get_by_role("button", name=" Sign Out ")).to_be_visible(timeout=10000)

    elif expected == "failed":
        # ✅ Failed login: toast validation
        # Try common toast containers (pick the one that matches your app)
        toast = page.locator("#toast-container, .toast-container, .ngx-toastr, [role='alert']").first
        expect(toast).to_be_visible(timeout=10000)

        expected_toast = str(row.get("expected_toast", "")).strip()
        actual_toast = toast.inner_text().strip()
        print(f"[{row.get('test_case')}] Toast shown: {actual_toast}")

        if expected_toast:
            expect(toast).to_contain_text(expected_toast, timeout=10000)

    else:
        raise ValueError(f"Invalid expected_result in Excel for {row.get('test_case')}: {row.get('expected_result')}")
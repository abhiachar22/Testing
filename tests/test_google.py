import re
from playwright.sync_api import expect

def test_google_search(page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")

    try:
        page.get_by_role("button", name = "Accept all").click(Timeout = 50000)
    except:
        print("No popup to accept")

    page.get_by_role("combobox", name="Search").fill("Playwright")

    page.keyboard.press("Enter") 
    expect(page).to_have_title(re.compile("Playwright",re.IGNORECASE))



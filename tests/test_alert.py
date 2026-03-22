
from playwright.sync_api import Page

def test_alert(page:Page):

    page.on("dialog", lambda dialog: dialog.accept())
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
   # page.get_by_role("button", name="Confirm").click()

    page.get_by_role("button", name="Mouse Hover").hover()
    page.get_by_role("link", name="Reload").click()

    page.wait_for_timeout(5000)


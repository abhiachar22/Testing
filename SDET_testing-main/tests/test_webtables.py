
from conftest import page
from playwright.sync_api import expect


#Frame handling 
def test_tables(page):
   page.goto("https://rahulshettyacademy.com/AutomationPractice/")
   page_locator = page.frame_locator("#courses-iframe")

   page_locator.get_by_role("link", name="All Access plan").click()

   page.wait_for_timeout(5000)


#Table handling
def test_tables(page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
      if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
        column_index = index
        print(f"found column index: {column_index}")
        break;
   
    row_index = page.locator("tr").filter(has_text="Rice")

    expect(row_index.locator("td").nth(column_index)).to_have_text("37")


           
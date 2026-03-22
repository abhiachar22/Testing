 

from playwright.sync_api import Page, expect
from conftest import page


def test_ui_validation(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.get_by_role("textbox", name="Password").fill("secret_sauce")

    page.locator()

    page.get_by_role("button", name="Login").click()

    bag = page.locator(".inventory_item ").filter(has_text="Sauce Labs Backpack")
    bag.get_by_role("button", name="Add to cart").click()

    bag = page.locator(".inventory_item ").filter(has_text="Sauce Labs Bike Light")
    bag.get_by_role("button", name="Add to cart").click()


    page.on("")
    
    #page.get_by_role("button", name="Add to cart").click()
    page.locator("#shopping_cart_container").click()

    expect(page.locator(".cart_item")).to_have_count(2)
    page.get_by_role("button", name="Checkout").click()

    page.get_by_role("textbox", name="First Name").fill("John")
    page.get_by_role("textbox", name="Last Name").fill("Doe")
    page.get_by_role("textbox", name="Zip/Postal Code").fill("12345")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Finish").click()


    page.wait_for_timeout(5000)





    

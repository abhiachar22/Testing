
import json
import pytest
from playwright.sync_api import Playwright, expect
from PageObjects.Dashborad import DashboardPage
from PageObjects.Orderdetails import orderdetailspage
from PageObjects.Orderhistory import orderhistorypage
from PageObjects.loginclass import LoginPage
from utils.api_base import APIUtils

with open("data/credentials.json") as f:  # Corrected file name
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data["user_credentials"]  # Corrected key

@pytest.mark.parametrize('credentials', user_credentials_list)
def test_e2e_api(playwright: Playwright, credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create order using API
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright,credentials)
    print(f"Order ID: {order_id}")  # Debug print

    # Login

    login_page = LoginPage(page)
    login_page.navigate_to_login_page()
    login_page.login(credentials)
    login_page.click_login()



    # Navigate to dashborad and click on order history
    dashborad_page = DashboardPage(page)
    dashborad_page.order_navigation()

    # Find and click the order row
    order_history = orderhistorypage(page)
    order_history.order_click(order_id)

    # Assertion page for the order details
    order_details = orderdetailspage(page)
    order_details.assertion_order_details()
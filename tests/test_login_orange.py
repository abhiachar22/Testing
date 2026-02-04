import re
from playwright.sync_api import Page, expect


from conftest import page
from pages.ORM_Home_page import home_page
from pages.ORM_login_page import login_page

def test_example(page:Page) -> None:
    loginpage = login_page(page)
    homepage = home_page(page) 

    Page.goto(page,"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    loginpage.enter_username("Admin")
    loginpage.enter_password("admin123")
    loginpage.click_login() 

    homepage.click_dashboard()
    homepage.click_recruitment()







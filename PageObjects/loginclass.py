# from conftest import credentials


class LoginPage:
    
    def __init__(self,page):
        self.page=page



    def navigate_to_login_page(self):
        self.page.goto("https://rahulshettyacademy.com/client")
       
    def login(self,credentials):
        self.page.get_by_placeholder("email@example.com").fill(credentials["username"])
        self.page.get_by_placeholder("enter your passsword").fill(credentials["password"])

    def click_login(self):
        self.page.get_by_role("button", name="Login").click()
        self.page.wait_for_load_state("networkidle")

    

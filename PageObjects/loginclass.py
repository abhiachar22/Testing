# from conftest import credentials


class LoginPage:
    
    def __init__(self,page):#init method is used to initialize the class and it takes the page object as an argument
        self.page=page#page object is used to interact with the web page and it is passed as an argument to the init method and it is assigned to the self.page variable so that it can be used in other methods of the class



    def navigate_to_login_page(self):
        self.page.goto("https://rahulshettyacademy.com/client")
       
    def login(self,credentials):
        self.page.get_by_placeholder("email@example.com").fill(credentials["username"])
        self.page.get_by_placeholder("enter your passsword").fill(credentials["password"])

    def click_login(self):
        self.page.get_by_role("button", name="Login").click()
        self.page.wait_for_load_state("networkidle")

    

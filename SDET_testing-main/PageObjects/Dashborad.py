# from conftest import credentials


class DashboardPage:
    
    def __init__(self,page):#initializing the page object
        self.page=page# passing the page object to the class variable
        
    def order_navigation(self):
        self.page.get_by_role("button", name="  ORDERS").click()
        self.page.wait_for_load_state("networkidle")

    

    

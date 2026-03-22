from playwright.sync_api import expect

class orderdetailspage:
    def __init__(self,page):
        self.page=page
    
    def assertion_order_details(self):
        expect(self.page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
        self.page.wait_for_timeout(5000)  # Optional, for observation
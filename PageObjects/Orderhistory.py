from conftest import page


class orderhistorypage:

    def __init__(self,page):
        self.page=page
    
    def order_click(self,order_id):
        row = self.page.locator("tr").filter(has_text=str(order_id))  # Ensure order_id is string
        row.get_by_role("button", name="View").click()
        self.page.wait_for_load_state("networkidle")

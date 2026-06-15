
#APIUtils is a utility class that provides methods for interacting with APIs. It can be used to create orders, retrieve data, and perform other API-related tasks.

import token
from playwright.sync_api import Playwright

order_payload = {"orders":[{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"}]} 

class APIUtils:

    def token(self,playwright:Playwright,credentials):

        usermail = credentials["username"]
        userpassword = credentials["password"]
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/api/ecom/auth/login")
        response = api_request_context.post("/api/ecom/auth/login",
                                 data = {"userEmail":usermail,"userPassword":userpassword}
                                 )
        assert response.ok
        print(response.json())
        response_json = response.json()
        return response_json["token"]
    

    def create_order(self,playwright:Playwright,credentials):

        token = self.token(playwright,credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/api/ecom/order/create-order")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data = order_payload,
                                 headers = {
                                     "content-type" : "application/json",
                                     "Authorization" : token})
        print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId




def test_api_get(playwright):
    request = playwright.request.new_context(
        extra_http_headers={"Content-Type": "application/json",
                            "Accept": "application/json",
                            "Authorization": "Bearer YOUR_API_TOKEN",
                            }

    ) 
    response = request.get("https://api.restful-api.dev/objects")


    assert response.status == 200
    json_response = response.json()
    print(json_response)
    assert json_response[6]["data"]["price"] == 1849.99

    request.dispose()
    print("Test completed successfully.")
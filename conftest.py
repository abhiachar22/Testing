
import playwright
import pytest
from playwright.sync_api import sync_playwright


# @pytest.fixture(scope="module") #scope can be function, class, module, session
# def page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         context = browser.new_context()
#         context.tracing.start(screenshots=True, snapshots=True, sources=True)
#         page = context.new_page()
#         #print("Launching the browser")
#         yield page
#         #print("Closing the browser")
#         context.tracing.stop(path="trace.zip")
#         context.close()
#         browser.close()

@pytest.fixture(scope="function")
def page(playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

# @pytest.fixture(scope="session")
# def credentials(request):
#     return request.param   



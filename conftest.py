# In conftest.py
from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        yield page
        context.tracing.stop(path="trace.zip")
        context.close()
        browser.close()
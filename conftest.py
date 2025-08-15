import pytest
from playwright.sync_api import sync_playwright 
from pages.base_page import BasePage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        yield browser
        browser.close()
        
@pytest.fixture
def page(browser, request):
    # Default messages if not overridden
    start_msg = getattr(request.node, "start_msg", "--- Test started ---")
    complete_msg = getattr(request.node, "complete_msg", "--- Test completed  ---")
    
    page = browser.new_page()
    base = BasePage(page)
    page.goto("https://the-internet.herokuapp.com/")
    
    base.log_status(start_msg)
    yield page
    base.log_status(complete_msg)
    page.close()
    

    
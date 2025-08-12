import re
from playwright.sync_api import Page, expect, sync_playwright

def test_digest_auth_success_with_page_fixture(page: Page) -> None:
    # Close the fixture's page to avoid leaking resources
    page.context.close()
    

    # Start our own Playwright instance so we can set http_credentials
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            http_credentials={"username": "admin", "password": "admin"}
        )
        auth_page = context.new_page()

        response = auth_page.goto("https://the-internet.herokuapp.com/digest_auth")
        assert response and response.status == 200
        expect(auth_page.locator("body")).to_contain_text("Congratulations")

        context.close()
        browser.close()
   
    

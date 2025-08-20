from playwright.sync_api import Page, expect

class BasicAuthPage:
    URL = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
    
    def __init__(self, page: Page):
        self.page = page
        
    def load(self):
        print("[LOG] Navigating to Basic Auth page...")
        self.page.goto(self.URL)

    def get_success_message(self):
        print("[LOG] Fetching success message text...")
        return self.page.locator(self.content_locator)

    def assert_success_message(self, expected_text: str):
        print(f"[LOG] Verifying success message is: '{expected_text}'")
        expect(self.get_success_message()).to_have_text(expected_text)
        print("[LOG] Success message verified ✅")

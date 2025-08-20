from playwright.sync_api import Page, expect

class ForgotPasswordPage:
    URL = "https://the-internet.herokuapp.com/forgot_password"

    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("#email")
        self.retrieve_btn = page.locator("#form_submit")
        self.confirmation_text = page.locator("h1")

    def load(self):
        self.page.goto(self.URL)

    def submit_email(self, email: str):
        self.email_input.fill(email)
        self.retrieve_btn.click()

    def get_confirmation_text(self) -> str:
        return self.confirmation_text.text_content().strip()

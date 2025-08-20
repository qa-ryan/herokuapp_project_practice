from playwright.sync_api import Page

class FormAuthentication:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page: Page):
        self.page = page
        # locators
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_btn = page.locator("button[type='submit']")
        self.logout_btn = page.locator("a[href='/logout']")
        self.heading = page.locator("h2")
        self.flash_msg = page.locator("#flash")

    def load(self):
        self.page.goto(self.URL)

    def input_username(self, username: str = "tomsmith"):
        self.username_input.fill(username)

    def input_password(self, password: str = "SuperSecretPassword!"):
        self.password_input.fill(password)

    def login_button(self):
        self.login_btn.click()

    def logout_button(self):
        self.logout_btn.click()

    def get_flash_message(self):
        return self.flash_msg.inner_text()

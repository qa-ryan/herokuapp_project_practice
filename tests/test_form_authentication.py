from playwright.sync_api import Page, expect
from pages.form_authentication_page import FormAuthentication
import pytest

USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"

@pytest.fixture(autouse=True)
def custom_messages(request):
    print(f"\n--- {request.node.name} test started ---")
    yield
    print(f"--- {request.node.name} test completed ---")

# TC-001: Verify login page is displayed
def test_login_page_displayed(page: Page):
    form = FormAuthentication(page)
    form.load()
    expect(page.locator("h2")).to_contain_text("Login Page")
    print("[✔] Login Page heading is displayed")

# TC-002: Successful login with valid credentials
def test_login_success(page: Page):
    form = FormAuthentication(page)
    form.load()
    form.input_username(USERNAME)
    form.input_password(PASSWORD)
    form.login_button()
    expect(page.locator("h2")).to_contain_text("Secure Area")
    print("[✔] Logged in successfully, Secure Area heading visible")

# TC-003: Logout after successful login
def test_logout_success(page: Page):
    form = FormAuthentication(page)
    form.load()
    form.input_username(USERNAME)
    form.input_password(PASSWORD)
    form.login_button()
    form.logout_button()
    expect(page.locator("h2")).to_contain_text("Login Page")
    print("[✔] Logout successful, returned to Login Page")

# TC-004: Unsuccessful login with invalid username
def test_login_invalid_username(page: Page):
    form = FormAuthentication(page)
    form.load()
    form.input_username("wronguser")
    form.input_password(PASSWORD)
    form.login_button()
    expect(page.locator("#flash")).to_contain_text("Your username is invalid!")
    print("[✔] Error message displayed for invalid username")

# TC-005: Unsuccessful login with invalid password
def test_login_invalid_password(page: Page):
    form = FormAuthentication(page)
    form.load()
    form.input_username(USERNAME)
    form.input_password("wrongpass")
    form.login_button()
    expect(page.locator("#flash")).to_contain_text("Your password is invalid!")
    print("[✔] Error message displayed for invalid password")

# TC-006: Empty username and password
def test_login_empty_credentials(page: Page):
    form = FormAuthentication(page)
    form.load()
    form.input_username("")  # assuming method supports empty input
    form.input_password("")  
    form.login_button()
    expect(page.locator("#flash")).to_contain_text("Your username is invalid!")
    print("[✔] Error message displayed for empty credentials")

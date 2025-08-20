import pytest
from pages.forgot_password_page import ForgotPasswordPage
from playwright.sync_api import expect

def test_forgot_password_flow(page):
    forgot = ForgotPasswordPage(page)
    forgot.load()
    print("\n[1] Forgot Password page loaded")

    # Submit email
    email = "user@example.com"
    forgot.submit_email(email)
    print(f"[2] Submitted email: {email}")

    # Check confirmation text
    confirmation = forgot.get_confirmation_text()
    print(f"[3] Confirmation text received: {confirmation}")

    # Assertion
    expect(page.locator("h1")).to_have_text("Internal Server Error")
    print("[4] Forgot Password request triggered (server responds with 500 intentionally)")

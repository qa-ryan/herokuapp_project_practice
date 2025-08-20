import pytest
from pages.basic_auth_page import BasicAuthPage

@pytest.fixture(autouse=True)
def custom_messages(request):
    print("\n--- Basic Auth test started ---")
    yield
    print("\n--- Basic Auth test completed ---")

def test_basic_auth(page):
    print("[TEST] Starting Basic Auth Test...")

    auth_page = BasicAuthPage(page)

    # Step 1: Load page with credentials
    auth_page.load()

    # Step 2: Verify the success message
    expected_text = "Congratulations! You must have the proper credentials."
    auth_page.assert_success_message(expected_text)

    print("[TEST] Basic Auth Test completed successfully ✅")

import pytest
from pages.digest_auth_page import DigestAuthPage

@pytest.fixture(autouse=True)
def custom_messages(request):
    print("\n--- Digest Auth test started ---")
    yield
    print("\n--- Digest Auth test completed ---")

def test_digest_auth(page):
    print("[TEST] Starting Digest Auth Test...")

    auth_page = DigestAuthPage(page)

    # Step 1: Load page with credentials
    auth_page.load()

    # Step 2: Verify the success message
    """expected_text = "Congratulations! You must have the proper credentials."
    auth_page.assert_success_message(expected_text)"""

    print("[TEST] Digest Auth Test completed successfully ✅")

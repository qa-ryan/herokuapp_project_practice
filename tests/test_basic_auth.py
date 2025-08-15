
from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def custom_messages(request):
    request.node.start_msg = "--- Basic Auth test started ---"
    request.node.complete_msg = "--- Basic Auth test completed ---"

def test_basic_auth_authorized(page: Page) -> None:
    print("\nTest Case 1: Authorized test started...")
    
    context = page.context
    context.set_extra_http_headers({
        "Authorization": "Basic YWRtaW46YWRtaW4=" # Base64 encoded 'admin:admin'
    })
    
    page.get_by_role("link", name="Basic Auth").click()
    expect(page.get_by_role("heading", name="Basic Auth")).to_be_visible()
    
    print("\nTest Case 1: Authorized test completed...")
    

def test_basic_auth_unauthorized(page: Page) -> None:
    print("\nTest Case 2: Unauthorized test started...")
    
    context = page.context
    context.set_extra_http_headers({
        "Authorization": "Basic bm9uYWRtaW46YWRtaW4=" # Base64 encoded 'nonadmin:admin'
    })
    
    page.get_by_role("link", name="Basic Auth").click()
    expect(page.get_by_role("heading", name="Basic Auth")).not_to_be_visible()
    
    print("\nTest Case 2: Unauthorized test completed...")



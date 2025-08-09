
from playwright.sync_api import Page, expect


def test_basic_auth_authorized(page: Page) -> None:
    
    print("\nStarting Authorize test...\n")

    page.goto("https://the-internet.herokuapp.com/")
    
    context = page.context
    context.set_extra_http_headers({
        "Authorization": "Basic YWRtaW46YWRtaW4=" # Base64 encoded 'admin:admin'
    })
    
    page.get_by_role("link", name="Basic Auth").click()
    expect(page.get_by_role("heading", name="Basic Auth")).to_be_visible()
    
    print("\n✅ Authorized test passed!\n")
    print("\nAuthorize test completed successfully.\n")

def test_basic_auth_unauthorized(page: Page) -> None:
    
    print("\nStarting Unauthorize test...\n")

    page.goto("https://the-internet.herokuapp.com/")
    
    context = page.context
    context.set_extra_http_headers({
        "Authorization": "Basic bm9uYWRtaW46YWRtaW4=" # Base64 encoded 'nonadmin:admin'
    })
    
    page.get_by_role("link", name="Basic Auth").click()
    expect(page.get_by_role("heading", name="Basic Auth")).not_to_be_visible()
    

    print("\n✅ Unauthorized test passed!\n")
    print("\nUnauthorize test completed successfully.\n")
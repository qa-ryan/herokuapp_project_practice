from playwright.sync_api import Page, expect
import pytest


@pytest.fixture(autouse=True)
def custom_messages(request):
    request.node.start_msg = "--- AB Testing test started ---"
    request.node.complete_msg = "--- AB Testing test completed ---"
    
def dynamic_content_page_setup(page: Page) -> None:
    page.get_by_role("link", name="Dynamic Content").click()
    expect(page.get_by_role("heading")).to_contain_text("Dynamic Content")

def test_dynamic_content(page: Page) -> None:
    dynamic_content_page_setup(page)
    print("\nStarting Dynamic Content test...\n")
    
    max_count = 3

    for i in range(max_count):
        print(f"\nRefresh Page {i + 1} of {max_count}...\n")
        
        items = page.locator("#content img").all()
        for item in items:
            img = item.get_attribute("src")
            print(f"\n: {img}")
            
        page.reload()

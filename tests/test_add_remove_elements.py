from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def custom_messages(request):
    request.node.start_msg = "--- Add Remove Elements test started ---"
    request.node.complete_msg = "--- Add Remove Elements test completed ---"

def test_add_remove_elements(page:Page) -> None:    
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Add/Remove Elements").click()
    
    expect(page.get_by_role("heading")).to_contain_text("Add/Remove Elements")

    for i in range(10):
        page.get_by_role("button", name="Add Element").click()
        print(f"Added element {i + 1}")
    
    for j in range(4):
        page.get_by_text("Delete").nth(0).click()
        print(f"Deleted element {j + 1}")

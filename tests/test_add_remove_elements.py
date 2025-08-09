import re
from playwright.sync_api import Page, expect


def test_add_remove_elements(page:Page) -> None:

    print("\nStarting Add/Remove Elements Testing test...\n")
    
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Add/Remove Elements").click()
    
    expect(page.get_by_role("heading")).to_contain_text("Add/Remove Elements")

    
    for i in range(10):
        page.get_by_role("button", name="Add Element").click()
        print(f"Added element {i + 1}")
    
    for j in range(4):
        page.get_by_text("Delete").nth(0).click()
        print(f"Deleted element {j + 1}")
  
    print("\nA/B Add/Remove Elements test completed successfully.\n")
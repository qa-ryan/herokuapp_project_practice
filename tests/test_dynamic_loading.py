from playwright.sync_api import Page, expect
import pytest
import random
import string

@pytest.fixture(autouse=True)
def custom_messages(request):
    request.node.start_msg = "--- Dynamic Loading test started ---"
    request.node.complete_msg = "--- Dynamic Loading test completed ---"
    
def test_dyanmic_loading(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dynamic_loading")
    print("Test Case 1: Element on page that is hidden test started...")
    page.get_by_role("link", name="Example 1: Element on page").click()
    expect(page.locator("#content")).to_contain_text("Example 1: Element on page that is hidden")
    page.get_by_role("button", name="Start").click()
    hello_wrld = page.get_by_role("heading", name="Hello World!").text_content()
    expect(page.get_by_role("heading", name="Hello World!"))
    print(hello_wrld)
    print("Test Case 1: Element on page that is hidden test completed...")
    
def test_dynamic_loading_2(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dynamic_loading")
    print("Test Case 2: Element rendered after the fact test started...")
    page.get_by_role("link", name="Example 2: Element rendered").click()
    expect(page.locator("#content")).to_contain_text("Example 2: Element rendered after the fact")
    page.get_by_role("button", name="Start").click()
    hello_wrld = page.get_by_role("heading", name="Hello World!").text_content()
    expect(page.get_by_role("heading", name="Hello World!"))
    print(hello_wrld)
    print("Test Case 2: Element rendered after the fact test completed...")
from playwright.sync_api import Page, expect
import pytest
import random
import string

@pytest.fixture(autouse=True)
def custom_messages(request):
    request.node.start_msg = "--- Dynamic Control test started ---"
    request.node.complete_msg = "--- Dynamic Control test completed ---"
    

def test_remove_add(page: Page) -> None:
    print("\nTest Case 1: Remove/add test started...")
    page.get_by_role("link", name="Dynamic Controls").click()
    
    expect(page.locator("#content")).to_contain_text("Dynamic Controls")
    expect(page.locator("#content")).to_contain_text("Remove/add")
    expect(page.locator("#content")).to_contain_text("Enable/disable")
    
    checkboxes = page.locator("input[type='checkbox']")
    count = checkboxes.count()
    
    print(f"\nNumber of checkboxes on the page: {count}\n")
    
    for i in range(count):
        cb = checkboxes.nth(i)
        print(f"Checkbox {i + 1} is {'checked' if cb.is_checked() else 'unchecked'}")
        
    for i in range(5):
        if page.get_by_role("button", name="Remove").is_visible():
            expect(page.get_by_role("button", name="Remove")).to_be_visible()
            page.get_by_role("button", name="Remove").click()
            expect(page.locator("#message")).to_contain_text("It's gone!")
            if page.get_by_text("It's gone!").is_visible():
                print(f"\n[{i+1}] Remove button pressed", flush=True)
                print("--> It's gone!")
            
            if page.locator("input[type='checkbox']").is_visible():
                print("--> Checkbox ready")
            else:
                print("--> Checkbox removed")
            
        elif page.get_by_role("button", name="Add").is_visible():
            expect(page.get_by_role("button", name="Add")).to_be_visible()
            page.get_by_role("button", name="Add").click()
            expect(page.locator("#message")).to_contain_text("It's back!")
            if page.get_by_text("It's back!").is_visible():
                print(f"\n[{i+1}] Add button pressed", flush=True)
                print("--> It's back!")
                
            if page.locator("input[type='checkbox']").is_visible():
                print("--> Checkbox ready")
            else:
                print("-->Checkbox removed")
            
    print("\nTest Case 1: Remove/add test completed...")
    
def test_enable_disable(page: Page) -> None:
    print("\nTest Case 2: Enable/Disable test started...")
    page.get_by_role("link", name="Dynamic Controls").click()
    
    for i in range(5):
        if page.get_by_role("button", name="Enable").is_visible():
            expect(page.get_by_role("button", name="Enable")).to_be_visible()
            page.get_by_role("button", name="Enable").click()
            expect(page.locator("#message")).to_contain_text("It's enabled!")
            if page.get_by_text("It's enabled!").is_visible():
                print(f"\n[{i+1}] Enable button pressed", flush=True)
                print("--> It's enabled!")
                
            random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
               
            if page.get_by_role("textbox").is_enabled():
                 page.get_by_role("textbox").click()
                 page.get_by_role("textbox").fill(random_text)
                 print(f"--> Random text: {random_text}")
            elif page.get_by_role("textbox").is_disabled():
                print("--> Input field is disabled")
            else:
                print("--> Can't found input field")
            
        elif page.get_by_role("button", name="Disable").is_visible():
            expect(page.get_by_role("button", name="Disable")).to_be_visible()
            page.get_by_role("button", name="Disable").click()
            expect(page.locator("#message")).to_contain_text("It's disabled!")
            if page.get_by_text("It's disabled!").is_visible():
                print(f"\n[{i+1}] Disable button pressed", flush=True)
                print("--> It's disabled!")
            
            if page.get_by_role("textbox").is_enabled():
                 page.get_by_role("textbox").click()
                 page.get_by_role("textbox").fill(random_text)
                 print(f"--> Random text: {random_text}")
            elif page.get_by_role("textbox").is_disabled():
                print("--> Input field is disabled")
            else:
                print("--> Can't found input field")
    print("\nTest Case 2: Enable/Disable test completed...")
    
    
   
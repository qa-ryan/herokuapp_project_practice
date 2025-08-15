import re
from playwright.sync_api import Page, expect

def dropdown_page_setup(page: Page) -> None:
    page.get_by_role("link", name="Dropdown").click()
    expect(page.get_by_role("heading")).to_contain_text("Dropdown List")
    
    
# Scenario 1: Default Selection
def test_dropdown_default_selection(page):
    dropdown_page_setup(page)
    print("\nStarting Scenario 1: Dropdown Default Selection test...")
    
    default_value = page.locator("#dropdown option[selected]").text_content()
    print(f"\nDefault value: {default_value}")
    
    option_elements = page.locator("#dropdown option:not([selected])")
    count = option_elements.count()
    for i in range(count):
        text = option_elements.nth(i).text_content()
        print(f"Option {i + 1}: {text}")
    
    print(f"\nScenario 1 Completed...")
    
# Scenario 2: Select Each Option
def test_select_each_option(page: Page) -> None:
    dropdown_page_setup(page)
    print("\nStarting Scenario 2: Select Each Option test...\n")
    
    options = page.locator("#dropdown option").all()
    for option in options:
        value = option.get_attribute("value")
        if value:
            page.select_option("#dropdown", value)
            selected_value = page.locator("#dropdown").input_value()
            assert selected_value == value, f"Expected {value}, but got {selected_value}"   
            print(f"Option Selected:", selected_value)
            
    print(f"\nScenario 2 Completed...")
            
# Scenario 3: Re Select Options      
def test_reselect_option(page: Page) -> None:
    dropdown_page_setup(page)
    print("\nStarting Scenario 3: Re Select Options test...\n")
 
    page.select_option("#dropdown", "2")
    first_value = page.locator("#dropdown").input_value()
    print(f"First selected value: {first_value}")
    
    page.select_option("#dropdown", "1")
    second_value = page.locator("#dropdown").input_value()
    print(f"Second selected value: {second_value}")
    assert first_value != second_value, "Re-selecting the same option should change the value."
    
    print(f"\nScenario 3 Completed...")
    
# Scenario 4: Keyboard Navigation
def test_keyboard_navigation(page: Page) -> None:
    dropdown_page_setup(page)
    print("\nStarting Scenario 4: Keyboard Navigation test...\n")
    
    page.locator("#dropdown").focus()
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")
    
    selected_value = page.locator("#dropdown").input_value()
    print(f"Selected value after keyboard navigation: {selected_value}")
    
    assert selected_value in ["1", "2"], "Selected value should be one of the options."
    
    print(f"\nScenario 4 Completed...")

    
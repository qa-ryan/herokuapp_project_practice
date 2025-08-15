from playwright.sync_api import Page, expect


def test_checkboxes(page: Page) -> None:
    
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Checkboxes").click()
    expect(page.get_by_role("heading")).to_contain_text("Checkboxes")
    
    checkboxes = page.locator("input[type='checkbox']")
    count = checkboxes.count()
    
    print(f"\nNumber of checkboxes on the page: {count}\n")
    
    for i in range(count):
        cb = checkboxes.nth(i)
        print(f"Checkbox {i + 1} is {'checked' if cb.is_checked() else 'unchecked'}")
        
    # --- STEP 1: Initial state ---
    print("\n[Initial State]")
    for i in range(count):
        cb = checkboxes.nth(i)
        print(f"Checkbox {i+1}: {'CHECKED' if cb.is_checked() else 'UNCHECKED'}")

    # --- STEP 2: Check all unchecked boxes ---
    for i in range(count):
        cb = checkboxes.nth(i)
        if not cb.is_checked():
            cb.check()
            print(f"Checkbox {i+1} was unchecked → now CHECKED")

    # --- STEP 3: Verify after checking ---
    print("\n[After Checking All]")
    for i in range(count):
        cb = checkboxes.nth(i)
        print(f"Checkbox {i+1}: {'CHECKED' if cb.is_checked() else 'UNCHECKED'}")

    # --- STEP 4: Uncheck all boxes ---
    for i in range(count):
        cb = checkboxes.nth(i)
        cb.uncheck()
        print(f"Checkbox {i+1} → UNCHECKED")

    # --- STEP 5: Verify after unchecking ---
    print("\n[After Unchecking All]")
    for i in range(count):
        cb = checkboxes.nth(i)
        print(f"Checkbox {i+1}: {'CHECKED' if cb.is_checked() else 'UNCHECKED'}")

    # --- STEP 6: Compare is_checked() vs get_attribute("checked") ---
    print("\n[Comparison Table]")
    print(f"{'Checkbox':<10} {'is_checked()':<12} {'get_attribute("checked")'}")
    print("-" * 40)
    for i in range(count):
        cb = checkboxes.nth(i)
        is_checked_value = cb.is_checked()
        attr_value = cb.get_attribute("checked")
        print(f"{i+1:<10} {str(is_checked_value):<12} {attr_value}")
        

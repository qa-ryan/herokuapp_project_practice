from playwright.sync_api import Page, expect

class CheckboxesPage:
    URL = "https://the-internet.herokuapp.com/checkboxes"
    
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading")
        self.checkbox = page.locator("input[type='checkbox']")

    def load (self):
        """Navigate to the Chekckboxes page"""
        self.page.goto(self.URL)

    def validate_page_content(self):
        """Validate if Checkboxes poge is present"""
        expect(self.heading).to_contain_text("Checkboxes")
        
    def checkboxes(self):
        checkbox = self.checkbox
        count = checkbox.count()
        
        print(f"\nNumber of checkboxes on the page: {count}\n")
        
        for i in range(count):
            cb = checkbox.nth(i)
            print(f"Checkbox {i + 1} is {'checked' if cb.is_checked() else 'unchecked'}")
            
        # --- STEP 1: Initial state ---
        print("\n[Initial State]")
        for i in range(count):
            cb = checkbox.nth(i)
            print(f"Checkbox {i+1}: {'CHECKED' if cb.is_checked() else 'UNCHECKED'}")

        # --- STEP 2: Check all unchecked boxes ---
        for i in range(count):
            cb = checkbox.nth(i)
            if not cb.is_checked():
                cb.check()
                print(f"Checkbox {i+1} was unchecked → now CHECKED")

        # --- STEP 3: Verify after checking ---
        print("\n[After Checking All]")
        for i in range(count):
            cb = checkbox.nth(i)
            print(f"Checkbox {i+1}: {'CHECKED' if cb.is_checked() else 'UNCHECKED'}")

        # --- STEP 4: Uncheck all boxes ---
        for i in range(count):
            cb = checkbox.nth(i)
            cb.uncheck()
            print(f"Checkbox {i+1} → UNCHECKED")

        # --- STEP 5: Verify after unchecking ---
        print("\n[After Unchecking All]")
        for i in range(count):
            cb = checkbox.nth(i)
            print(f"Checkbox {i+1}: {'CHECKED' if cb.is_checked() else 'UNCHECKED'}")

        
            

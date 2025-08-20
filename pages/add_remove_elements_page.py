from playwright.sync_api import Page, expect

class AddRemovePage:
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading")
        self.add = page.get_by_role("button", name="Add Element")
        self.delete = page.get_by_text("Delete").nth(0)

    def load (self):
        """Navigate to the Add Remove Elements page"""
        self.page.goto(self.URL)

    def validate_page_content(self):
        """Validate if Add Remove Elements poge is present"""
        expect(self.heading).to_contain_text("Add/Remove Elements")
        
    def add_element(self):
        """Function to add element"""
        for i in range(100):
            self.add.click()
            print(f"Added element {i + 1}")
    
    def delete_element(self):
        """Function to delete element"""
        for j in range(50):
            self.delete.click()
            print(f"Deleted element {j + 1}")

        

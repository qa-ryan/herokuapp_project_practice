from playwright.sync_api import Page, expect

class BrokenImagePage:
    URL = "https://the-internet.herokuapp.com/broken_images"
    
    def __init__(self, page: Page):
        self.page = page
    
    def load(self):
        """Navigate to the Broken Image Testing page"""
        self.page.goto(self.URL)

    def validate_page_content(self):
        """Validate Page Title is present"""
        expect(self.page.get_by_role("heading")).to_contain_text("Broken Images")
    
    def broken_images(self):
        images = self.page.locator("img")
        count = images.count()
        
        print(f"Number of images on the page: {count}")
        
        broken_count = 0
        for i in range(count):
            img = images.nth(i)
            src = img.get_attribute("src")
            natural_width = img.evaluate("img => img.naturalWidth")

            if natural_width == 0:
                print(f"❌ Broken image: {src}")
                broken_count += 1
            else:
                print(f"✅ Working image: {src}")

        print(f"\nTotal broken images: {broken_count}")
        

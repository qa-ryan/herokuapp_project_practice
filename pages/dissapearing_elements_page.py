
from playwright.sync_api import Page, expect

class DisappearingElementsPage:
    
    def __init__(self, page:Page):
        self.page = page
            
    def get_gallery_url(self):
        self.page.get_by_role("link", name="Gallery").click()
        gallery_url = self.page.url
        description = self.page.get_by_role("heading")
        print(f"Gallery Description: {description.text_content()}")
        expect(description).to_contain_text("Not Found") 
        print(f"Gallery URL: {gallery_url}")

    def get_portfolio_url(self):
        self.page.get_by_role("link", name="Portfolio").click()
        portolio_url = self.page.url
        description = self.page.get_by_role("heading")
        print(f"Portfolio Description: {description.text_content()}")
        expect(description).to_contain_text("Not Found") 
        print(f"Portfolio URL: {portolio_url}")
        
    def get_contact_us_url(self):
        self.page.get_by_role("link", name="Contact Us").click()
        contact_us_url = self.page.url
        description = self.page.get_by_role("heading")
        print(f"Contact Us Description: {description.text_content()}")
        expect(description).to_contain_text("Not Found")
        print(f"Contact Us URL: {contact_us_url}")

    def get_about_url(self):
        self.page.get_by_role("link", name="About").click()
        about_url = self.page.url
        description = self.page.get_by_role("heading")
        print(f"About Description: {description.text_content()}")
        expect(description).to_contain_text("Not Found")
        print(f"About URL: {about_url}")

    def get_home_url(self):
        self.page.get_by_role("link", name="Home").click()
        home_url = self.page.url
        #description = self.page.get_by_role('heading', { name: 'Welcome to the-internet' })
        #print(f"Home Description: {description.text_content()}")
        #expect(description).to_contain_text("Welcome to the-internet")
        print(f"Home URL: {home_url}")
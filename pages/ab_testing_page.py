from playwright.sync_api import Page, expect

class ABTestingPage:
    URL = "https://the-internet.herokuapp.com/abtest"

    TEXT_A = "A/B Test Variation 1"
    TEXT_B = "A/B Test Control"
    TEXT_DESCRIPTION = (
        "Also known as split testing. This is a way in which businesses are able "
        "to simultaneously test and learn different versions of a page to see which "
        "text and/or functionality works best towards a desired outcome (e.g. a user "
        "action such as a click-through)."
    )

    def __init__(self, page: Page):
        self.page = page
    
    def load(self):
        """Navigate to the A/B Testing page"""
        self.page.goto(self.URL)

    def validate_page_content(self):
        """Validate if A or B variation is present"""
        content = self.page.content()

        if self.TEXT_A in content:
            expect(self.page.get_by_role("heading")).to_contain_text(self.TEXT_A)
            expect(self.page.get_by_role("paragraph")).to_contain_text(self.TEXT_DESCRIPTION)
            print("\n✅ A/B Test Variation 1 is present in the page content.")
            return "Variation A"

        elif self.TEXT_B in content:
            expect(self.page.get_by_role("heading")).to_contain_text(self.TEXT_B)
            expect(self.page.get_by_role("paragraph")).to_contain_text(self.TEXT_DESCRIPTION)
            print("\n✅ A/B Test Control is present in the page content.")
            return "Variation B"

        else:
            raise AssertionError("❌ Neither Variation A nor Variation B found on page.")

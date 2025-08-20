from playwright.sync_api import Page, expect

class FloatingMenuPage:
    URL = "https://the-internet.herokuapp.com/floating_menu"

    def __init__(self, page: Page):
        self.page = page
        self.menu = page.locator("#menu")
        self.footer = page.locator("#page-footer")
        self.header = page.locator("h3")

    def load(self):
        self.page.goto(self.URL)

    def is_menu_visible(self) -> bool:
        return self.menu.is_visible()

    def scroll_to_footer(self):
        self.footer.scroll_into_view_if_needed()

    def get_menu_position(self):
        # Returns bounding box for menu: { x, y, width, height }
        return self.menu.bounding_box()

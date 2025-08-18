from playwright.sync_api import Page, expect


def test_entry_ad(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/entry_ad")
    
    if page.locator("#modal").is_visible():
        expect(page.locator("#modal")).to_contain_text("This is a modal window")
        expect(page.locator("#modal")).to_contain_text("It's commonly used to encourage a user to take an action (e.g., give their e-mail address to sign up for something or disable their ad blocker).")
        print("Entry ad shwon...")
        page.get_by_text("Close", exact=True).click()
    elif page.locator("#modal").is_hidden():
        page.get_by_role("link", name="click here").click()
        
        page.get_by_role("link", name="Elemental Selenium").click()
        page.close()
        page.goto("https://the-internet.herokuapp.com/entry_ad")
        page.get_by_role("link", name="click here").click()
        page.reload()

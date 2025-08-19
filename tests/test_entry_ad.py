from playwright.sync_api import Page, expect
import time


def test_entry_ad(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/entry_ad")
    modal = page.locator("#modal")
    close_btn = page.get_by_text("Close", exact=True)
    trigger_link = page.get_by_role("link", name="click here")

    for attempt in range(1, 11):
        time.sleep(5)  # give modal a chance to appear

        if modal.is_visible():
            expect(modal).to_contain_text("This is a modal window")
            expect(modal).to_contain_text(
                "It's commonly used to encourage a user to take an action"
            )
            print(f"[{attempt}] Entry ad is visible ✅")
            close_btn.click()

        else:
            print(f"[{attempt}] Entry ad is hidden ❌")
            trigger_link.click()
            page.reload()
            print("   → Page reloaded to re-trigger modal")
            
            
           
    
    
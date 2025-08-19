from playwright.sync_api import Page, expect
import time


def test_exit_intent(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/exit_intent")
    modal = page.locator("#ouibounce-modal")
    close_button = page.get_by_text("Close", exact=True)

    for attempt in range(1, 6):
        time.sleep(2)  # pause between attempts

        # Trigger exit intent by moving mouse outside the viewport (top side)
        page.mouse.move(200, 200)     # start inside
        page.wait_for_timeout(500)
        page.mouse.move(200, -10)     # exit outside (top)

        if modal.is_visible():
            expect(modal).to_contain_text("This is a modal window")
            expect(modal).to_contain_text(
                "It's commonly used to encourage a user to take an action"
            )
            print(f"[{attempt}] Exit intent modal is visible ✅")
            close_button.click()
            expect(modal).to_be_hidden(timeout=3000)
            print("   → Modal closed")

        else:
            print(f"[{attempt}] Modal did not appear ❌")
            # Reload page and retry triggering modal
            page.reload()
            page.wait_for_load_state("domcontentloaded")
            print("   → Page reloaded to re-trigger modal")

            # Try again right after reload
            page.mouse.move(300, 300)
            page.wait_for_timeout(500)
            page.mouse.move(300, -10)

            if modal.is_visible():
                print("   → Modal appeared after reload 🔄")
                close_button.click()
                expect(modal).to_be_hidden(timeout=3000)
            else:
                print("   → Still no modal after reload ❌")
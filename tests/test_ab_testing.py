from playwright.sync_api import Page, expect


def test_ab_testing(page:Page) -> None:
    text_A = "A/B Test Variation 1"
    text_B = "A/B Test Control"
    text_description = "Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through)."

    print("\nStarting A/B Testing test...\n")
    
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="A/B Testing").click()
    
    if text_A in page.content():
        expect(page.get_by_role("heading")).to_contain_text(text_A)
        expect(page.get_by_role("paragraph")).to_contain_text(text_description)
        print("A/B Test Variation 1 is present in the page content.")
        
    elif text_B in page.content():
        expect(page.get_by_role("heading")).to_contain_text(text_B)
        expect(page.get_by_role("paragraph")).to_contain_text(text_description)
        print("A/B Test Control is present in the page content.")
        
    else:
        raise AssertionError("Neither A/B Test Variation 1 nor A/B Test Control found in page content.")

    print("\nA/B Testing test completed successfully.\n")
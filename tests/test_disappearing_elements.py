import re
from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError
from pages.dissapearing_elements_page import DisappearingElementsPage
from urllib.parse import urljoin


def test_disappearing_elements_test_case_1(page: Page) -> None:

    dissapearing_elements_page = DisappearingElementsPage(page)
    
    print("\nStarting Disappearing Elements test...\n")
    
    page.get_by_role("link", name="Disappearing Elements").click()
    expect(page.get_by_role("heading")).to_contain_text("Disappearing Elements")
    
    target_selectors = "a[href='/gallery/']"
    max_attempts = 10
    
    for attempt in range(1, max_attempts + 1):
        print(f"Attempt {attempt} of {max_attempts} to find the element...")
        
        try:
            page.wait_for_selector(target_selectors, timeout=5000)
            print("\nElement found, proceeding with the test...\n")
            break
        except PlaywrightTimeoutError:
            print("Element not found, reloading the page...")
            page.reload()
    
    
    dissapearing_elements_page.get_gallery_url()
    page.go_back()
    
    print("\n")
    
    dissapearing_elements_page.get_portfolio_url()
    page.go_back()
    
    print("\n")
    
    dissapearing_elements_page.get_contact_us_url()
    page.go_back()
    
    print("\n")
    
    dissapearing_elements_page.get_about_url()
    page.go_back()
    
    print("\n")
    
    dissapearing_elements_page.get_home_url()
    page.go_back()
    
    print("\nDissapearing test completed successfully.\n")
    

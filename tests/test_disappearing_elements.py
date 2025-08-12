import re
from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError
from pages.dissapearing_elements_page import DisappearingElementsPage
from urllib.parse import urljoin


"""def test_disappearing_elements_test_case_1(page: Page) -> None:
    
    dissapearing_elements_page = DisappearingElementsPage(page)
    
    print("\nStarting Disappearing Elements test...\n")
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Disappearing Elements").click()
    expect(page.get_by_role("heading")).to_contain_text("Disappearing Elements")
    
    target_selectors = "a[href='/gallery/']"
    max_attempts = 10
    
    for attempt in range(1, max_attempts + 1):
        print(f"Attempt {attempt} of {max_attempts} to find the element...")
        
        try:
            page.wait_for_selector(target_selectors, timeout=5000)
            print("\nElement found, proceeding with the test...]n")
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
    
    print("\nDissapearing test completed successfully.\n")"""
    
async def test_open_link_new_tab_async(page, context):
    await page.goto("https://example.com")
    
    # Get link using get_by_role
    link = page.get_by_role("link", name="Contact Us")
    link_url = await link.get_attribute("href")
    
    # Open in new tab
    new_page = await context.new_page()
    await new_page.goto(link_url)
    
    # Both tabs are open
    assert "Contact" in await new_page.title()
    assert await page.title() == "Original Title"
    
    await new_page.close()
    
def test_disappearing_elements_test_case2(page: Page, context) -> None:
    
    print("\nStarting Disappearing Elements test...\n")
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Disappearing Elements").click()
    expect(page.get_by_role("heading")).to_contain_text("Disappearing Elements")
    
    target_selectors = "a[href='/gallery/']"
    max_attempts = 10
    
    for attempt in range(1, max_attempts + 1):
        print(f"Attempt {attempt} of {max_attempts} to find the element...")
        
        try:
            page.wait_for_selector(target_selectors, timeout=5000)
            print("\nElement found, proceeding with the test...]n")
            break
        except PlaywrightTimeoutError:
            print("Element not found, reloading the page...")
            page.reload()
            
            
    link = page.get_by_role("link", name="Gallery")
    link_url = link.get_attribute("href")
    
    new_page = context.new_page()
    new_page.goto(link_url)
    
    page.pause()
    
    """gallery_url = page.url
    description = page.get_by_role("heading")
    print(f"Gallery Description: {description.text_content()}")
    expect(description).to_contain_text("Not Found") 
    print(f"Gallery URL: {gallery_url}")"""
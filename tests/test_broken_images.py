from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def custom_messages(request):
    request.node.start_msg = "---Broken Images test started ---"
    request.node.complete_msg = "--- Broken Images test completed ---"
    
def test_broken_images(page: Page) -> None:
    page.get_by_role("link", name="Broken Images").click()
    expect(page.get_by_role("heading")).to_contain_text("Broken Images")
    
    images = page.locator("img")
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
    

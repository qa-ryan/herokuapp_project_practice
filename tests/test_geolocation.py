from playwright.sync_api import Page, expect
import pytest, time


@pytest.fixture(autouse=True)
def custom_messages(request):
    request.node.start_msg = "--- Geolocation test started ---"
    request.node.complete_msg = "--- Geolocation test completed ---"
    
def test_geolocation(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/geolocation")
    
    expect(page.get_by_role("heading")).to_contain_text("Geolocation")
    expect(page.locator("#demo")).to_contain_text("Click the button to get your current latitude and longitude")
    
from playwright.sync_api import Page, expect
from pages.form_authentication_page import FormAuthentication
import pytest, time


@pytest.fixture(autouse=True)
def custom_messages(request):
    request.node.start_msg = "--- Frames test started ---"
    request.node.complete_msg = "--- Frames test completed ---"
    
def test_frames_pages(page: Page) -> None:
    page.get_by_role("link", name="Frames", exact=True).click()
    expect(page.get_by_role("list")).to_contain_text("Nested Frames")
    expect(page.get_by_role("list")).to_contain_text("iFrame")
    
    
def test_count_frames(page: Page):
    # Example URL with nested frames (The Internet Herokuapp)
    page.goto("https://the-internet.herokuapp.com/nested_frames")

    # Get all frames in the page
    frames = page.frames

    print(f"Total frames found: {len(frames)}")

    # List frame names
    for idx, frame in enumerate(frames):
        print(f"[{idx}] Frame name: {frame.name or 'No name'} | URL: {frame.url}")

    # Example: Access specific frame
    top_frame = page.frame(name="frame-top")
    if top_frame:
        print("✅ Found 'frame-top'")
        # Access child frame
        left_frame = top_frame.child_frames[0]
        print(f"Child frame name: {left_frame.name or 'No name'}")
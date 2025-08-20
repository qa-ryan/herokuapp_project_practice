from pages.broken_image_page import BrokenImagePage
import pytest

@pytest.fixture(autouse=True)
def custom_messages(request):
    request.node.start_msg = "---Broken Images test started ---"
    request.node.complete_msg = "--- Broken Images test completed ---"
    
def test_broken_images(page):
    broken = BrokenImagePage(page)
    
    broken.load()
    broken.broken_images()
    
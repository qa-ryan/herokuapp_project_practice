import pytest
from pages.ab_testing_page import ABTestingPage

@pytest.fixture(autouse=True)
def custom_messages(request):
    request.node.start_msg = "--- AB Testing test started ---"
    request.node.complete_msg = "--- AB Testing test completed ---"

def test_ab_testing(page):
    ab_page = ABTestingPage(page)
    ab_page.load()
    variation = ab_page.validate_page_content()

    assert variation in ["Variation A", "Variation B"]
    print(f"✅ Test passed with {variation}")

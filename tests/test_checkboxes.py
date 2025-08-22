from pages.checkboxes_page import CheckboxesPage
import pytest

@pytest.fixture(autouse=True)
def custom_messages(request):
    request.node.start_msg = "--- Checkboxes test started ---"
    request.node.complete_msg = "--- Checkboxes test completed ---"
def test_checkboxes(page):
    checkbox = CheckboxesPage(page)
    checkbox.load()
    
    checkbox.checkboxes()
from pages.add_remove_elements_page import AddRemovePage
import pytest

@pytest.fixture(autouse=True)
def custom_messages(request):
    request.node.start_msg = "--- Add Remove Elements test started ---"
    request.node.complete_msg = "--- Add Remove Elements test completed ---"

def test_add_remove_elements(page) -> None:    
    add_remove = AddRemovePage(page)
    
    """Load the page then validate Page Title"""
    add_remove.load()
    add_remove.validate_page_content()
    
    """Add and Remove elemet"""
    add_remove.add_element()
    add_remove.delete_element()
    
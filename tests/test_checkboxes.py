from pages.checkboxes_page import CheckboxesPage


def test_checkboxes(page):
    checkbox = CheckboxesPage(page)
    checkbox.load()
    
    checkbox.checkboxes()
from playwright.sync_api import Page, expect

def test_drag_and_drop(page:Page) -> None:
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Drag and Drop").click()
    
    col_a_role = page.text_content("#column-a header")
    col_b_role = page.text_content("#column-b header")
    
    print(f"\nColumn A role: {col_a_role}")
    print(f"Column B role: {col_b_role}")

    col_a = page.locator("#column-a")
    col_b = page.locator("#column-b")

    box_a = col_a.bounding_box()
    box_b = col_b.bounding_box()

    page.mouse.move(box_a["x"] + box_a["width"] / 2, box_a["y"] + box_a["height"] / 2)
    page.mouse.down()
    page.mouse.move(box_b["x"] + box_b["width"] / 2, box_b["y"] + box_b["height"] / 2, steps=10)
    page.mouse.up()
    
    col_a_role = page.text_content("#column-a header")
    col_b_role = page.text_content("#column-b header")
    
    print(f"\nColumn A role: {col_a_role}")
    print(f"Column B role: {col_b_role}")

    assert page.locator("#column-a header").text_content() == "B"
    assert page.locator("#column-b header").text_content() == "A"
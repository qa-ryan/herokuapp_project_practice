import pytest
from pages.floating_menu_page import FloatingMenuPage

def test_floating_menu_stays_visible_on_scroll(page):
    floating = FloatingMenuPage(page)
    floating.load()
    print("\n[1] Page loaded")

    # Menu visible on load
    assert floating.is_menu_visible(), "Floating menu should be visible on load"
    print("[2] Floating menu is visible on page load")

    # Capture initial menu X position
    initial_pos = floating.get_menu_position()
    print(f"[3] Initial menu position: {initial_pos}")
    assert initial_pos is not None

    # Scroll down to footer
    floating.scroll_to_footer()
    print("[4] Scrolled to footer")

    # Menu still visible
    assert floating.is_menu_visible(), "Floating menu must remain visible after scrolling"
    print("[5] Floating menu is still visible after scrolling")

    # Capture menu position after scroll
    scrolled_pos = floating.get_menu_position()
    print(f"[6] Menu position after scrolling: {scrolled_pos}")
    assert scrolled_pos is not None

    # Check X position remains the same (fixed horizontally)
    tolerance = 5  # pixels
    diff_x = abs(initial_pos['x'] - scrolled_pos['x'])
    print(f"[7] X difference after scrolling: {diff_x}")
    assert diff_x <= tolerance, f"Floating menu moved horizontally: {diff_x}"

    print("[8] Floating menu remained visible and fixed horizontally ✅")

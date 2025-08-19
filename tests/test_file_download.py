from playwright.sync_api import Page, expect
import time
import random
from pathlib import Path


def test_exit_intent(page: Page, tmp_path) -> None:
    page.goto("https://the-internet.herokuapp.com/download")
    
    # Get all file links
    links = page.locator("div.example a")
    count = links.count()
    print(f"\nFound {count} download links:")

    # Print all links
    for i in range(count):
        link = links.nth(i)
        link_text = (link.text_content() or "").strip()
        link_href = link.get_attribute("href")
        print(f"[{i+1}] {link_text} -> {link_href}")

    # Pick a random number from 1 to 27 (or adjust to count if fewer files exist)
    random_index = random.randint(1, min(27, count))
    chosen_link = links.nth(random_index - 1)  # nth is zero-based

    chosen_text = (chosen_link.text_content() or "").strip()
    print(f"\n🎲 Randomly chosen file: [{random_index}] {chosen_text}")

    # Start download
    with page.expect_download() as download_info:
        chosen_link.click()
        
    download = download_info.value
    DOWNLOAD_DIR = Path(__file__).parent / "downloads"
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    # Save file
    save_path = DOWNLOAD_DIR / "E:\\herokuapp_project\\herokuapp_project_practice\\download"
    download.save_as(str(save_path))

    # Assert file exists
    assert save_path.exists(), f"Downloaded file {save_path.name} should exist"
    print(f"✅ Downloaded file saved at: {save_path}")

    # Cleanup
    save_path.unlink()
    
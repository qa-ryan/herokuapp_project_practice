import pytest
from playwright.sync_api import sync_playwright 

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()
        
@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
    
@pytest.fixture
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        yield browser
        await browser.close()

@pytest.fixture
async def context(browser):
    context = await browser.new_context()
    yield context
    await context.close()

@pytest.fixture
async def page(context):
    page = await context.new_page()
    yield page
    await page.close()
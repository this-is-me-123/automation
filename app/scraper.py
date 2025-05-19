from fastapi.responses import JSONResponse
from playwright.async_api import async_playwright

def return_mock_login(username: str):
    return {
        "message": f"Test received for {username}",
        "status": "success",
        "note": "This is a mock response. No real login performed."
    }

async def run_real_login(username: str, password: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://onlyfans.com/")
        await page.fill('input[name="email"]', username)
        await page.fill('input[name="password"]', password)
        await page.click('button[type="submit"]')
        await page.wait_for_load_state("networkidle")
        content = await page.content()
        await browser.close()
        return {
            "status": "success",
            "content_snippet": content[:500]
        }

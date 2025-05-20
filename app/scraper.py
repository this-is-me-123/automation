import base64
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
        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/113.0.0.0 Safari/537.36"
            )
        )
        page = await context.new_page()

        try:
            await page.goto("https://onlyfans.com/", timeout=60000)

            # Take screenshot before interaction to debug login page visibility
            initial_screenshot = await page.screenshot(full_page=True)
            initial_screenshot_b64 = base64.b64encode(initial_screenshot).decode("utf-8")

            # Check if login input is available
            await page.wait_for_selector('input[name="email"]', timeout=15000)
            await page.fill('input[name="email"]', username)
            await page.fill('input[name="password"]', password)
            await page.click('button[type="submit"]')

            # Wait for page load and allow JavaScript to settle
            await page.wait_for_load_state("networkidle", timeout=20000)
            await page.wait_for_timeout(2000)

            # Capture final state
            content = await page.content()
            title = await page.title()
            current_url = page.url

            final_screenshot = await page.screenshot(full_page=True)
            final_screenshot_b64 = base64.b64encode(final_screenshot).decode("utf-8")

            await browser.close()

            return {
                "status": "success",
                "title": title,
                "url": current_url,
                "content_snippet": content[:500],
                "screenshot_initial": initial_screenshot_b64,
                "screenshot_final": final_screenshot_b64
            }

        except Exception as e:
            await browser.close()
            raise Exception(f"Playwright error: {str(e)}")

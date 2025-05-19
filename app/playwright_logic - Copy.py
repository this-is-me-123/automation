from playwright.sync_api import sync_playwright

def login_and_scrape(username: str, password: str) -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://onlyfans.com/")

        page.fill("input[name='email']", username)
        page.fill("input[name='password']", password)
        page.click("button[type='submit']")

        page.wait_for_timeout(5000)  # Wait for login to process (customize this!)

        # Example check for successful login
        if "home" in page.url:
            result = {"status": "success", "url": page.url}
        else:
            result = {"status": "error", "message": "Login failed"}

        browser.close()
        return result

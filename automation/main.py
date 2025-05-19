from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from playwright.async_api import async_playwright
import asyncio

app = FastAPI()

API_KEY = "super-secret-key"  # Replace with your real secret

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login-scrape")
async def login_scrape(
    data: LoginRequest,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto("https://onlyfans.com/login")

            # Fill the login form fields
            await page.fill('input[name="login_email"]', data.username)
            await page.fill('input[name="login_password"]', data.password)

            # Wait for the login button to be visible and enabled
            login_button = page.locator('button:has-text("Log In")')
            await login_button.wait_for(state="visible")
            await page.wait_for_function(
                '() => !document.querySelector("button:has-text(\'Log In\')").disabled'
            )

            # Click the login button
            await login_button.click()

            # Optionally wait for navigation or some indication of login success/failure
            await page.wait_for_load_state("networkidle")

            # You can check here if login succeeded by looking for some element only visible after login
            # For demo, just returning success
            await browser.close()

        return {"status": "success", "detail": "Login attempted"}

    except Exception as e:
        return {"status": "error", "detail": str(e)}

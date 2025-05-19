# playwright_logic.py

import logging

def login_and_scrape(username: str, password: str) -> dict:
    """
    Simulated login and scraping function using dummy data.
    Replace this with real Playwright logic in production.
    """
    logging.info(f"Mock login attempt for: {username}")

    # Simulated validation
    if username == "test@example.com" and password == "test123":
        return {
            "message": f"Test received for {username}",
            "status": "success",
            "note": "This is a mock response. No real login performed."
        }
    else:
        return {
            "message": "Unauthorized",
            "status": "error"
        }

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define expected input format
class Credentials(BaseModel):
    username: str
    password: str

# Test route — doesn't actually log in
@app.post("/login-scrape")
def login_scrape(credentials: Credentials):
    print(f"Received username: {credentials.username}")
    return {
        "message": f"Test received for {credentials.username}",
        "status": "success",
        "note": "This is a mock response. No real login performed."
    }

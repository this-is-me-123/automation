from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.config import settings
from app.scraper import run_real_login, return_mock_login

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login-scrape")
async def login_scrape(data: LoginRequest):
    if settings.mock_login:
        return return_mock_login(data.username)
    try:
        return await run_real_login(data.username, data.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Login failed: {str(e)}")

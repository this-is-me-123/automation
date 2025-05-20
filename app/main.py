from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel
from app.config import settings
from app.scraper import run_real_login, return_mock_login
import base64

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login-scrape")
async def login_scrape(data: LoginRequest, image: bool = Query(False)):
    if settings.mock_login:
        return return_mock_login(data.username)

    try:
        result = await run_real_login(data.username, data.password)

        if image:
            screenshot_bytes = base64.b64decode(result["screenshot_base64"])
            return Response(content=screenshot_bytes, media_type="image/png")

        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Login failed: {str(e)}")

from fastapi import FastAPI
from app.config import settings

app = FastAPI(debug=settings.debug)

@app.get("/")
def read_root():
    return {"env": settings.env, "debug": settings.debug}

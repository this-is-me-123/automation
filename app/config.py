from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    env: str = "development"
    debug: bool = True
    mock_login: bool = False  # ✅ This must match your .env var

    class Config:
        env_file = f".env.{os.getenv('ENV', 'dev')}"

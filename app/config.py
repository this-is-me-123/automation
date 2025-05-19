from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    env: str = "development"
    debug: bool = True

    class Config:
        env_file = f".env.{os.getenv('ENV', 'dev')}"

settings = Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    env: str = "development"
    debug: bool = True
    mock_login: bool = False

    model_config = SettingsConfigDict(
        env_file=f".env.{os.getenv('ENV', 'development')}",
        extra="forbid"  # Only allow fields defined above
    )

settings = Settings()

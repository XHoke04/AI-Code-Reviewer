from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Server config
    port: int = 8000
    environment: str = "development"

    # Github config (will add later)
    github_api_id: str = ""
    github_private_key: str = ""
    github_webhook_secret: str = ""

    # OpenAI config (will add later)
    openai_api_key: str = ""

    # Database config (will add later)
    database_url: str = ""

    class Config:
        env_file = ".env"
        case_sensitive = False

@lru_cache()
def get_settings() -> Settings:
    """Create cached settings instance."""
    return Settings()
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from constants import MODEL_REVISION
import os


class Settings(BaseSettings):
    model_revision: str = Field(default=MODEL_REVISION)

    model_config = SettingsConfigDict(
        env_file=".env" if os.getenv("ENV", "development") == "development" else None,
        env_file_encoding="utf-8",
        extra="ignore",
        validate_default=True,
    )


settings = Settings()

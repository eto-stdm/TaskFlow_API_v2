from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str

    class Config:
        env_file = "app/.env"
        env_file_encoding = "utf-8"

settings = Settings()
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Wordle"

    class Config:
        env_file = ".env"

settings = Settings()

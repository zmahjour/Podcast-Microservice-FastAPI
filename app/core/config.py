from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # MongoDB
    MONGODB_HOST: str
    MONGODB_PORT: int

    RSS_APP_BASE_URL: str

    class Config:
        env_file = (
            "/home/samane/Documents/MaktabSharif/FinalProject/Project/Podcast/.env"
        )


settings = Settings()

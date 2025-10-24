from pydantic import BaseModel
import os

class Settings(BaseModel):
    db_url: str = os.getenv("DB_URL", "postgresql+psycopg2://flipzen@db:5432/flipzen_db")
    cors_origins: str = os.getenv("CORS_ORIGINS", "http://localhost:5173")

settings = Settings()
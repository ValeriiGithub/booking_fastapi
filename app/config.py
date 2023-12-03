from pydantic_settings import BaseSettings
from pydantic import model_validator, validator


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @model_validator(mode='before')
    def get_database_url(cls, v):
        v["DATABASE_URL"] = f"postgresql+asyncpg://{v['DB_USER']}:{v['DB_PASS']}@{v['DB_HOST']}:{v['DB_PORT']}/{v['DB_NAME']}"
        return v
    class Config:
        env_file = "../.env"


settings = Settings()

print(settings.DATABASE_URL)



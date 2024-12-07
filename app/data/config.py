import os


class Settings:

    @property
    def DATABASE_URL(self) -> str:
        db_url = os.getenv("DATABASE_URL", "postgresql://postgres:1234@localhost:5432/db_kurs")
        if not db_url:
            raise ValueError("DATABASE_URL is not set in environment variables.")
        return db_url


settings = Settings()

print(settings.DATABASE_URL)

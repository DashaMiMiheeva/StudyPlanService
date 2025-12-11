import os

class Settings:
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://study_user:study_password@localhost:5432/study_plan_db"
    )

settings = Settings()
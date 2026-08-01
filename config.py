from dotenv import load_dotenv
import os

load_dotenv()


class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "aspire_ai_hackathon_secret_key"
    )

    MYSQL_HOST = os.getenv(
        "MYSQL_HOST",
        "localhost"
    )

    MYSQL_USER = os.getenv(
        "MYSQL_USER",
        "root"
    )

    MYSQL_PASSWORD = os.getenv(
        "MYSQL_PASSWORD",
        ""
    )

    MYSQL_DB = os.getenv(
        "MYSQL_DB",
        "aspire_ai"
    )

    GEMINI_API_KEY = os.getenv(
        "GEMINI_API_KEY"
    )
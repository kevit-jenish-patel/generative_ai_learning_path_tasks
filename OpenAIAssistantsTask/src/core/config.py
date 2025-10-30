from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    MONGODB_URI: str = ""
    LANGFUSE_SECRET_KEY: str = ""
    LANGFUSE_PUBLIC_KEY: str = ""
    LANGFUSE_BASE_URL: str = ""
    WEBSITE_URL_TO_SCRAP: str = ""
    OPENAI_API_KEY: str = ""
    OPENAI_ASSISTANT_ID: str = ""

    class Config:
        env_file = ".env"

settings = Settings()

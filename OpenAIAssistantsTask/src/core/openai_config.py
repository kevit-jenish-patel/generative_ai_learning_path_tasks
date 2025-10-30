from langfuse.openai import OpenAI
from langfuse import observe

from src.core.config import settings

@observe()
def connect_to_openai():
    return OpenAI(api_key=settings.OPENAI_API_KEY)

client = connect_to_openai()
from groq import Groq
import litellm
from langfuse import Langfuse

from apps.core.config import LANGFUSE_SECRET_KEY, LANGFUSE_PUBLIC_KEY, LANGFUSE_HOST
from apps.core.config import GROK_API_KEY

# client = Groq(
#     api_key=GROK_API_KEY,
# )

langfuse = Langfuse(
  secret_key=LANGFUSE_SECRET_KEY,
  public_key=LANGFUSE_PUBLIC_KEY,
  host=LANGFUSE_HOST
)

def generate_llm_response(prompt):
    # chat_completion = client.chat.completions.create(
    #     messages=prompt,
    #     model="llama-3.3-70b-versatile",
    #     temperature=0.3,
    #     max_completion_tokens=8192,
    #     stop=None
    # )
    # return chat_completion.choices[0].message.content

    # Enable Langfuse OTEL integration
    litellm.callbacks = ["langfuse_otel"]

    response = litellm.completion(
        model="groq/llama-3.3-70b-versatile",
        messages=prompt,
        temperature=0.3,
        stop=None,
        api_key=GROK_API_KEY,
    )
    return response.choices[0].message.content
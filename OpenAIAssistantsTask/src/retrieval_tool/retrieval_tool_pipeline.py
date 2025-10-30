from src.core.config import settings
from src.retrieval_tool.threads import create_thread, create_message, list_messages, run_thread


# GPT-4.1 nano
# GPT-4o mini

def retrieval_tool_pipeline():

    user_query = input("Please enter a query: ")

    thread = create_thread()

    assistant_message = create_message(thread.id, "assistant", "How can I help you?")

    user_message = create_message(thread.id,"user",user_query)

    messages = list_messages(thread.id)
    for message in messages:
        print(message.content[0].text.value)

    run = run_thread(thread_id=thread.id,assistant_id=settings.OPENAI_ASSISTANT_ID)

    messages = list_messages(thread.id)
    for message in messages:
        print(message.content[0].text.value)
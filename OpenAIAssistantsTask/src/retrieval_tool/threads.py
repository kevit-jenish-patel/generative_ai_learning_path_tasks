from langfuse import observe

from src.core.openai_config import client

@observe()
def create_thread():
    thread = client.beta.threads.create()
    return thread

@observe()
def create_message(thread_id,role,content):
    message = client.beta.threads.messages.create(thread_id=thread_id,role=role,content=content)
    return message

@observe()
def list_messages(thread_id):
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    return messages.data

@observe()
def run_thread(thread_id,assistant_id):
    run = client.beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant_id)
    return run
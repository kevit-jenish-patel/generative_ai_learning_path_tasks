import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st

from src.core.config import settings
from src.core.openai_config import client
from src.retrieval_tool.threads import create_thread, create_message, list_messages, run_thread


thread = create_thread()
st.session_state["thread_id"]=thread.id

def add_session_state(message):
    if "messages" in st.session_state:
        st.session_state["messages"].append({
            "role": message.role,
            "content": message.content[0].text.value
        })
    else:
        st.session_state["messages"]=[{
            "role": message.role,
            "content": message.content[0].text.value
        }]

def display_message(message):
    add_session_state(message)
    with st.chat_message(message.role):
        st.markdown(message.content[0].text.value)


# --- SIDEBAR ---
with st.sidebar:
    openai_api_key = st.text_input("🔑 OpenAI API Key", key="chatbot_api_key", type="password")
    st.markdown("[Get an API key](https://platform.openai.com/account/api-keys)")
    st.markdown("[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)")

# --- PAGE SETUP ---
st.title("💬 Assistant API Chatbot")
st.caption("🚀 Powered by the OpenAI Assistants API and Streamlit")

# --- INITIALIZE SESSION STATE ---
if "messages" not in st.session_state:
    assistant_message = create_message(st.session_state["thread_id"], "assistant", "How can I help you?")
    add_session_state(assistant_message)

# --- DISPLAY CHAT HISTORY ---
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- CHAT INPUT ---
if prompt := st.chat_input("Type your message..."):
    # --- ADD USER MESSAGE ---
    user_message = create_message(st.session_state["thread_id"], "user", prompt)
    display_message(user_message)

    # # --- RUN THE ASSISTANT ---
    # with st.spinner("Assistant is thinking..."):
    #     run = run_thread(thread_id=st.session_state.thread_id, assistant_id=settings.OPENAI_ASSISTANT_ID)
    #
    # # --- GET UPDATED MESSAGES ---
    # messages = list_messages(st.session_state.thread_id)
    # assistant_reply = messages[0]
    #
    # # --- DISPLAY ASSISTANT RESPONSE ---
    # display_message(assistant_reply)

    # Stream the assistant’s response
    with st.chat_message("assistant"):
        response_box = st.empty()
        streamed_text = ""

        with client.beta.threads.runs.stream(
                thread_id=st.session_state["thread_id"],
                assistant_id=settings.OPENAI_ASSISTANT_ID,
        ) as stream:
            for event in stream:
                if event.event == "thread.message.delta":
                    delta = event.data.delta
                    token = delta.content[0].text.value
                    streamed_text += token
                    response_box.markdown(streamed_text + "▌")
                elif event.event == "thread.run.completed":
                    # Optional: handle completion
                    break

            response_box.markdown(streamed_text)

        st.session_state.messages.append({"role": "assistant", "content": streamed_text})

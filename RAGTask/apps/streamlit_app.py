import streamlit as st
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from apps.ingestion.ingestion_pipeline import run_ingestion_pipeline
from apps.utils.rag_pipeline import run_rag_pipeline

run_ingestion_pipeline()

st.title("Hey! I am your assistant")

st.caption("Feel free to ask any queries, questions or inquiries.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Enter your message here"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        try:
            with st.spinner("Thinking..."):
                assistant_response = run_rag_pipeline(prompt)
            for chunk in assistant_response.split("\n"):
                full_response += chunk + "\n"
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
        except Exception as e:
            full_response = "Sorry, something went wrong while processing your request."
            st.error(f"Error: {e}")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Optional: Clear chat button
if st.button("Clear chat"):
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]
    st.rerun()
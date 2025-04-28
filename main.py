import streamlit as st
from typing import Optional

from src.chatbotmanager import ChatbotManager
from setup import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_MODEL,
    AZURE_OPENAI_API_ENDPOINT,
    TIKTOKEN_MODEL,
    MAX_TOKENS,
    TEMPERATURE,
)


def main():
    chat: ChatbotManager = ChatbotManager(
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
        model=AZURE_OPENAI_MODEL,
        endpoint=AZURE_OPENAI_API_ENDPOINT,
        tiktoken_model=TIKTOKEN_MODEL,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
    )

    # Streamlit App
    st.title("Chatbot App")  # Add a title

    # User input
    with st.form("user_form", clear_on_submit=False):
        user_input: str = st.text_input("Type something")
        submit_button: bool = st.form_submit_button(label="Send")

    if submit_button:
        with st.spinner("Wait for it..."):
            response: Optional[str] = chat.get_response(user_input)
            prompt_tokens_amount: int = chat.get_tokens(user_input)
            response_tokens_amount: int = chat.get_tokens(response)
            st.write(f'Prompt tokens: {prompt_tokens_amount}')
            st.write(f'Assistant: {response}')
            st.write(f'Response tokens: {response_tokens_amount}')


if __name__ == '__main__':
    main()

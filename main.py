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

    user_prompt: str = ''
    while not user_prompt == 'exit':
        user_prompt: str = str(input('Prompt: '))
        response: str = chat.get_response(prompt=user_prompt)
        tokens_amount: int = chat.get_tokens(input=user_prompt)

        print(f'Tokens amount: {tokens_amount}')
        print(f'Assistant: {response}')
        print('-'*50, '\n')


if __name__ == '__main__':
    main()

from typing import Optional
from tiktoken import get_encoding
from tiktoken.core import Encoding
from openai import AzureOpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessage

from setup import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_MODEL,
    AZURE_OPENAI_API_ENDPOINT,
    TIKTOKEN_MODEL,
    MAX_TOKENS,
    TEMPERATURE,
    SYSTEM_MESSAGE,
)

class ChatbotManager:
    def __init__(self) -> None:
        self.client: AzureOpenAI = AzureOpenAI(
            azure_endpoint=AZURE_OPENAI_API_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            api_version=AZURE_OPENAI_API_VERSION,
        )
        self.encoding: Encoding = get_encoding(TIKTOKEN_MODEL)
        self.messages: list[dict[str, str]] = [
            {'role': 'system', 'content': SYSTEM_MESSAGE}
        ]

    def get_response(self, prompt: str) -> Optional[str]:
        self.messages.append({'role': 'user', 'content': prompt})
        completion: ChatCompletion = self.client.chat.completions.create(
            model=AZURE_OPENAI_MODEL,
            messages=self.messages,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
        )
        message: ChatCompletionMessage = completion.choices[0].message
        self.messages.append({'role': message.role, 'content': message.content})

        response: Optional[str] = message.content
        return response

    def get_tokens(self, input: str) -> int:
        tokens_integers: list[int] = self.encoding.encode(input)
        tokens_amount: int = len(tokens_integers)
        return tokens_amount

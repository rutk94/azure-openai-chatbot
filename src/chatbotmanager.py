from tiktoken import get_encoding
from tiktoken.core import Encoding
from openai import AzureOpenAI, Completion


class ChatbotManager:
    def __init__(
        self,
        api_key: str,
        api_version: str,
        model: str,
        endpoint: str,
        tiktoken_model: str,
        max_tokens: int = 4096,
        temperature: float = 0.1
    ) -> None:
        self._api_key: str = api_key
        self.api_version: str = api_version
        self.model: str = model
        self.endpoint: str = endpoint
        self.tiktoken_model: str = tiktoken_model
        self.max_tokens: int = max_tokens
        self.temperature: float = temperature

        self.client: AzureOpenAI = AzureOpenAI(
            azure_endpoint=self.endpoint,
            api_key=self._api_key,
            api_version=self.api_version
        )
        self.encoding: Encoding = get_encoding(self.tiktoken_model)

    def get_response(self, prompt: str) -> str:
        completion: Completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': prompt}
            ],
            max_tokens=self.max_tokens,
            temperature=self.temperature
        )
        response: str = completion.choices[0].message.content
        return response

    def get_tokens(self, input: str) -> int:
        tokens_integers: list[int] = self.encoding.encode(input)
        tokens_amount: int = len(tokens_integers)
        return tokens_amount

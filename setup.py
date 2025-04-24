import os
from dotenv import load_dotenv


load_dotenv(override=True)

AZURE_OPENAI_API_KEY: str = os.getenv('AZURE_OPENAI_API_KEY')
AZURE_OPENAI_API_ENDPOINT: str = os.getenv('AZURE_OPENAI_API_ENDPOINT')
AZURE_OPENAI_API_VERSION: str = os.getenv('AZURE_OPENAI_API_VERSION')
AZURE_OPENAI_MODEL: str = os.getenv('AZURE_OPENAI_MODEL')
TIKTOKEN_MODEL: str = os.getenv('TIKTOKEN_MODEL')
MAX_TOKENS: int = int(os.getenv('MAX_TOKENS'))
TEMPERATURE: float = float(os.getenv('TEMPERATURE'))

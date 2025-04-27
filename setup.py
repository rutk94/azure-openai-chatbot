import os
from dotenv import load_dotenv
from typing import Optional

from utils.setup_validator import get_var_type_or_die


load_dotenv(override=True)

AZURE_OPENAI_API_KEY: str = get_var_type_or_die('AZURE_OPENAI_API_KEY', str)
AZURE_OPENAI_API_ENDPOINT: str = get_var_type_or_die('AZURE_OPENAI_API_ENDPOINT', str)
AZURE_OPENAI_API_VERSION: str = get_var_type_or_die('AZURE_OPENAI_API_VERSION', str)
AZURE_OPENAI_MODEL: str = get_var_type_or_die('AZURE_OPENAI_MODEL', str)
TIKTOKEN_MODEL: str = get_var_type_or_die('TIKTOKEN_MODEL', str)

MAX_TOKENS: Optional[int] = int(str(os.getenv('MAX_TOKENS'))) if os.getenv('MAX_TOKENS') else None
TEMPERATURE: Optional[float] = float(str(os.getenv('TEMPERATURE'))) if os.getenv('TEMPERATURE') else None

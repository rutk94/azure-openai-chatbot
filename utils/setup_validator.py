import os
from typing import Optional, Any
from dotenv import load_dotenv


load_dotenv(override=True)


def get_var_type_or_die(var_name: str, var_type: type, default: Optional[Any] = None) -> Any:

    if default:
        if var_type != bool and not isinstance(default, var_type):
            raise ValueError(
                f"Wrong default value type for variable '{var_name}'. "
                f"{default=} must be '{var_type}' if it's not None"
            )
        elif var_type == bool and default.lower() not in ('true', 't', '1', 'false', 'f', '0'):
            raise ValueError(
                f"Wrong default value type for variable '{var_name}'. "
                f"{default=} must be '{var_type}' if it's not None"
            )

    try:
        value: Any
        if var_type == bool:
            value = str(os.getenv(var_name, default=default)).lower() in ('true', 't', '1')
        else:
            value = var_type(os.getenv(var_name, default=default))
    except ValueError:
        raise ValueError(f'Wrong value {var_name=} or {default=}. It must be a {var_type}.')
    else:
        return value

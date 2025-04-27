from pytest import mark, raises
from unittest.mock import MagicMock
from typing import Optional, Any

from utils.setup_validator import get_var_type_or_die


def mock_getenv(monkeypatch, value: Optional[str], default: Optional[Any]) -> MagicMock:
    mock_getenv: MagicMock
    if value:
        mock_getenv = MagicMock(return_value=value)
    elif default:
        mock_getenv = MagicMock(return_value=default)
    else:
        raise ValueError(
            "At least one of arguments 'value' or 'default' mustn't be 'None'!"
        )
    monkeypatch.setattr('os.getenv', mock_getenv)
    return mock_getenv


@mark.parametrize(
    'var_value, var_type, default, expected_value',
    [
        ('abc', str, None, 'abc'),
        ('1', int, None, 1),
        ('1.0', float, None, 1.0),
        ('true', bool, None, True),
        (None, str, 'abc1', 'abc1'),
        (None, int, 2, 2),
        (None, float, 2.0, 2.0),
        (None, bool, 'False', False),
    ],
)
def test_get_var_type_or_die(
    monkeypatch,
    var_value: Optional[str],
    var_type: type,
    default: Optional[Any],
    expected_value: Any,
) -> None:
    mock_getenv(monkeypatch, value=var_value, default=default)
    value: Any = get_var_type_or_die(
        var_name='any_name', var_type=var_type, default=default
    )
    assert isinstance(value, var_type)
    assert value == expected_value


@mark.parametrize(
    'var_value, var_type, default',
    [('abc', str, 1), ('true', bool, 'abc'), ('abc', int, None)],
)
def test_get_var_type_or_die_raises_error(
    monkeypatch, var_value: Optional[str], var_type: type, default: Optional[Any]
) -> None:
    mock_getenv(monkeypatch, value=var_value, default=default)
    with raises(ValueError):
        _ = get_var_type_or_die(var_name='any_name', var_type=var_type, default=default)

import pytest

from src.widget import get_date


@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        ("2023-12-31", "31.12.2023"),
        ("1999-01-01", "01.01.1999"),
        ("2000-02-29", "29.02.2000"),  # високосный год
        ("2021-10-05", "05.10.2021"),
        ("2024-04-15", "15.04.2024"),
    ]
)
def test_get_date(input_date: str, expected_output: str) -> None:
    assert get_date(input_date) == expected_output

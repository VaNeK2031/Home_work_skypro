import pytest

from src.widget import mask_account_card


def test_mask_valid_card(valid_card_data: dict) -> None:
    """Тестирует маскировку номеров карт."""
    for input_data, expected_output in valid_card_data.items():
        assert mask_account_card(input_data) == expected_output


def test_mask_valid_account(valid_account_data: dict) -> None:
    """Тестирует маскировку номеров счетов."""
    for input_data, expected_output in valid_account_data.items():
        assert mask_account_card(input_data) == expected_output


def test_invalid_input_format(invalid_input_data: dict) -> None:
    """Проверяет, что при некорректном формате входных данных выбрасывается ValueError."""
    for data in invalid_input_data:
        with pytest.raises(ValueError):
            mask_account_card(data)


def test_invalid_card_number_length(invalid_card_number_data: dict) -> None:
    """Проверяет, что при неверной длине номера карты выбрасывается ValueError."""
    for data in invalid_card_number_data:
        with pytest.raises(ValueError):
            mask_account_card(data)


def test_invalid_account_number(invalid_account_number_data: dict) -> None:
    """Проверяет, что при неверном номере счёта выбрасывается ValueError."""
    for data in invalid_account_number_data:
        with pytest.raises(ValueError):
            mask_account_card(data)

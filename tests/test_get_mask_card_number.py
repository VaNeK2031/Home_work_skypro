import pytest

from src.masks import get_mask_card_number


# Тест на основной корректный номер (через фикстуру)
def test_main_valid_card(valid_card: str) -> None:
    expected = "1234 56** **** 3456"
    assert get_mask_card_number(valid_card) == expected


# Тест на другие корректные номера (с параметризацией и фикстурой)
def test_other_valid_cards(other_valid_cards: list) -> None:
    for card, expected in other_valid_cards:
        assert get_mask_card_number(card) == expected


# Тесты на некорректные входные данные
def test_invalid_card_numbers(invalid_card_inputs: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card_inputs)

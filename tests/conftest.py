from typing import Any, Dict

import pytest
from pytest import FixtureRequest

# фикстура с корректным номером карты


@pytest.fixture
def valid_card() -> str:
    """Возвращает корректный номер карты."""
    return "1234567890123456"

# фикстура с параметризацией для различных корректных номеров карт


@pytest.fixture
def other_valid_cards() -> list:
    """Возвращает список других корректных номеров карт и ожидаемых результатов."""
    return [
        ("0000000000000001", "0000 00** **** 0001"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("7777666655554444", "7777 66** **** 4444"),
    ]

# фикстура с некорректными номерами карты


@pytest.fixture
def invalid_card_inputs() -> list:
    return [
        "123",                   # слишком короткий
        "12345678901234567",     # слишком длинный
        "1234-5678-9012-3456",   # содержит символы
        "abcdabcdabcdabcd",      # только буквы
        "12a456b890c23d56",      # смешанные буквы и цифры
        "",                      # пустая строка
        " ",                     # пробел
    ]

# Фикстура, возвращающая корректный номер счета


@pytest.fixture
def valid_account_number() -> str:
    return "1234567890"


# Фикстура, возвращающая короткий номер счета


@pytest.fixture
def short_account_number() -> str:
    return "123"


# Фикстура, возвращающая некорректный (с буквами) номер счета


@pytest.fixture
def invalid_account_number() -> str:
    return "12a4"


# Корректные входные данные


@pytest.fixture
def valid_card_data() -> dict:
    """Корректные данные для карт."""
    return {
        "Visa Platinum 7000792289606361": "Visa Platinum 7000 79** **** 6361",
        "MasterCard 5486470000000093": "Mastercard 5486 47** **** 0093",
        "Maestro 6368550978813332": "Maestro 6368 55** **** 3332",
        "МИР 2200668499890012": "Мир 2200 66** **** 0012",
    }


@pytest.fixture
def valid_account_data() -> dict:
    """Корректные данные для счетов."""
    return {
        "Счет 73654108430135874305": "Счет **4305",
        "Счет 12345678901234567890": "Счет **7890",
        "Счет 00000000000000000000": "Счет **0000",
    }


@pytest.fixture
def invalid_input_data() -> list:
    """Некорректные входные данные (без номера или неверный формат)."""
    return [
        "Visa Platinum",                   # Нет номера карты
        "Счет",                            # Нет номера счёта
        "1234567890123456",                # Только номер без типа
        "Visa Platinum ABCDABCDABCDABCD",  # Буквы в номере
        "Счет ABCD1234",                   # Буквы в номере счёта
        "MasterCard 123",                  # Слишком короткий номер
    ]


@pytest.fixture
def invalid_card_number_data() -> list[str]:
    """Некорректные номера карт (неверная длина)."""
    return [
        "Visa Platinum 1234",               # Слишком короткий номер
        "Visa Platinum 123456789012345",    # 15 цифр — должно быть 16
        "Visa Platinum 12345678901234567",  # 17 цифр
    ]


@pytest.fixture
def invalid_account_number_data() -> list:
    """Некорректные номера счетов (слишком короткие)."""
    return [
        "Счет 123",       # Слишком короткий номер
        "Счет ABCD1234",  # Буквы в номере
    ]


@pytest.fixture(params=[
    ("EXECUTED", [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}]),
    ("CANCELED", [{"id": 2, "state": "CANCELED"}, {"id": 5, "state": "CANCELED"}]),
    ("PENDING", [{"id": 4, "state": "PENDING"}]),
    ("NOT_EXIST", []),
])
def filter_params(request: FixtureRequest) -> Dict[str, Any]:
    state, expected = request.param
    return {"state": state, "expected": expected}


@pytest.fixture
def sample_data_ver2() -> list:
    """Базовый набор данных с разными датами."""
    return [
        {'name': 'event1', 'date': '2023-01-01T12:00:00'},
        {'name': 'event2', 'date': '2022-12-31T23:59:59'},
        {'name': 'event3', 'date': '2023-01-02T00:00:00'},
    ]


@pytest.fixture
def expected_sorted_asc() -> list:
    """Ожидаемый результат при сортировке по возрастанию."""
    return [
        {'name': 'event2', 'date': '2022-12-31T23:59:59'},
        {'name': 'event1', 'date': '2023-01-01T12:00:00'},
        {'name': 'event3', 'date': '2023-01-02T00:00:00'},
    ]


@pytest.fixture
def expected_sorted_desc() -> list:
    """Ожидаемый результат при сортировке по убыванию."""
    return [
        {'name': 'event3', 'date': '2023-01-02T00:00:00'},
        {'name': 'event1', 'date': '2023-01-01T12:00:00'},
        {'name': 'event2', 'date': '2022-12-31T23:59:59'},
    ]

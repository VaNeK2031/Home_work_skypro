from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state

# Тест 1: Проверяем фильтрацию по умолчанию (state='EXECUTED')


def test_filter_by_state_default() -> None:
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
    ]
    expected = [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}]
    result = filter_by_state(data)
    assert result == expected


# Тест 2: Проверяем фильтрацию с указанным state='CANCELED'


def test_filter_by_state_canceled() -> None:
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "CANCELED"},
    ]
    expected = [{"id": 2, "state": "CANCELED"}, {"id": 4, "state": "CANCELED"}]
    result = filter_by_state(data, "CANCELED")
    assert result == expected


# Тест 3: Проверяем работу с пустым списком


def test_filter_by_state_empty_data() -> None:
    data: List[Dict[str, Any]] = []
    expected: List[Dict[str, Any]] = []
    result = filter_by_state(data, "EXECUTED")
    assert result == expected


# Тест 4: Проверяем случай, когда совпадений нет


def test_filter_by_state_no_match() -> None:
    data = [
        {"id": 1, "state": "CANCELED"},
        {"id": 2, "state": "PENDING"},
    ]
    expected: List[Dict[str, Any]] = []
    result = filter_by_state(data, "EXECUTED")
    assert result == expected


# Тест 5: Проверяем случай, когда ключ 'state' отсутствует


def test_filter_by_state_missing_key() -> None:
    data: List[Dict[str, Any]] = [
        {"id": 1},
        {"id": 2, "state": "EXECUTED"},
        {"id": 3},  # нет ключа 'state'
    ]
    expected = [{"id": 2, "state": "EXECUTED"}]
    result = filter_by_state(data, "EXECUTED")
    assert result == expected


# Параметризованный тест — проверяем несколько состояний сразу


@pytest.mark.parametrize(
    "data, state, expected",
    [
        (
            [
                {"id": 1, "state": "EXECUTED"},
                {"id": 2, "state": "CANCELED"},
                {"id": 3, "state": "EXECUTED"},
            ],
            "EXECUTED",
            [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}],
        ),
        (
            [
                {"id": 1, "state": "EXECUTED"},
                {"id": 2, "state": "CANCELED"},
                {"id": 3, "state": "PENDING"},
            ],
            "CANCELED",
            [{"id": 2, "state": "CANCELED"}],
        ),
        (
            [],
            "EXECUTED",
            [],
        ),
        (
            [
                {"id": 1},
                {"id": 2, "state": "PENDING"},
                {"id": 3, "state": "EXECUTED"},
            ],
            "EXECUTED",
            [{"id": 3, "state": "EXECUTED"}],
        ),
    ],
)
def test_filter_by_state_parametrized(
    data: List[Dict[str, Any]],
    state: str,
    expected: List[Dict[str, Any]]
) -> None:
    assert filter_by_state(data, state) == expected

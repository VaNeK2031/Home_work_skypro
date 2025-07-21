import pytest

from src.processing import sort_by_date


# Тест: пустой список должен возвращать пустой список
def test_sort_by_date_empty_list() -> None:
    assert sort_by_date([]) == []


# Тест: список из одного элемента остаётся неизменным
def test_sort_by_date_single_item() -> None:
    data = [{'name': 'event', 'date': '2023-01-01T00:00:00'}]
    assert sort_by_date(data, ascending=True) == data
    assert sort_by_date(data, ascending=False) == data


# Тест: поведение при отсутствии ключа 'date' (ожидается KeyError)
def test_sort_by_date_missing_key() -> None:
    data = [{'name': 'event1'}, {'name': 'event2', 'date': 'invalid'}]
    with pytest.raises(KeyError):
        sort_by_date(data)

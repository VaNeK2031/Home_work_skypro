import pytest
from src.masks import get_mask_account

# Параметризованный тест для проверки корректных входных данных
@pytest.mark.parametrize("account_number, expected", [
    ("1234", "**1234"),
    ("12345678", "**5678"),
    ("9876543210", "**3210"),
])
def test_get_mask_account_valid(account_number, expected):
    assert get_mask_account(account_number) == expected


# Тестирование с фикстурой, содержащей правильный номер
def test_get_mask_account_with_fixture(valid_account_number):
    assert get_mask_account(valid_account_number) == "**7890"


# Тестирование с коротким номером счета (меньше 4 символов)
def test_get_mask_account_short(short_account_number):
    with pytest.raises(ValueError):
        get_mask_account(short_account_number)


# Тестирование с некорректным номером (не только цифры)
def test_get_mask_account_invalid(invalid_account_number):
    with pytest.raises(ValueError):
        get_mask_account(invalid_account_number)


# Параметризованный тест на выброс исключений
@pytest.mark.parametrize("account_number", [
    "12",          # слишком короткий
    "abcd",        # не цифры
    "12ab",        # смесь букв и цифр
    "",            # пустая строка
])
def test_get_mask_account_invalid_cases(account_number):
    with pytest.raises(ValueError):
        get_mask_account(account_number)

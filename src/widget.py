from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Возвращает строку с замаскированным номером карты или счёта.

    Определяет тип финансового инструмента (карта или счёт) на основе входной строки,
    применяет соответствующую маску к номеру и возвращает обновлённую строку.

    Args:
        data (str): Строка, содержащая тип и номер карты или счёта.
                    Примеры:
                        - "Visa Platinum 7000792289606361"
                        - "Счет 73654108430135874305"

    Returns:
        str: Строка с замаскированным номером.
             Примеры:
                - "Visa Platinum 7000 79** **** 6361"
                - "Счет **4305"
    """
    # Полученные данные приведем к нижнему регистру и разобьем на список, содержащий отдельно имя(имена) отдельно номер
    parts = data.split()
    if len(parts) < 2:
        raise ValueError(f"Неверный формат данных: '{data}'. Ожидалось название и номер.")

    number = parts[-1]
    name = " ".join(parts[:-1])

    # Проверяем, что номер состоит только из цифр
    if not number.isdigit():
        raise ValueError(f"Номер должен состоять только цифры. Получено: '{number}'")

    # Определяем тип: карта или счёт
    if name.lower() == "счет":
        if len(number) < 4:
            raise ValueError(f"Номер счёта должен содержать минимум 4 цифры. Получено: {len(number)} символов.")
        return f"{name.title()} {get_mask_account(number)}"
    elif len(number) != 16:
        raise ValueError(f"Номер карты должен содержать 16 цифр. Получено: {len(number)} символов.")
    return f"{name.title()} {get_mask_card_number(number)}"


def get_date(date: str) -> str:
    """
        Преобразует строку с датой из формата 'YYYY-MM-DD' в формат 'DD.MM.YYYY'.

        Параметры:
            date (str): Дата в формате 'YYYY-MM-DD'.

        Возвращает:
            str: Дата в формате 'DD.MM.YYYY'.
        """
    # Зная формат входных данных делаем срезы по году, месяцу и дню
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]

    return f"{day}.{month}.{year}"

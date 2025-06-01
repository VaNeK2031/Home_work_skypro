from masks import get_mask_account, get_mask_card_number


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
    parts = data.lower().split()
    number = parts[-1]
    name = " ".join(parts[:-1])
    masked_data = ''
    # Проверяем получен счет или название карты, и производим маскировку данных
    if name == "счет":
        masked_data = name.title() + ' ' + get_mask_account(number)
    elif name != "счет":
        masked_data = name.title() + ' ' + get_mask_card_number(number)
    return masked_data


def get_date(date: str) -> str:
    # Зная формат входных данных делаем срезы по году, месяцу и дню
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]

    return f"{day}.{month}.{year}"

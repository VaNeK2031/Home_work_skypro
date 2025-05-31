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
    # Полученные данные приведем к нижнему регистру и разобъем на список, содержащий отдельно имя(имена) отдельно номер
    parts = data.split()
    number = parts[-1]
    name = ' '.join(parts[:-1])
    masked_card = ''
    masked_account = ''
    # Проверяем получен счет или название карты, и производим маскировку данных
    if name == 'счет':
        return f"{name.title()} {get_mask_account(number)}"
    elif name != 'счет':
        return f"{name.title()} {get_mask_card_number(number)}"


def get_date(date: str) -> str:
    pass


if __name__ == '__main__':
    user_input = input("Введите данные: ")
    print(mask_account_card(user_input))

def get_mask_card_number(card_number: str) -> str:
    # Убедимся, что номер карты имеет длину 16 символов
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать ровно 16 цифр")

    # Берем первые 6 и последние 4 цифры
    first_part = card_number[:6]
    last_part = card_number[-4:]

    # Формируем маску: XXXX XX** **** XXXX
    masked_number = f"{first_part[:4]} {first_part[4:]}" + "** **** " + last_part

    return masked_number


def get_mask_account(account_number: str) -> str:
    # Проверяем, что номер счета содержит хотя бы 4 цифры
    if not account_number.isdigit() or len(account_number) < 4:
        raise ValueError("Номер счета должен содержать не менее 4 цифр")

    # Берем только последние 4 цифры
    last_four_digits = account_number[-4:]

    # Формируем маску: **XXXX
    masked_account = f"**{last_four_digits}"

    return masked_account


if __name__ == '__main__':
    user_card = input("ВВедите номер карты: ")
    user_account = input("Введите номер счета: ")
    print(get_mask_card_number(user_card))
    print(get_mask_account(user_account))

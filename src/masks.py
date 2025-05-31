def get_mask_card_number(card_number: str) -> str:
    """
        Возвращает замаскированный номер карты в формате 'XXXX XX** **** XXXX'.

        Проверяет, что номер карты состоит ровно из 16 цифр. Если проверка не пройдена,
        выбрасывается исключение ValueError.

        Args:
            card_number (str): Номер карты (только цифры, длина — 16 символов).

        Returns:
            str: Замаскированный номер карты.

        Raises:
            ValueError: Если номер содержит не 16 символов или содержит не только цифры.
    """
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
    """
        Возвращает замаскированный номер счета в формате '**XXXX'.

        Оставляет только последние 4 цифры и добавляет '**' перед ними.
        Проверяет, что номер содержит минимум 4 цифры. Если проверка не пройдена,
        выбрасывается исключение ValueError.

        Args:
            account_number (str): Номер счета (только цифры, минимум 4 символа).

        Returns:
            str: Замаскированный номер счета.

        Raises:
            ValueError: Если номер содержит менее 4 символов или содержит нецифровые значения.
    """
    # Проверяем, что номер счета содержит хотя бы 4 цифры
    if not account_number.isdigit() or len(account_number) < 4:
        raise ValueError("Номер счета должен содержать не менее 4 цифр")

    # Берем только последние 4 цифры
    last_four_digits = account_number[-4:]

    # Формируем маску: **XXXX
    masked_account = f"**{last_four_digits}"

    return masked_account

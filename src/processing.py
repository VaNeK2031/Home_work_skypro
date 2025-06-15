def filter_by_state(data: list, state='EXECUTED'):
    """
        Фильтрует список словарей по значению ключа 'state'.

        Args:
            data (list of dict): Список словарей, представляющих данные.
            state (str, optional): Значение ключа 'state' для фильтрации.
                По умолчанию 'EXECUTED'.

        Returns:
            list of dict: Новый список, содержащий только те словари,
                у которых значение по ключу 'state' совпадает с указанным.
        """
    result = []
    for item in data:
        if item.get('state') == state:
            result.append(item)
    return result


def sort_by_date(date: list, ascending=False):
    """
       Возвращает новый список словарей, отсортированный по значению ключа 'date'.

       Сортировка выполняется на основе строковых значений поля 'date',
       которые предполагаются в формате ISO 8601 (например, '2023-01-01T12:34:56.789012').

       Args:
           data (list of dict): Список словарей, каждый из которых содержит ключ 'date'.
           ascending (bool, optional): Порядок сортировки: если True — по возрастанию даты,
               если False (по умолчанию) — по убыванию.

       Returns:
           list of dict: Новый список словарей, отсортированный по дате.
       """
    sorted_data = sorted(date, key=lambda x: x['date'], reverse=not ascending)
    return sorted_data

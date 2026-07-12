import json
import os
from datetime import datetime
from typing import Callable, Any, Generator


def create_id_generator(id_gen=0) -> Generator[int, Any, Any]:
    """
    Генератор последовательных ID
    """

    last_id = id_gen

    while True:
        last_id += 1
        yield last_id


def get_last_id_from_json(transaction_type=None) -> int:
    """
    Находит максимальный ID в JSON файле.
    Args:
        transaction_type: Тип транзакции ('income', 'expense' или None для общего ID)
    Returns:
        Максимальный ID или 0, если файл отсутствует, пуст или поврежден
    """

    if not os.path.exists(constants.PATH) or os.path.getsize(constants.PATH) == 0:
        return 0

    try:
        with open(constants.PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)

            if not data:
                return 0

            id_list: List[int] = []

            for daily_operations in data.values():

                for operation in daily_operations:

                    if transaction_type is None:
                        current_id = operation.get('id')

                    elif transaction_type == 'income':
                        current_id = operation.get('id_income')

                    elif transaction_type == 'expense':
                        current_id = operation.get('id_expense')

                    else:
                        current_id = None

                    if isinstance(current_id, int):  # Берем только если это число
                        id_list.append(current_id)

        return max(id_list) if id_list else 0

    except (json.JSONDecodeError, KeyError):  # Если файл поврежден или нет ключа 'id'
        return 0


def get_current_datetime() -> str:
    """
    Возвращает текущее время в формате yyyy-mm-dd hh:mm:ss
    """

    return datetime.now().strftime(constants.DATE_FMT)
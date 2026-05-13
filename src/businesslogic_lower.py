import itertools
import json
import os
from datetime import datetime
from typing import Callable, Any, Generator
from src import display, constants


def create_id_generator(id_gen=0) -> Generator[int, Any, Any]:
    """
    Генератор последовательных ID
    """

    last_id = id_gen

    while True:
        last_id += 1
        yield last_id


def get_last_id_from_json(t_type=None) -> int:
    """
    Находит максимальный ID в JSON файле.
    """
    if not os.path.exists(constants.PATH) or os.path.getsize(constants.PATH) == 0:
        return 0

    try:
        with open(constants.PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not data:
                return 0

            ids = []
            for day_ops in data.values():
                for op in day_ops:
                    if t_type is None:
                        val = op.get('id')
                    elif t_type == 'income':
                        val = op.get('id_income')
                    elif t_type == 'expense':
                        val = op.get('id_expense')
                    else:
                        val = None

                    if isinstance(val, int):  # Берем только если это число
                        ids.append(val)

        return max(ids) if ids else 0

    except (json.JSONDecodeError, KeyError):  # Если файл поврежден или нет ключа 'id'
        return 0




def validate_type_transaction(type_transaction) -> str:

    if type_transaction not in ['income', 'expense']:

        display.show_error_message("Type transaction must be Income or Expense")
        raise ValueError("Invalid transaction type")

    return type_transaction


def validate_amount(amount, min_value = 0.01, max_value = None, allow_zero = False) -> float | None:
    """
    Проверяет сумму, допускает не более 2 знаков после запятой
        min_value: минимальное значение (по умолчанию 0.01)
        max_value: максимальное значение (по умолчанию None - без ограничений)
        allow_zero: разрешать ли ноль (по умолчанию False)
    """


    while True:

        # Проверяем формат (целые или с запятой/точкой)
        if not amount.replace(',', '.').replace('.', '').isdigit():

            display.show_error_message("Error! The amount must contain only numbers, a comma, or a period")

            continue

        # Заменяем запятую на точку
        normalized = amount.replace(',', '.')

        # Проверяем количество знаков после запятой
        if '.' in normalized:

            parts = normalized.split('.')

            if len(parts) > 2:

                display.show_error_message("Error! The amount can only contain one comma or period")

                continue

            if len(parts[1]) > 2:

                display.show_error_message("Error! The amount may contain no more than 2 decimal places")

                continue

        try:
            amount = float(normalized)

            # Проверка на ноль
            if not allow_zero and amount == 0:

                display.show_info_message("The sum cannot be equal to zero!")

                continue

            # Проверка минимального значения
            if amount < min_value:

                display.show_info_message(f"The amount must be no less than {min_value}!")

                continue

            # Проверка максимального значения
            if max_value is not None and amount > max_value:

                display.show_info_message(f"The amount should not be more than {max_value}!")

                continue

            # Округляем до 2 знаков для денежных сумм
            return round(amount, 2)

        except ValueError:
            display.show_error_message("Error! Incorrect number format")

            continue



def validate_category(category_input: str, category_type: str) -> bool:

    allowed = constants.CATEGORIES.get(category_type, [])

    if category_input.strip().lower() in allowed:
        return True

    allowed_str = ", ".join(allowed).capitalize()

    display.show_error_message(f"Error! The {category_type} category must be: {allowed_str}")

    return False


def validate_description(description_type: str, type_name="Text") -> bool:

    # Проверка длины
    if len(description_type) > 255:

        display.show_error_message(f"Error! Text too long ({len(description_type)} > 255)")

        return False

    # Проверка на пустоту
    if not description_type.strip():

        display.show_error_message(f"Error!{type_name} cannot be empty!")

        return False

    # Проверка символов
    for char in description_type:

        if not (char.isalpha() or char.isdigit() or char.isspace() or char in ".,-"):

            display.show_error_message(f"Error! Invalid character: '{char}'")

            return False

    return True


def get_current_datetime() -> str:
    return datetime.now().strftime(constants.DATE_FMT)


def try_write_journal_entry_income(gen_total, gen_income, type_transaction, amount, category_income, description_income, date) -> bool:
    # 1. Создаем запись
    entry = {
        "id": next(gen_total),
        "id_income": next(gen_income), # Это функция для доходов, просто берем следующий ID дохода
        "id_expense": None,            # Для доходов поле расхода всегда пустое
        "type": validate_type_transaction(type_transaction),
        "amount": validate_amount(amount),
        "category": validate_category_income(category_income),
        "description": validate_description_income(description_income),
        "datetime": date
    }

    # 2. Читаем текущий файл
    data = {}
    if os.path.exists(constants.PATH) and os.path.getsize(constants.PATH) > 0:
        try:
            with open(constants.PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {}

    # 3. Определяем ключ даты для группировки (первые 10 символов: YYYY-MM-DD)
    date_key = date[:10]

    # 4. Добавляем запись в нужную дату
    if date_key not in data:
        data[date_key] = []
    data[date_key].append(entry)

    # 5. Сохраняем обратно в файл
    try:
        with open(constants.PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True # Подтверждение успешной записи
    except Exception:
        return False


def write_journal_entry_expense(last_id, type_transaction, amount, category, description, date):
    pass
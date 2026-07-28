import itertools
import json
import os
from src import display, constants


def validate_type_transaction(input_type_transaction: str) -> str | bool:

    normalized_type = input_type_transaction.strip().lower()

    # Проверяем, есть ли тип в ключах словаря CATEGORIES
    if normalized_type in constants.CATEGORIES:
        return normalized_type

    # Если нет - формируем сообщение об ошибке
    allowed_types = ", ".join(constants.CATEGORIES.keys())
    display.show_error_message(f"Введен неверный тип операции. Допустимые типы: {allowed_types}")
    return False


def validate_amount(input_amount, min_value = 0.01, max_value = None, allow_zero = False) -> bool | str:
    """
    Проверяет сумму, допускает не более 2 знаков после запятой
        min_value: минимальное значение (по умолчанию 0.01)
        max_value: максимальное значение (по умолчанию None - без ограничений)
        allow_zero: разрешать ли ноль (по умолчанию False)
    """

    # Проверяем формат (целые или с запятой/точкой)
    if not isinstance(input_amount, str):
        input_amount = str(input_amount)


    # Разрешаем только цифры и разделители
    summa = input_amount.strip()

    if not summa:
        display.show_error_message("Сумма должна содержать только цифры, запятую или точку")
        return False


    # Заменяем запятую на точку
    normalized = summa.replace(',', '.')

    # Проверка “что похоже на число”
    if not normalized.replace('.', '').isdigit():

        display.show_error_message("Сумма должна содержать только цифры, запятую или точку")
        return False


    # Проверяем количество знаков после запятой
    if '.' in normalized:
        parts = normalized.split('.')

        if len(parts) != 2:

            display.show_error_message("Сумма может содержать только одну запятую или точку.")
            return False

        if len(parts[1]) > 2:

            display.show_error_message("Сумма не должна содержать более 2 знаков после запятой.")
            return False


    # Преобразовываем в float
    try:
        value = float(normalized)

    except ValueError:
        display.show_error_message("Сумма должна содержать только цифры, запятую или точку")
        return False


    # Проверяем по значениям
    if not allow_zero and value == 0:

        display.show_info_message("Сумма не может быть равна нулю")
        return False

    if value < min_value:

        display.show_info_message(f"Сумма должна быть не меньше {min_value}")
        return False

    if max_value is not None and value > max_value:

        display.show_info_message(f"Сумма не должна превышать {max_value}")
        return False


    # Возвращаем значение в строку
    return str(input_amount)


def validate_category(category_input: str, category_type: str) -> str | bool:

    allowed = constants.CATEGORIES.get(category_type, [])

    if category_input.strip().lower() in allowed:
        return category_input

    allowed_str = ", ".join(allowed).capitalize()

    display.show_error_message(f"Введена неверная категория. Допустимые категории: {allowed_str}")
    return False


def validate_description(description_type: str) -> bool | str:

    # Проверка типа
    if description_type is None:
        display.show_error_message("Текст не может быть пустым")
        return False

    # Приводим к строке
    description_type = str(description_type)

    # Проверка длины
    if len(description_type) > 255:

        display.show_error_message(f"Текст слишком длинный ({len(description_type)} символов > 255 символов)")
        return False

    # Проверка на пустоту
    if not description_type.strip():

        display.show_error_message(f"Текст не может быть пустым")
        return False

    # Проверка символов
    for char in description_type:

        if not (char.isalpha() or char.isdigit() or char.isspace() or char in ".,-"):

            display.show_error_message(f"Недопустимый символ: '{char}'")
            return False

    return description_type



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
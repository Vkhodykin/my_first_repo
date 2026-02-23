import itertools
import json
from datetime import datetime
from typing import Callable, Any
from src import display
from src import constants


def create_id_generator(start=1) -> Callable[[], int]:
    """
    Генератор последовательных ID
    """

    counter = start

    def generate() -> int:

        nonlocal counter
        current = counter
        counter += 1

        return current

    return generate


def validate_type_transaction(type_transaction) -> bool:

    if type_transaction not in ['income', 'expense']:

        display.show_error_message("Type transaction must be Income or Expense")

    return True


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



def validate_category_income(category_income):

    if category_income not in ['regular', 'random']:

        display.show_error_message("The income category must be Regular or Random")

    return True


def validate_category_expense(category_expense):

    if category_expense not in ['mandatory', 'optional', 'saving']:

        display.show_error_message("The expense category must be Mandatory or Optional or Saving")

    return True


def validate_description_income(description_income):

    while True:

    # Проверка длины
        if len(description_income) > 255:

            display.show_error_message(f"Error! Text too long ({len(description_income)} > 255)")

            continue

    # Проверка на пустоту
        if not description_income.strip():

            display.show_error_message("Text cannot be empty!")

            continue

    # Проверка символов
        valid = True

        for char in description_income:

            if not (char.isalpha() or char.isdigit() or char.isspace()):

                display.show_error_message(f"Error! Invalid character: '{char}'")

                valid = False

                break

        if valid:
            return description_income


def validate_description_expense(description_expense):

    while True:

        # Проверка длины
        if len(description_expense) > 255:
            display.show_error_message(f"Error! Text too long ({len(description_expense)} > 255)")

            continue

        # Проверка на пустоту
        if not description_expense.strip():
            display.show_error_message("Text cannot be empty!")

            continue

        # Проверка символов
        valid = True

        for char in description_expense:

            if not (char.isalpha() or char.isdigit() or char.isspace()):
                display.show_error_message(f"Error! Invalid character: '{char}'")

                valid = False

                break

        if valid:
            return description_expense


def get_current_datetime() -> str:

    return datetime.now().strftime(DATE_FMT)


def formater_journal() -> dict[str, Callable[[], int] | str | Any]:

    entry = {
        "id": create_id_generator(),
        "type": type_transaction(),
        "amount": amount(),
        "category": category_income(),
        "description": description_income(),
        "datetime": get_current_datetime()
    }

    return entry


def try_write_journal_entry_income(create_id_generator, type_transaction, amount, category_income, description_income, get_current_datetime) -> None:

    # Читаем или создаем файл
    try:
        with open(constants.PATH, "r", encoding="utf-8") as f:

            data = json.load(f)

    except:

        data = []

    # Добавляем запись
    data.append(formater_journal())

    # Сохраняем
    with open(constants.PATH, "w", encoding="utf-8") as f:

        json.dump(data, f, ensure_ascii=False, indent=None, separators=(',', ':'))


def write_journal_entry_expense(create_id_generator, type_transaction, amount, category, description, get_current_datetime):
    pass
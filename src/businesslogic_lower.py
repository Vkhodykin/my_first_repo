import itertools
from typing import Callable
from src import display
from src import core

def create_id_generator(start=1, prefix='') -> Callable[[], str]:
    """
    Генератор последовательных ID
    """

    counter = start

    def generate() -> str:

        nonlocal counter
        current = counter
        counter += 1

        return f"{prefix}{current}" if prefix else current

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
        core.amount = amount.strip()

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


def validate_category_income(category_income):

    if category_income not in ['regular', 'random']:

        display.show_error_message("The income category must be Regular or Random")

    return True


def validate_category_expense(category_expense):

    if category_expense not in ['mandatory', 'optional', 'saving']:

        display.show_error_message("The expense category must be Mandatory or Optional or Saving")

    return True


def validate_description_income(description_income):
    pass

def validate_description_expense(description_expense):
    pass


def write_journal_entry(type_transaction, amount, category, description):
    pass

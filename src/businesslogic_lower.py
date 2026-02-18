import itertools
from typing import Callable


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


def validate_type_transaction(type_transaction):
    pass

def validate_amount(amount):
    pass

def validate_category(category):
    pass

def validate_description(description):
    pass

def write_journal_entry(type_transaction, amount, category, description):
    pass

from businesslogic_lower import *

def add_journal_entry(type_transaction: str, amount: float, category: str, description: str) -> None:

    if not validate_type_transaction(type_transaction):
        raise ValueError("Invalid transaction type")

    if not validate_amount(amount):
        raise ValueError("Invalid amount")

    if not validate_category(category):
        raise ValueError("Invalid category")

    if not validate_description(description):
        raise ValueError("Invalid description")

    write_journal_entry(type_transaction, amount, category, description)

    pass

def show_entries():
    pass

def find_entries_by_type(type_transaction):
    pass


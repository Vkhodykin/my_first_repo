from src import businesslogic_lower as bll


def try_add_journal_entry(type_transaction: str, amount: float, category: str, description: str) -> bool:

    if not bll.validate_type_transaction(type_transaction):
        return False

    if not bll.validate_amount(amount):
        return False

    if not bll.validate_category(category):
        return False

    if not bll.validate_description(description):
        return False

    bll.write_journal_entry(type_transaction, amount, category, description)

    return True


def show_entries():
    pass


def find_entries_by_type(type_transaction):
    pass


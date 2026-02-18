from src import businesslogic_lower as bll


def try_add_journal_entry_income(create_id_generator: int, type_transaction: str, amount: str, category_income: str, description_income: str) -> bool:

    if not bll.create_id_generator():
        return False

    if not bll.validate_type_transaction(type_transaction):
        return False

    if not bll.validate_amount(amount):
        return False

    if not bll.validate_category_income(category_income):
        return False

    if not bll.validate_description_income(description_income):
        return False

    bll.write_journal_entry_income(create_id_generator, type_transaction, amount, category_income, description_income)

    return True


def try_add_journal_entry_expense(create_id_generator: int, type_transaction: str, amount: float, category_expense: str,
                                  description_expense: str) -> bool:

    if not bll.create_id_generator():
        return False

    if not bll.validate_type_transaction(type_transaction):
        return False

    if not bll.validate_amount(amount):
        return False

    if not bll.validate_category_expense(category_expense):
        return False

    if not bll.validate_description_expense(description_expense):
        return False

    bll.write_journal_entry_expense(create_id_generator, type_transaction, amount, category_expense, description_expense)

    return True


def show_entries():
    pass


def find_entries_by_type(type_transaction):
    pass


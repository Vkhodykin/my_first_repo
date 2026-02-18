from src import businesslogic_lower as bll


def try_add_journal_entry(create_id_generator: str, type_transaction: str, amount: float, category_income: str | None,
                          category_expense: str | None, description_income: str | None, description_expense: str | None) -> bool:

    if not bll.create_id_generator():
        return False

    if not bll.validate_type_transaction(type_transaction):
        return False

    if not bll.validate_amount(amount):
        return False

    if not bll.validate_category_income(category_income):
        return False

    if not bll.validate_category_expense(category_expense):
        return False

    if not bll.validate_description_income(description_income):
        return False

    if not bll.validate_description_expense(description_expense):
        return False

    bll.write_journal_entry(create_id_generator, type_transaction, amount, category_income, category_expense,
                            description_income, description_expense)

    return True


def show_entries():
    pass


def find_entries_by_type(type_transaction):
    pass


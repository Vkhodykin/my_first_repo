from src import businesslogic_lower as bll


def validate_type_transaction(input_type_transaction: str) -> bool:

    if not bll.validate_type_transaction(input_type_transaction):
        return False

    return True


def validate_amount(input_amount):

    if not bll.validate_amount(input_amount):
        return False

    return True


def validate_category(category_input: str, category_type: str) -> bool:

    if not bll.validate_category(category_input, category_type):
        return False

    return True


def validate_description(description_type):

    if not bll.validate_description(description_type):
        return False

    return True


def try_add_journal_entry_income(gen_total, 
                                 gen_income, 
                                 input_type_transaction: str, 
                                 input_amount: str, 
                                 category_input: str,
                                 description_type: str, 
                                 date: str) -> bool:

    if not bll.validate_type_transaction(input_type_transaction):
        return False

    if not bll.validate_amount(input_amount):
        return False

    if not bll.validate_category(category_input, 'income'):
        return False

    if not bll.validate_description(description_type):
        return False

    bll.try_write_journal_entry_income(gen_total, 
                                       gen_income, 
                                       input_type_transaction, 
                                       input_amount, 
                                       category_input, 
                                       description_type, 
                                       date)
    return True


def try_add_journal_entry_expense(create_id_generator: int, type_transaction: str, amount: float, category_expense: str,
                                  description_expense: str, get_current_datetime: str) -> bool:

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

    if not bll.get_current_datetime():
        return False

    bll.write_journal_entry_expense(create_id_generator, type_transaction, amount, category_expense, description_expense,
                                    get_current_datetime)

    return True


def show_entries():
    pass


def find_entries_by_type(type_transaction):
    pass


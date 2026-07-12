import json
import os

from src import display
from src import constants
from src import help
from src import businesslogic_upper as blu
from src import support_utils as su


def start():
    """
    Запуск
    :return:
    """

    display.show_notification_message(help.COMMANDS_HELP)


def main_loop():
    """
    Работа
    :return:
    """

    is_working = True
    while is_working:

        display.show_info_message("Введите команду")
        user_input = input(">> ")

        if user_input == constants.INFO_COMMAND:

            display.show_notification_message(help.PROGRAM_INFO)


        elif user_input == constants.ADD_COMMAND:

            create_a_new_entry = True
            while create_a_new_entry:

                gen_total = su.create_id_generator(su.get_last_id_from_json(transaction_type=None))
                gen_income = su.create_id_generator(su.get_last_id_from_json(transaction_type='income'))
                gen_expense = su.create_id_generator(su.get_last_id_from_json(transaction_type='expense'))

                date = su.get_current_datetime()


                display.show_info_message("Введите тип операции (Income/Expense):")
                input_type_transaction = input(">> ")

                if not blu.validate_type_transaction(input_type_transaction):
                    continue


                if input_type_transaction == "income":

                    income_amount = True
                    while income_amount:

                        display.show_info_message("Введите сумму дохода:")
                        input_amount = input(">> ")

                        if blu.validate_amount(input_amount):
                            break


                    income_category = True
                    while income_category:
                        
                        display.show_info_message("Введите категорию доходов (Regular/Random):")
                        category_input = input(">> ")

                        if blu.validate_category(category_input, 'income'):
                            break


                    income_description = True
                    while income_description:
                        
                        display.show_info_message("Введите описание доходов (не более 255 символов):")
                        description_type = input(">> ")

                        if blu.validate_description(description_type):
                            break


                    write_operation = blu.try_add_journal_entry_income(gen_total,
                                                                       gen_income,
                                                                       input_type_transaction,
                                                                       input_amount,
                                                                       category_input,
                                                                       description_type,
                                                                       date)

                    if write_operation:
                        display.show_notification_message("Операция записана успешно")

                        display.show_confirmation_message("Хотите продолжить запись данных? (y/n)")
                        confirmed = su.confirm(">> ")
                        
                        if confirmed:
                            # продолжить
                            continue
                        else:
                            # отменить
                            break


                    else:
                        display.show_error_message("Ошибка при записи операции")
                        display.show_info_message("Операция не записана")

                else:
                    display.show_info_message("Введен неверный тип операции")
                    continue


            elif type_transaction == "expense":

                category_expense = input("Введите категорию расходов (Mandatory/Optional/Saving) >> ").strip().lower()

                description_expense = input("Введите описание расходов (не более 255 символов) >> ")

                if blu.try_add_journal_entry_expense(gen_total, type_transaction, amount, category_expense,
                                                     description_expense, date):

                    display.show_info_message("Операция записана успешно")


            else:
                display.show_error_message("Введено некорректное значение. Введите еще раз")

                continue


        elif user_input == constants.SHOW_COMMAND:
            pass

        elif user_input == constants.DEL_COMMAND:
            pass

        elif user_input == constants.EDIT_COMMAND:
            pass

        elif user_input == constants.FIND_COMMAND:
            pass

        elif user_input == constants.TYPE_COMMAND:
            pass

        elif user_input == constants.CAT_COMMAND:
            pass

        elif user_input == constants.PERIOD_COMMAND:
            pass

        elif user_input == constants.STATS_COMMAND:
            pass

        elif user_input == constants.EXIT_COMMAND:
            break

        else:
            display.show_error_message("Введено некорректное значение. Введите еще раз >>")
            continue

def stop():
    """
    Завершение
    :return:
    """

    display.show_info_message("Работа программы завершена")


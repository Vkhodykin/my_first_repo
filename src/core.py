import json
import os

from src import display
from src import constants
from src import businesslogic_upper as blu
from src.businesslogic_lower import create_id_generator, get_last_id_from_json, get_current_datetime


def start():
    """
    Запуск
    :return: 
    """



    display.show_info_message("Для начала работы выберите что вы хотите сделать. Введите команду:\n "
                              "1 - info\n "
                              "2 - add\n "
                              "3 - show\n "
                              "4 - del\n"
                              "5 - edit\n "
                              "6 - find\n "
                              "7 - type\n "
                              "8 - cat\n "
                              "9 - period\n "
                              "10 - stats\n "
                              "11 - exit")


def main_loop():
    """
    Работа
    :return: 
    """

    while True:

        user_input = input(">> ")

        if user_input == constants.INFO_COMMAND:
            pass


        elif user_input == constants.ADD_COMMAND:


            gen_total = create_id_generator(get_last_id_from_json(t_type=None))
            gen_income = create_id_generator(get_last_id_from_json(t_type='income'))
            gen_expense = create_id_generator(get_last_id_from_json(t_type='expense'))

            date = get_current_datetime()

#
            type_transaction = input("Введите тип операции (Income/Expense): >> ").strip().lower()

            amount = input("Введите сумму >> ").strip()


            if type_transaction == "income":

                category_income = input("Введите категорию доходов (Regular/Random) >> ").strip().lower()

                description_income = input("Введите описание доходов (не более 255 символов) >> ")

                if blu.try_add_journal_entry_income(gen_total, gen_income, type_transaction, amount, category_income,
                                                    description_income, date):

                    display.show_info_message("Операция записана успешно")


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


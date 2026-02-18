from src import display
from src import constants
from src import businesslogic_upper as blu


def start():
    """
    Запуск
    :return: 
    """

    display.show_info_message("Для начала работы выберите что вы хотите сделать. Введите команду:\n 1 - info\n 2 - add\n 3 - show\n 4 - del\n"
                      "5 - edit\n 6 - find\n 7 - type\n 8 - cat\n 9 - period\n 10 - stats\n 11 - exit")


def main_loop():
    """
    Работа
    :return: 
    """

    while True:

        user_input = input(">>")

        if user_input == constants.INFO_COMMAND:
            pass

        elif user_input == constants.ADD_COMMAND:

            type_transaction = input("Тип операции >>")
            amount = input("Сумма >>")
            category = input("Категория >>")
            description = input("Описание >>")

            if blu.try_add_journal_entry(type_transaction, amount, category, description):

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


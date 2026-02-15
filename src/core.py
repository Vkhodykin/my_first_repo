from display import show_info_message, show_error_message


def start():
    """
    Запуск
    :return: 
    """

    show_info_message("Для начала работы выберите что вы хотите сделать:\n 1 - info\n 2 - add\n 3 - show\n 4 - del\n"
                      "5 - edit\n 6 - find\n 7 - type\n 8 - cat\n 9 - period\n 10 - stats\n 11 - exit")


def main_loop():
    """
    Работа
    :return: 
    """

    while True:

        user_input = input(">>")

        if user_input == "info":
            pass

        elif user_input == "add":
            pass

        elif user_input == "show":
            pass

        elif user_input == "del":
            pass

        elif user_input == "edit":
            pass

        elif user_input == "find":
            pass

        elif user_input == "type":
            pass

        elif user_input == "cat":
            pass

        elif user_input == "period":
            pass

        elif user_input == "stats":
            pass

        elif user_input == "exit":
            break

        else:
            show_error_message("Введено некорректное значение. Введите еще раз >>")
            continue

def stop():
    """
    Завершение
    :return:
    """
    pass


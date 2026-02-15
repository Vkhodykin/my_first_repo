from src.constants import *

def show_error_message(message) -> None:
    print(f"{ERROR_MESSAGE_STYLE}{message}{DEFAULT_MESSAGE_STYLE}...")

def show_info_message(message) -> None:
    print(f"{INFO_MESSAGE_STYLE}{message}{DEFAULT_MESSAGE_STYLE}...")


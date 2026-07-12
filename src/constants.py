
ERROR_MESSAGE_STYLE = "\x1b[1;31m"
DEFAULT_MESSAGE_STYLE = "\x1b[0m"
INFO_MESSAGE_STYLE = "\x1b[1;33m"
NOTIFICATION_MESSAGE_STYLE = "\x1b[1;32m"
CONFIRMATION_MESSAGE_STYLE = "\x1b[1;35m"

PATH = "data/journal.json"

INFO_COMMAND = "info"
ADD_COMMAND = "add"
SHOW_COMMAND = "show"
DEL_COMMAND = "del"
EDIT_COMMAND = "edit"
FIND_COMMAND = "find"
TYPE_COMMAND = "type"
CAT_COMMAND = "cat"
PERIOD_COMMAND = "period"
STATS_COMMAND = "stats"
EXIT_COMMAND = "exit"
HELP_COMMAND = ["help", "?"]

DATE_FMT = "%Y-%m-%d %H:%M:%S"

CATEGORIES = {
    'income': ['regular', 'random'],
    'expense': ['mandatory', 'optional', 'saving']
}
import logging

class LogColors:
    BLUE1 = '\033[95m'
    BLUE2 = '\033[96m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    NOCOLOR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    START_ERROR = ERROR + 'ERROR |❌| '
    START_WARNING = WARNING + '|🚀| '
    START_INFO = BLUE2 + '|🚀| '
    START_TITLE = WARNING + '  |·'
    START_SUBTITLE = BLUE1 + '  |·'
    START_SUBTITLE_2 = BLUE2 + '  |·'
    START_DEBUG = BLUE2 + '|DEBUG| '
    START_SUCCESS = SUCCESS + '|🚀| '
    LOADING = BLUE1 + 'ººº' + NOCOLOR
    INTERSECTION = ERROR + ' · '


class Logger:
    def __init__(self, log_level: str = "INFO"):
        self.log = logging.basicConfig(
            format="%(levelname)-2s %(message)s",
            level=log_level,
            encoding='utf-8'
        )

    def error(self, msg: str, exception: Exception = None):
        logging.error(f"{LogColors.START_ERROR}{msg}{LogColors.NOCOLOR}")
        exit(1)

    def warn(self, msg: str, exception: Exception = None):
        logging.warning(f"{LogColors.START_WARNING}{msg}{LogColors.NOCOLOR}")

    def info(self, msg: str, exception: Exception = None):
        logging.info(f"{LogColors.START_SUCCESS}{msg}{LogColors.NOCOLOR}")

    def debug(self, msg: str, exception: Exception = None):
        logging.debug(f"{LogColors.START_DEBUG}{msg}{LogColors.NOCOLOR}")
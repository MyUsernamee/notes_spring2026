import sys
import logging
from termcolor import colored

from . import TAB_WIDTH, logger, LOG_COLORS, CENTERING_WIDTH

class Formatter(logging.Formatter):
    def format(self, record: logging.LogRecord):
        level = colored(record.levelname, LOG_COLORS[record.levelname]).center(CENTERING_WIDTH)
        name = record.name
        msg = record.getMessage()
        return f'[{level}] {name} : {msg.expandtabs(TAB_WIDTH)}'

def init_logger():
    sh = logging.StreamHandler()
    f = Formatter()
    sh.setFormatter(f)

    logger.setLevel(logging.INFO)
    logger.addHandler(sh)

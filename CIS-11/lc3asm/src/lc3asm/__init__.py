import logging
import tree_sitter_lc3asm as tslc3asm
from tree_sitter import Language

LC3_LANGUAGE = Language(tslc3asm.language())

SEPARATOR_WIDTH = 32
SEPARATOR = '-' * SEPARATOR_WIDTH

TAB_WIDTH = 2
CENTERING_WIDTH = 18

LOG_COLORS = {
    'DEBUG': 'green',
    'INFO': 'white',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'purple'
}

logger = logging.getLogger(__name__)


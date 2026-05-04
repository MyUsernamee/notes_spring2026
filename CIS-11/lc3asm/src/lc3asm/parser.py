from tree_sitter import LogType, Parser, Language
from logging import DEBUG

from lc3asm.error import Error
from lc3asm.syntax import validate_syntax
from lc3asm import logger, LC3_LANGUAGE
logger = logger.getChild('parser')


def make_parser() -> Parser:
    logger.debug('Making parser...')
    return Parser(LC3_LANGUAGE, logger = lambda level, msg: logger.log(1, msg))

def parse_tree(path: PathLike, source: bytes, parser: Parser) -> (Tree, Error | None):
    logger.debug('Parsing file %s.', path)
    tree = parser.parse(source)
    error = validate_syntax(path, tree)

    logger.debug('Parsed %s, with the following errors: %s', path, error)
    return tree, error

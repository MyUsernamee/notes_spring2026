from functools import reduce
from logging import DEBUG
from os import PathLike
from pathlib import Path
from tree_sitter import Language, Parser, Query, QueryCursor, Tree

from lc3asm.error import Location

from . import LC3_LANGUAGE, SEPARATOR, logger
from .parser import parse_tree

logger = logger.getChild('preprocessor')

def get_includes(path: PathLike, tree: Tree) -> List[(Path, Location)]:
    """Get all paths to files attemping to be included in the tree"""

    local_logger = logger.getChild('get_includes')

    query = Query(LC3_LANGUAGE, """(statement (directive) (string_literal) @include)""")
    local_logger.debug("Making includes query...")
    cursor = QueryCursor(query)
    captures = cursor.captures(tree.root_node)

    local_logger.debug('Ran includes query for %s, got %s...', path, captures)
    local_logger.debug('Converting queries to paths...')

    ret = [(Path(capture.text.decode()), Location.from_node(path, tree, capture)) for capture in reduce(lambda a, b: a+b, captures.values())]

    return ret    

def preprocess(paths: List[PathLike], source: bytes, parser: Parser) -> str:
    logger.debug('Starting preprocessing...')

    if not isinstance(paths, list):
        logger.debug('paths (%s) is not a list, convert it to one...', paths)
        paths = [paths]

    logger.debug('Getting include directives for %s...', paths[-1])
    tree, error = parse_tree(paths[-1], source, parser)

    if error:
        logger.error(f"\n{SEPARATOR}\nError while parsing file {paths[-1]}.\n  {str(error).replace('\n','\n\t')}\n{SEPARATOR}")

    includes = get_includes(paths[-1], tree)

# %%


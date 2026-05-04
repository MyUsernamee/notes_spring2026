from os import PathLike
from tree_sitter import Tree

from lc3asm.parser import parse_tree
from lc3asm import logger
logger = logger.getChild('assembler')


def assemble(path: PathLike, source: bytes, parser: Tree) -> (bytes, List[Error] | Error | None):
    logger.debug('Starting assembler...')
    tree, error = parse_tree()

    if error:
        logger.error(f"\n{SEPARATOR}\nError while parsing file {paths[-1]}.\n  {str(error).replace('\n','\n\t')}\n{SEPARATOR}")
        return source, error

    identifiers = get_identifiers(path, parser)

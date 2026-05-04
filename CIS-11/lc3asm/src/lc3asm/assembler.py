from dataclasses import dataclass
from os import PathLike
from typing import Dict
from tree_sitter import Tree, Query, QueryCursor

from lc3asm.parser import parse_tree
from lc3asm.instruction import Instruction
from lc3asm import LC3_LANGUAGE, logger
logger = logger.getChild('assembler')

@dataclass
class AssemblerState:
    path: PathLike
    source: bytes
    tree: Tree
    symbol_table: Dict[bytes, int]
    obj_file: ObjFile

@dataclass
class ObjFile:
    path: PathLike
    origin: int
    memory_locations: List[Instruction]

def get_identifiers(state: AssemblerState):
    logger.debug('Getting identifiers for %s', path)

    query = Query("""
        (statement (identifier) @identifier .)
    """)
    cursor = QueryCursor(LC3_LANGUAGE, query)
    captures = cursor.capture(state.tree)

    logger.debug('Ruan identifier capture, got %s...', captures)

def assemble(path: PathLike, source: bytes, parser: Tree) -> (bytes, List[Error] | Error | None):
    logger.debug('Starting assembler...')
    tree, error = parse_tree()

    if error:
        logger.error(f"\n{SEPARATOR}\nError while parsing file {paths[-1]}.\n  {str(error).replace('\n','\n\t')}\n{SEPARATOR}")
        return source, error

    state = AssemblerState(path, source, tree, {})

    errors = get_identifiers(state)
    if errors:
        return (source, error)





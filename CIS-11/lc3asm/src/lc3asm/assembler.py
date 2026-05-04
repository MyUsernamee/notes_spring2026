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
    logger.debug('Getting identifiers for %s', state.path)

    query = Query(LC3_LANGUAGE, """
        (statement (identifier) @identifier .)
    """)
    cursor = QueryCursor(query)
    captures = cursor.captures(state.tree.root_node)

    logger.debug('Ran identifier capture, got %s...', captures)

    for capture in captures['identifier']:
        logger.debug('Adding %s to the symbol_table...', capture.text)
        state.symbol_table[capture.text] = 0

def assemble(path: PathLike, source: bytes, parser: Tree) -> (bytes, List[Error] | Error | None):
    logger.debug('Starting assembler...')
    tree, error = parse_tree(path, source, parser)

    if error:
        logger.error(f"\n{SEPARATOR}\nError while parsing file {paths[-1]}.\n  {str(error).replace('\n','\n\t')}\n{SEPARATOR}")
        return source, error

    state = AssemblerState(path, source, tree, {}, ObjFile(path, 0, []))

    errors = get_identifiers(state)
    if errors:
        return (source, errors)

    return (b'', errors)




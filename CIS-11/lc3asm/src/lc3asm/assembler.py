from dataclasses import dataclass
from os import PathLike
from pathlib import Path
from typing import Dict
from lc3asm.error import Error, ErrorType
from tree_sitter import Tree, Query, QueryCursor, Node

from lc3asm.parser import parse_tree
from lc3asm.instruction import Instruction, OpCode
from lc3asm.error import Error, ErrorType, Location
from lc3asm import LC3_LANGUAGE, logger
logger = logger.getChild('assembler')

@dataclass
class AssemblerState:
    path: Path
    source: bytes
    tree: Tree
    ir_file: IrFile | None
    obj_file: ObjFile | None

@dataclass
class IrFile:
    origin: int
    symbol_table: Dict[bytes, int]
    memory_locations: List[UnlinkedInstruction]

@dataclass
class ObjFile:
    origin: int
    memory_locations: List[Instruction]

def get_identifiers(state: AssemblerState):
    logger.debug('Getting identifiers for %s', state.path)

    query = Query(LC3_LANGUAGE, """
        (statement . (identifier) @identifier )
    """)
    cursor = QueryCursor(query)
    captures = cursor.captures(state.tree.root_node)

    logger.debug('Ran identifier capture, got %s...', captures)

    if 'identifier' not in captures:
        logger.debug('No identifiers found in %s', state.path)
        return

    for capture in captures['identifier']:
        logger.debug('Adding %s to the symbol_table...', capture.text)
        state.symbol_table[capture.text] = 0

    logger.debug('Done finding identifiers, symbol_table is %s', state.symbol_table)

def handle_identifier(state: AssemblerState, ir_file: IrFile, cursor: TreeCursor):
    if cursor.node.text in ir_file.symbol_table:
        err = make_error(state, cursor, f'The label {cursor.node.text} is already defined.')
        return err
    ir_file.symbol_table[cursor.node.text] = len(ir_file.memory_locations)
    return None

def handle_directive(state: AssemblerState, ir_file: IrFile, c: TreeCursor):
    return None

def handle_opcode(state: AssemblerState, ir_file: IrFile, c: TreeCursor):
    memonic_text = c.node.text.decode().upper()
    if memonic_text not in dir(OpCode):
        return make_error(state, c, f'Unrecognized OpCode {memonic_text}')

    memonic = OpCode[memonic_text]
    logger.debug('Found opcode %s', memonic)

def make_error(state: AssemblerState, c: TreeCursor, msg: str, err=ErrorType.AssemblerError) -> Error:
    loc = Location.from_node(state.path, state.tree, c.node, msg=msg)
    error = Error([loc], err) 
    logger.error('%s', error)
    return error

def number_literal(node: Node):
    t = node.text.decode()
    if node.type != 'base_literal':
        return int(t)
    if t.startswith('#'):
        return int(t[1:])
    return int('0' + t, 0)

def build_ir(state: AssemblerState):
    logger.debug('Building intermediate representation for %s', state.path)     
    state.ir_file = IrFile(None, {}, [])
    c = state.tree.walk()
    c.goto_first_child() # source_file -> statement

    c0 = c.node.child(0)
    c1 = c.node.child(1)

    if not (c0.type == "directive" and c0.text.lower() == b".orig"):
        err = make_error(state, c, 'The first statement in a source file should be an .ORIG statment.')
        return err
    if c1.type != 'base_literal':
        err = make_error(state, c, f'Expected a number offset for .ORIG, got {c1}')
        return err

    state.ir_file.origin = number_literal(c1)
    
    while c.goto_next_sibling():
        c0 = c.node.child(0).walk()
        c0.goto_first_child()

        logger.debug('At %s', c0.node)
        
        if c0.node.type == 'identifier':
            logger.debug('Found identifier %s', c0.node)
            handle_identifier(state, state.ir_file, c0)
            c0.goto_next_sibling()

        if c0.node.type == 'directive':
            handle_directive(state, state.ir_file, c0)
            continue

        if c0.node.type == 'opcode':
            handle_opcode(state, state.ir_file, c0)
            continue

def assemble(path: PathLike, source: bytes, parser: Tree) -> (ObjFile | None, IrFile | None, List[Error] | Error | None):
    logger.debug('Starting assembler...')
    tree, error = parse_tree(path, source, parser)

    if error:
        logger.error(f"\n{SEPARATOR}\nError while parsing file {paths[-1]}.\n  {str(error).replace('\n','\n\t')}\n{SEPARATOR}")
        return (None, None, error)
    
    state = AssemblerState(Path(path), source, tree, None, None)

    # errors = get_identifiers(state)
    # if errors:
    #     return (None, None, errors)

    errors = build_ir(state)
    if errors:
        return (None, None, errors)

    return state.obj_file, state.ir_file, errors




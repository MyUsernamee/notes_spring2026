from os import PathLike
import tree_sitter_lc3asm 
from tree_sitter import Tree

def assemble(path: PathLike, source: bytes, parser: Tree) -> bytes:
    return b''

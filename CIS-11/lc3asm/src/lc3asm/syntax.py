from dataclasses import dataclass
from functools import reduce
from os import PathLike
from tree_sitter import Query, QueryCursor, Tree

from lc3asm import LC3_LANGUAGE, logger
logger = logger.getChild('syntax')

from .error import Error, ErrorType
from lc3asm.error import Location

def validate_syntax(path: PathLike, tree: Tree) -> Error | None:
    """Validates an AST and return true if there are no syntactic error."""
    logger.debug('Validating the syntax for %s...', path)
    error_query = Query(LC3_LANGUAGE, """
        (MISSING) @missing
        (ERROR) @error
    """,)
    cursor = QueryCursor(error_query)
    captures = cursor.captures(tree.root_node)

    if len(captures) == 0:
        return
   
    locations = [node for node in reduce(lambda a, b: a + b, captures.values())]

    lookaheads = []
    for node in locations:
        lookahead = LC3_LANGUAGE.lookahead_iterator(node.child(0).parse_state)
        possible_tokens = lookahead.names()
        expected_msg = f'Unexpected token; Expected one of {", ".join([f"\"{a}\"" for a in possible_tokens])}'
        lookaheads.append(expected_msg)

    logger.debug('Lookaheads : %s', lookaheads)
    locations = [Location.from_node(path, tree, node, msg=expected) for node, expected in zip(locations, lookaheads)]
    
    errors = Error(locations, ErrorType.SyntaxError)

    return errors


# %%


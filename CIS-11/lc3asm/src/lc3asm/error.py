import curses
from dataclasses import dataclass
from enum import Enum, auto
from logging import Logger
from termcolor import colored
from os import PathLike
import re

from tree_sitter import Node, Tree

from . import logger
logger = logger.getChild('error')

class ErrorType(Enum):
    UnkownError = auto()
    SyntaxError = auto()

@dataclass
class Location:
    start: int
    end: int
    line_start: int
    line_end: int
    path: PathLike
    source: str
    msg: str

    def __init__(self, path: PathLike, source, start, end, line_start, line_end=None, msg=""):
        if not line_end:
            line_end = line_start
        self.start = start
        self.end = end
        self.line_start = line_start
        self.line_end = line_end
        self.path = path
        self.source = source
        self.msg = msg
    
    @staticmethod
    def from_node(path: PathLike, tree: Tree, node: Node, msg=""):
        start = node.start_byte
        end = node.end_byte
        line_start = node.start_point.row
        line_end = node.end_point.row
        source = tree.root_node.text

        return Location(path, source, start, end, line_start, line_end, msg=msg)

    def _line_offset(self, line: int) -> (int, int):
        new_lines = [m.start() for m in re.finditer(b'\\n', self.source)]
        logger.debug('%s lines..', new_lines)
        if line == 0:
            return (0, new_lines[0])

        line = line - 1

        if line >= len(new_lines):
            raise Exception(f'Line {line} doesn\'t exist in {self.path}?')

        elif line == len(new_lines) - 1:
            return (new_lines[-1] + 1, len(self.source))

        return (new_lines[line] + 1, new_lines[line + 1])

    def __str__(self) -> str:
        start_offset, _ = self._line_offset(self.line_start)
        _, end_offset = self._line_offset(self.line_end)

        start = self.start - start_offset
        end = self.end - start_offset

        lines = self.source[start_offset:end_offset].decode()
        lines = f'{lines[:start]}{colored(lines[start:end], 'red', attrs=['bold', 'underline'])}{lines[end:]}'
        clean_lines = "\n\t".join(lines.splitlines())

        return f'{self.path}:{self.line_start}:{self.start}:\n\t{clean_lines}\t{colored(f'({self.msg})', attrs=['bold'])}'

@dataclass
class Error:
    locations: List[Location]
    type: ErrorType
    msg: str

    def __init__(self, locations: List[Location], type=ErrorType.UnkownError, msg=""):
        logger.debug('Error created with %s', locations)
        self.locations = locations
        self.type = type
        self.msg = msg

    def __str__(self) -> str:
        ret = f'{colored(self.type.name, 'red', attrs=['bold', 'underline'])}'
        for location in self.locations:
            ret += f' in {str(location)}'

        if self.msg:
            ret += f'\n\n{colored(self.msg, attrs=['bold'])}'

        return ret

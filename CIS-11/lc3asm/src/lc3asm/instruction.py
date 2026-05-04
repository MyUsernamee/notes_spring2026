from dataclasses import dataclass
from enum import Enum, auto

from lc3asm import logger
logger = logger.getChild('instruction')

class OpCode(Enum):
    ADD  = 0b0001
    AND  = 0b0101
    BR   = 0b0000
    JMP  = 0b1100
    JSR  = 0b0100
    LD   = 0b0010
    LDI  = 0b1010
    LEA  = 0b1110
    NOT  = 0b1001
    RET  = 0b1100
    RTI  = 0b1000
    ST   = 0b0011
    STI  = 0b1011
    STR  = 0b0111
    TRAP = 0b1111

class OperandType(Enum):
    REGISTER = auto()
    ADDRESS = auto()
    IMMEDIATE = auto()

@dataclass
class Operand:
    type: OperandType
    data: int

    def __str__(self):
        return f'({self.type.name}){self.data}'

@dataclass
class Instruction:
    opcode: OpCode    
    operands: (Operand | None, Operand | None, Operand | None)

    def __str__(self):
        ret = f'{self.opcode.name} '
        ret += ", ".join(self.opeands)
        return ret

def encode(instruction: Instruction) -> (bytes, int):
    logger.debug('Encoding %s...', instruction)
    ret = bytes(instruction.opcode)[0]
    
    logger.debug('Encoded %s as %s', instruction.opcode.name, ret)

from enum import Enum
from dataclasses import dataclass
from typing import List, Union


class TokenType(Enum):
    NUMBER = "num"
    STRING = "str"
    BOOL = "bool"
    DICT = "dict"
    LIST = "list"
    ADDRESS = "addr"
    WORD = "word"
    OPERATOR = "op"
    UNKNOWN = "unknown"


@dataclass
class Token:
    type: TokenType
    value: str


@dataclass
class MessageAST:
    tokens: List[Token]

from dataclasses import dataclass
from enum import Enum

class TokenType(str, Enum):
    SELECT = "SELECT"
    FROM = "FROM"
    WHERE = "WHERE"
    IDENT = "IDENT"
    NUMBER = "NUMBER"
    STRING = "STRING"
    SHOW = "SHOW"
    DESCRIBE = "DESCRIBE"
    LPAREN = "("
    RPAREN = ")"
    EQ = "="
    LT = "<"
    GT = ">"
    NEQ = "!="
    LTE = "<="
    GTE = ">="
    IN = "IN"
    LIKE = "LIKE"
    STAR = "*"
    LBRACK = "["
    RBRACK = "]"
    COMMA = ","
    PERCENT = "%"        # %
    QUESTION = "?"      # ?   (or UNDERSCORE if you go SQL style)
    DASH = "-"          # -
    CARET = "^"         # ^   (only if you support negation in charclass)
    LITERAL = "LITERAL"       # a, b, c, 1, ., etc.
    ESCAPE = "\\"        # \   (if you support escaping)

    EOF = "EOF"

@dataclass
class Token:
    type: str
    value: str
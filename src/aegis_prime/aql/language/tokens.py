
from dataclasses import dataclass
from enum import Enum

class TokenType(str, Enum):
    AS = "AS"
    ASC = "ASC"
    AND = "AND"
    BETWEEN = "BETWEEN"
    BY = "BY"
    CONTAINS = "CONTAINS"
    DESC = "DESC"
    DESCRIBE = "DESCRIBE"
    ENDSWITH = "ENDSWITH"
    EOF = "EOF"
    FROM = "FROM"
    GROUP = "GROUP"
    HAVING = "HAVING"
    IDENT = "IDENT"
    IN = "IN"
    LIKE = "LIKE"
    LIMIT = "LIMIT"
    LITERAL = "LITERAL"       # a, b, c, 1, ., etc.
    NOT = "NOT"
    NUMBER = "NUMBER"
    OR = "OR"
    ORDER = "ORDER"
    SELECT = "SELECT"
    SHOW = "SHOW"
    STARTSWITH = "STARTSWITH"
    STRING = "STRING"
    WHERE = "WHERE"
    LPAREN = "("
    RPAREN = ")"
    EQ = "="
    LT = "<"
    GT = ">"
    NEQ = "!="
    LTE = "<="
    GTE = ">="
    MATCH = "~="
    STAR = "*"
    LBRACK = "["
    RBRACK = "]"
    COMMA = ","
    PERCENT = "%"        # %
    QUESTION = "?"      # ?   (or UNDERSCORE if you go SQL style)
    DASH = "-"          # -
    CARET = "^"         # ^   (only if you support negation in charclass)
    ESCAPE = "\\"        # \   (if you support escaping)

@dataclass
class Token:
    type: str
    value: str
# aql_core/language/keywords.py

from .tokens import TokenType

KEYWORDS = {
    "SELECT": TokenType.SELECT,
    "FROM": TokenType.FROM,
    "WHERE": TokenType.WHERE,
    "IN": TokenType.IN,
    "LIKE": TokenType.LIKE,
    "SHOW": TokenType.SHOW,
    "DESCRIBE": TokenType.DESCRIBE,
}
# aql_core/language/keywords.py

from .tokens import TokenType

KEYWORDS = {
    "AND": TokenType.AND,
    "AS": TokenType.AS,
    "ASC": TokenType.ASC,
    "BETWEEN": TokenType.BETWEEN,
    "BY": TokenType.BY,
    "CONTAINS": TokenType.CONTAINS,
    "DESC": TokenType.DESC,
    "DESCRIBE": TokenType.DESCRIBE,
    "ENDSWITH": TokenType.ENDSWITH,
    "FROM": TokenType.FROM,
    "GROUP": TokenType.GROUP,
    "HAVING": TokenType.HAVING,
    "IN": TokenType.IN,
    "LIKE": TokenType.LIKE,
    "LIMIT": TokenType.LIMIT,
    "NOT": TokenType.NOT,
    "OR": TokenType.OR,
    "ORDER": TokenType.ORDER,
    "SELECT": TokenType.SELECT,
    "SHOW": TokenType.SHOW,
    "STARTSWITH": TokenType.STARTSWITH,
    "WHERE": TokenType.WHERE,
}
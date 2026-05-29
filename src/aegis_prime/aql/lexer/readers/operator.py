# aegis_prime.aql/lexer/readers/operator.py

from aegis_prime.aql.language.tokens import Token, TokenType
from .base import TokenReader
from ..registry import register_readers

@register_readers
class OperatorReader(TokenReader):
    OPERATORS = {
        "=": TokenType.EQ,
        "<": TokenType.LT,
        ">": TokenType.GT,
        "[": TokenType.LBRACK,
        "]": TokenType.RBRACK,
        ",": TokenType.COMMA,
        "(": TokenType.LPAREN,
        ")": TokenType.RPAREN,
    }

    def can_read(self, ch: str) -> bool:
        return ch in self.OPERATORS

    def read(self, lexer):
        ch = lexer.current
        lexer.advance()
        return Token(self.OPERATORS[ch], ch)
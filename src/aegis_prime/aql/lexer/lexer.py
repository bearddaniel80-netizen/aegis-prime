from aegis_prime.aql.language.tokens import Token, TokenType
from .registry import READER_REGISTRY
from . import readers

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.i = 0
        self.current = text[0] if text else None
        self.readers = [cls() for cls in READER_REGISTRY]

    def advance(self):
        self.i += 1
        self.current = self.text[self.i] if self.i < len(self.text) else None

    def skip_whitespace(self):
        while self.current and self.current.isspace():
            self.advance()

    def next_token(self):
        self.skip_whitespace()

        if not self.current:
            return Token(TokenType.EOF, "EOF")

        for reader in self.readers:
            if reader.can_read(self.current):
                return reader.read(self)

        raise SyntaxError(f"Unknown character: {self.current}")

    def tokenize(self):
        tokens = []
        # print("tokenize: " + ', '.join(cls.__name__ for cls in READER_REGISTRY))

        while True:
            tok = self.next_token()
            tokens.append(tok)
            if tok.type == TokenType.EOF:
                break

        return tokens
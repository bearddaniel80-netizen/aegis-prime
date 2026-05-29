class ParserContext:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def check(self, token_type):
        return self.peek().type == token_type
        
    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self):
        tok = self.peek()
        self.pos += 1
        return tok

    def match(self, token_type):
        tok = self.peek()
        if tok and tok.type == token_type:
            return self.consume()
        return None

    def expect(self, token_type):
        tok = self.consume()
        if not tok or tok.type != token_type:
            raise SyntaxError(f"Expected {token_type}, got {tok}")
        return tok
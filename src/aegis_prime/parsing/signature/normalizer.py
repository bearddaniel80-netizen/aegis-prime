from aegis_prime.parsing.signature.ir import MessageAST, TokenType

class Normalizer:

    ALLOWED = {
        TokenType.NUMBER: "<num>",
        TokenType.STRING: "<str>",
        TokenType.BOOL: "<bool>",
        TokenType.DICT: "<dict>",
        TokenType.LIST: "<list>",
        TokenType.OPERATOR: "<op>",
        TokenType.ADDRESS: "<addr>",
    }

    def normalize(self, ast: MessageAST) -> str:
        output = []

        for token in ast.tokens:
            if token.type in self.ALLOWED:
                output.append(self.ALLOWED[token.type])

        return " ".join(output)
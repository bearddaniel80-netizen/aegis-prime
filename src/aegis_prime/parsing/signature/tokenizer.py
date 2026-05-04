import ast
from aegis_prime.parsing.signature.ir import Token, TokenType, MessageAST

class Tokenizer:

    def tokenize(self, msg: str) -> MessageAST:
        tokens: List[Token] = []
        i = 0
        n = len(msg)

        while i < n:
            ch = msg[i]

            # Skip whitespace
            if ch.isspace():
                i += 1
                continue

            # Number
            if ch.isdigit():
                start = i
                while i < n and msg[i].isdigit():
                    i += 1
                tokens.append(Token(TokenType.NUMBER, msg[start:i]))
                continue

            # Boolean
            if msg.startswith("True", i):
                tokens.append(Token(TokenType.BOOL, "True"))
                i += 4
                continue

            if msg.startswith("False", i):
                tokens.append(Token(TokenType.BOOL, "False"))
                i += 5
                continue

            # String
            if ch in ("'", '"'):
                quote = ch
                start = i
                i += 1
                while i < n and msg[i] != quote:
                    i += 1
                i += 1  # consume closing
                tokens.append(Token(TokenType.STRING, msg[start:i]))
                continue

            # Operators
            OPERATORS = ["==", "!=", "<", ">"]

            for op in OPERATORS:
                if msg.startswith(op, i):
                    tokens.append(Token(TokenType.OPERATOR, op))
                    i += len(op)
                    break
                # continue

            # Address (0x...)
            if msg.startswith("0x", i):
                start = i
                i += 2
                while i < n and msg[i] in "0123456789abcdefABCDEF":
                    i += 1
                tokens.append(Token(TokenType.ADDRESS, msg[start:i]))
                continue

            # Dict / List (use Python parser instead of regex)
            if ch in "{[":
                start = i
                try:
                    node = ast.literal_eval(msg[i:])
                    literal_str = repr(node)
                    i += len(literal_str)

                    if isinstance(node, dict):
                        tokens.append(Token(TokenType.DICT, literal_str))
                    elif isinstance(node, list):
                        tokens.append(Token(TokenType.LIST, literal_str))
                    continue
                except Exception:
                    pass  # fallback to word parsing

            # Word
            start = i
            while i < n and not msg[i].isspace():
                i += 1
            tokens.append(Token(TokenType.WORD, msg[start:i]))

        return MessageAST(tokens)
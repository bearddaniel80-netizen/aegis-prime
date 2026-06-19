from aegis_prime.aql.language.tokens import TokenType
from aegis_prime.aql.language.ast.identifier import Identifier
from aegis_prime.aql.language.ast.expressions.literals import ListLiteral, Literal
from aegis_prime.aql.language.ast.expressions.operators import BinaryOp, InOp

class ExpressionParser:
    PRECEDENCE = {
        "=": 10,
        "<": 10,
        ">": 10,
        "!=": 10,
        "<=": 10,
        ">=": 10,
        "IN": 20,
    }

    def parse(self, ctx, precedence=0):
        left = self.parse_primary(ctx)

        while True:
            tok = ctx.peek()
            if not tok:
                break

            if tok.type == TokenType.IN:
                op = "IN"
            elif tok.type in (TokenType.EQ, TokenType.LT, TokenType.GT, TokenType.NEQ, TokenType.LTE, TokenType.GTE):
                op = tok.value
            else:
                break

            prec = self.PRECEDENCE.get(op, -1)
            if prec < precedence:
                break

            ctx.consume()

            if tok.type == TokenType.IN:
                left = self.parse_in(ctx, left)
            else:
                right = self.parse(ctx, prec + 1)
                left = BinaryOp(left, op, right)

        return left

    def parse_primary(self, ctx):
        tok = ctx.consume()

        if tok.type == TokenType.IDENT:
            return Identifier(tok.value)

        if tok.type == TokenType.NUMBER:
            return Literal(int(tok.value))

        if tok.type == TokenType.STRING:
            return Literal(tok.value)

        raise SyntaxError(f"Unexpected token: {tok}")

    def parse_in(self, ctx, left):
        ctx.expect(TokenType.LBRACK)

        values = []
        while True:
            values.append(self.parse_primary(ctx))
            if not ctx.match(TokenType.COMMA):
                break

        ctx.expect(TokenType.RBRACK)

        return InOp(left, values)

    def parse_compond_operators(self, ctx):
        pass
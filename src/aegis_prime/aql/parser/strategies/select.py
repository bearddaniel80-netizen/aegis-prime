from .base import StatementStrategy
from aegis_prime.aql.language.tokens import TokenType
from aegis_prime.aql.language.ast.statements.query import Query
from aegis_prime.aql.language.ast.function_call import TableFunctionCall
from aegis_prime.aql.language.ast.identifier import Identifier
from aegis_prime.aql.language.ast.expressions.literals import Literal
from aegis_prime.aql.parser.expressions.parser import ExpressionParser

class SelectStrategy(StatementStrategy):
    def can_handle(self, ctx):
        tok = ctx.peek()
        return tok and tok.type == TokenType.SELECT

    def parse(self, ctx):
        ctx.expect(TokenType.SELECT)

        select = self.parse_fields(ctx)

        ctx.expect(TokenType.FROM)
        source = self.parse_from(ctx)

        where = None
        if ctx.match(TokenType.WHERE):
            where = ExpressionParser().parse(ctx)

        return Query(select, source, where)

    def parse_fields(self, ctx):
        fields = []

        while True:
            token = ctx.consume()

            if ctx.match(TokenType.STAR):
                fields.append(Identifier("*"))
            else:
                fields.append(Identifier(token.value))

            if not ctx.match(TokenType.COMMA):
                break

        return fields

    def parse_from(self, ctx):
        ident = ctx.expect(TokenType.IDENT)

        # function call
        if ctx.match(TokenType.LPAREN):
            arg = None

            while ctx.peek().type != TokenType.RPAREN:
                arg = ExpressionParser().parse(ctx)

            ctx.expect(TokenType.RPAREN)

            return TableFunctionCall(
                name=ident.value,
                arg=arg
            )

        # regular table name
        return Identifier(ident.value)
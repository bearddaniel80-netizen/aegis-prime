from .base import StatementStrategy
from aegis_prime.aql.language.tokens import TokenType
from aegis_prime.aql.language.ast.statements.show import Show
from aegis_prime.aql.link.registry import FUNCTION_CALL_REGISTRY
from aegis_prime.aql.link import fn_call
from .select import SelectStrategy

class ShowStrategy(StatementStrategy):
    def can_handle(self, ctx):
        tok = ctx.peek()
        return tok and tok.type == TokenType.SHOW

    def parse(self, ctx):
        ctx.expect(TokenType.SHOW)
        target = ctx.peek()
        if target.value in FUNCTION_CALL_REGISTRY.keys():
            select = SelectStrategy()
            target = select.parse_from(ctx)
        else:
            target = ctx.expect(TokenType.IDENT).value
        return Show(target)
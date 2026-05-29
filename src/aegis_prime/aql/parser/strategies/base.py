from aegis_prime.aql.parser.context import ParserContext

class StatementStrategy:
    def can_handle(self, ctx: ParserContext) -> bool:
        raise NotImplementedError

    def parse(self, ctx: ParserContext):
        raise NotImplementedError
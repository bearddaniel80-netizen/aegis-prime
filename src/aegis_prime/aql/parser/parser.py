from .context import ParserContext
from aegis_prime.aql.parser.strategies.select import SelectStrategy
from aegis_prime.aql.parser.strategies.show import ShowStrategy
from aegis_prime.aql.parser.strategies.describe import DescribeStrategy

class Parser:
    def __init__(self, tokens):
        self.ctx = ParserContext(tokens)

        self.strategies = [
            SelectStrategy(),
            ShowStrategy(),
            DescribeStrategy(),
        ]

    def parse(self):
        if not self.ctx.peek():
            raise SyntaxError("Empty query")

        for strategy in self.strategies:
            if strategy.can_handle(self.ctx):
                return strategy.parse(self.ctx)

        raise SyntaxError(f"Unknown statement: {self.ctx.peek()}")
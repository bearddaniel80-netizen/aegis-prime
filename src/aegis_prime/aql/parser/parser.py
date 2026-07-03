from .context import ParserContext
from .strategies.select import SelectStrategy
from .strategies.show import ShowStrategy
from .strategies.describe import DescribeStrategy
from ..context.analysis import AnalysisContext

class Parser:
    def __init__(self, analysis_ctx: AnalysisContext):
        self.ctx = ParserContext(analysis_ctx)
        self.analysis_ctx = analysis_ctx
        self.strategies = [
            SelectStrategy(),
            ShowStrategy(),
            DescribeStrategy(),
        ]

    def parse(self):
        if not self.ctx.peek():
            analysis_ctx.artifacts["diagnostic"].fatal("PP01", f"Empty query", "Fix query")
            return


        for strategy in self.strategies:
            if strategy.can_handle(self.ctx):
                self.analysis_ctx.artifacts["ast"] = strategy.parse(self.ctx, self.analysis_ctx)
                return

        analysis_ctx.artifacts["diagnostic"].warning("PP02", f"Unknown statement: {self.ctx.peek()}", "Fix statement")
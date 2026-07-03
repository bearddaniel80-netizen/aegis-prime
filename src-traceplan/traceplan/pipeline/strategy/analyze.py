from .base import Strategy
from ..registry import strategy

@strategy(
    "analyze",
    aliases=["inspect"],
    description="Analyze a graph node",
    capabilities=["graph"]
)
class AnalyzeStrategy(Strategy):

    def execute(
        self,
        context
    ):
        pass
from .base import Strategy
from ..registry import strategy

@strategy(
    "compatibility",
    description="Analyze API compatibility",
    capabilities=[
        "snapshot",
        "diff",
        "graph"
    ]
)
class CompatibilityStrategy(Strategy):

    def execute(
        self,
        context
    ):
        pass
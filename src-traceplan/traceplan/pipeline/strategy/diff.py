from .base import Strategy
from ..registry import strategy

@strategy(
    "diff",
    description="Compare two snapshots",
    capabilities=["snapshot"]
)
class DiffStrategy(Strategy):

    def execute(
        self,
        context
    ):
        pass
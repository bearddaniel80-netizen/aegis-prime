from .base import Strategy
from ..registry import strategy
from ..context import PipelineContext
from ...graph.build import GraphBuilder
from ...reports.build import BuildReport


@strategy(
    "build",
    aliases=["graph"],
    description="Build a dependency graph from source code",
    capabilities=["source", "graph"]
)
class BuildStrategy(
    Strategy[
        PipelineContext,
        BuildReport
    ]
):

    def __init__(
        self,
        builder: GraphBuilder | None = None
    ):

        self.builder = builder or GraphBuilder()

    def execute(
        self,
        context: PipelineContext
    ) -> BuildReport:

        snapshot = self.builder.build(
            context.data
        )

        return BuildReport.from_snapshot(
            snapshot
        )
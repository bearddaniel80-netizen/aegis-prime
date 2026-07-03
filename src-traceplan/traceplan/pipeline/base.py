from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar, Any


TContext = TypeVar("TContext")
TReport = TypeVar("TReport")
TOutput = TypeVar("TOutput")


# -------------------------
# Pipeline Context
# -------------------------

@dataclass
class PipelineContext:
    """
    Shared runtime context passed through all strategies.
    """

    data: Any = None

    snapshot: Any = None

    old_snapshot: Any = None
    new_snapshot: Any = None

    node_id: str | None = None

    config: dict | None = None

class AsyncStrategy(ABC, Generic[TContext, TReport]):

    @abstractmethod
    async def execute(
        self,
        context: TContext
    ) -> TReport:
        """
        Transform context -> report model
        """
        pass

class AsyncRenderer(ABC, Generic[TReport, TOutput]):

    @abstractmethod
    async def render(
        self,
        report: TReport
    ) -> TOutput:
        """
        Transform report -> output (console/json/html/etc)
        """
        pass

class Pipeline(Generic[TContext, TReport, TOutput]):

    def __init__(
        self,
        strategy: AsyncStrategy[TContext, TReport],
        renderer: AsyncRenderer[TReport, TOutput]
    ):

        self.strategy = strategy
        self.renderer = renderer

    def run(
        self,
        context: TContext
    ) -> TOutput:

        report = await self.strategy.execute(
            context
        )

        return await self.renderer.render(
            report
        )

class Stage(ABC):

    @abstractmethod
    def process(self, data):
        pass

class StagePipeline:

    def __init__(self, stages: list[Stage]):

        self.stages = stages

    def run(self, data):

        for stage in self.stages:

            data = stage.process(data)

        return data
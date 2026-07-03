from dataclasses import dataclass, field
from time import time
from typing import Generic, Any

from .base import (
    PipelineContext,
    AsyncStrategy,
    AsyncRenderer
)

@dataclass
class PipelineResult:

    output: Any

    duration_ms: float

    success: bool = True

    error: str | None = None

    metadata: dict = field(
        default_factory=dict
    )

class Pipeline(
    Generic[PipelineContext, Any, Any]
):

    def __init__(
        self,
        strategy: AsyncStrategy,
        renderer: AsyncRenderer,
        enable_timing: bool = True,
        metadata: dict | None = None
    ):

        self.strategy = strategy
        self.renderer = renderer

        self.enable_timing = enable_timing

        self.metadata = metadata or {}

    def run(
        self,
        context: PipelineContext
    ) -> PipelineResult:

        start = time()

        try:

            # -------------------------
            # Strategy execution
            # -------------------------

            report = self.strategy.execute(
                context
            )

            # -------------------------
            # Render output
            # -------------------------

            output = self.renderer.render(
                report
            )

            duration = (
                (time() - start) * 1000
            )

            return PipelineResult(
                output=output,

                duration_ms=duration,

                success=True,

                metadata={
                    **self.metadata,
                    "strategy": self.strategy.__class__.__name__,
                    "renderer": self.renderer.__class__.__name__
                }
            )

        except Exception as e:

            duration = (
                (time() - start) * 1000
            )

            return PipelineResult(
                output=None,

                duration_ms=duration,

                success=False,

                error=str(e),

                metadata={
                    **self.metadata,
                    "strategy": self.strategy.__class__.__name__,
                    "renderer": self.renderer.__class__.__name__
                }
            )

    def safe_run(
        self,
        context: PipelineContext
    ) -> Any:

        result = self.run(context)

        if not result.success:

            print(
                f"[Pipeline Error] {result.error}"
            )

            return None

        return result.output

    def debug_run(
        self,
        context: PipelineContext
    ) -> PipelineResult:

        result = self.run(context)

        print(
            f"[Pipeline] "
            f"{self.strategy.__class__.__name__} "
            f"-> {self.renderer.__class__.__name__} "
            f"({result.duration_ms:.2f}ms)"
        )

        return result
from .pipeline import Pipeline
from .registry import get

class PipelineFactory:

    @staticmethod
    def create(
        command: str,
        _format
    ):

        strategy_cls, renderer_cls = get(
            command, _format
        )

        return Pipeline(
            strategy=strategy_cls(),
            renderer=renderer_cls()
        )
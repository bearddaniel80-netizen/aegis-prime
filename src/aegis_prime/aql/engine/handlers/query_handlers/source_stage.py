from .base import Stage
from ..query_exec_context import ExecutionContext

class SourceStage(Stage):

    def execute(self, context: ExecutionContext):

        if context.query.source == "stdin":
            data, model_cls = context.engine_context.source_resolver.resolve(context.query.source)
        else:
            data = context.engine_context.source_resolver.resolve(context.query.source)

        if data is None:
            raise ValueError(f"Unknown source: {context.query.source}")

        context.rows = data

        return context
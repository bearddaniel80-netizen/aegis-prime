from .base import Stage
from ..query_exec_context import ExecutionContext

class TransformStage(Stage):
    def __init__(self, transforms):
        self.transforms = transforms

    def execute(self, context: ExecutionContext):
        for t in self.transforms:
            result = t.evaluate(row)

            # merge structured output
            if isinstance(result, dict):
                row.update(result)

        return context

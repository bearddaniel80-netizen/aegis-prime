from .base import ExecutionPlan
from ...models import ExecutionResult

class VirtualExecutionPlan(
    ExecutionPlan
):

    def execute(
        self,
        query: str,
    ) -> ExecutionResult:

        command = (
            f'aegis query "{query}"'
        )

        return self._run(command)
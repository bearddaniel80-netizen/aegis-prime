from .base import AggregateFunction
from ..registry import register_function_call

@register_function_call("SUM")
class SumFunction(AggregateFunction):

    def __init__(self):
        self.kind = "aggregate"
        self.total = 0

    def step(self, value):
        self.total += int(value)

    def finalize(self):
        return self.total
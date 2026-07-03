from .base import AggregateFunction
from ..registry import register_function_call

@register_function_call("MAX")
class MaxFunction(AggregateFunction):

    def __init__(self):
        self.kind = "aggregate"
        self._max = 0

    def step(self, value):
        if self._max < int(value):
            self._max = int(value)

    def finalize(self):
        return self._max
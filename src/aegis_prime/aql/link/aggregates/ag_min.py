import math
from .base import AggregateFunction
from ..registry import register_function_call

@register_function_call("MIN")
class MaxFunction(AggregateFunction):

    def __init__(self):
        self.kind = "aggregate"
        self._min = math.inf

    def step(self, value):
        if self._min > int(value):
            self._min = int(value)

    def finalize(self):
        return self._min
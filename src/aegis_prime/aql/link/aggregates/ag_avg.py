import numpy as np
from .base import AggregateFunction
from ..registry import register_function_call

@register_function_call("AVG")
class AverageFunction(AggregateFunction):

    def __init__(self):
        self.kind = "aggregate"
        self.values = []

    def step(self, value):
        self.values.append(value)

    def finalize(self):
        return np.average(self.values)
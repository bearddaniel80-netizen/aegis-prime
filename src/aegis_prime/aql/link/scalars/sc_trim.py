from .base import ScalarFunction
from ..registry import register_function_call

@register_function_call("TRIM")
class TrimFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return value.strip()
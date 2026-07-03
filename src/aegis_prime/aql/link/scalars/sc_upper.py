from .base import ScalarFunction
from ..registry import register_function_call

@register_function_call("UPPER")
class UpperFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return value.upper()
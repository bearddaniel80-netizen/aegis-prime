from .base import ScalarFunction
from ..registry import register_function_call

@register_function_call("CAPITALIZE")
class CapitalizeFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return value.capitalize()
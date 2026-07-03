from .base import ScalarFunction
from ..registry import register_function_call

@register_function_call("IS_LOWER")
class IsLowerFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return value.islower()
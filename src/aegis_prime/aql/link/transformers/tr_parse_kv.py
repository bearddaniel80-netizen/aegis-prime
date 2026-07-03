import re
from .base import TransformFunction
from ..registry import register_function_call

@register_function_call("PARSE_KV")
class ParseKVFunction(TransformFunction):

    def __init__(self):
        self.kind = "transform"

    def evaluate(self, row, field: str, pattern: list):
        line = row[field]

        p = "|".join(pattern)

        parts = re.split(p, line)

        data = {}
        i = 0
        while i < len(parts) - 1:
            key = parts[i]
            value = parts[i + 1]
            data[key] = value
            i += 2

        return data
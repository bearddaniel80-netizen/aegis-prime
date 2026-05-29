from ..registry import register_function_call
from aegis_prime.aql.adapter.source.arrow_source import ArrowSource

@register_function_call("arrow")
class ArrowTableFunction:

    def execute(self, *args):
        path = args[0]

        source = ArrowSource.from_file(path)

        return source.to_dataset()
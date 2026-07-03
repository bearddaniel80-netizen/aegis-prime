from ..registry import register_function_call
from aegis_prime.aql.adapter.source.binary_source import BinarySource

@register_function_call("binary")
class BinaryTableFunction:

    def execute(self, *args):
        path = args[0]

        source = BinarySource.from_file(path)

        return source.to_dataset()
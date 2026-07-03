from ..registry import register_function_call
from aegis_prime.aql.adapter.source.zip_source import ZipSource

@register_function_call("zip")
class ZipTableFunction:

    def execute(self, *args):
        path = args[0]

        source = ZipSource.from_file(path)

        return source.to_dataset()
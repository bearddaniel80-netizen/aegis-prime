from ..registry import register_function_call
from aegis_prime.aql.adapter.source.sevenzip_source import SevenZipSource

@register_function_call("7z")
class SevenZipTableFunction:

    def execute(self, *args):
        path = args[0]

        source = SevenZipSource.from_file(path)

        return source.to_dataset()
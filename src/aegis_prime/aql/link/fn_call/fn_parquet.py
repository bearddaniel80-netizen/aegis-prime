from ..registry import register_function_call
from aegis_prime.aql.adapter.source.parquet_source import ParquetSource

@register_function_call("parquet")
class ParquetTableFunction:

    def execute(self, *args):
        path = args[0]

        source = ParquetSource.from_file(path)

        return source.to_dataset()
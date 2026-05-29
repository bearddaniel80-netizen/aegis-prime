from ..registry import register_function_call
from aegis_prime.aql.adapter.source.csv_source import CsvSource

@register_function_call("csv")
class CsvTableFunction:

    def execute(self, *args):
        path = args[0]

        source = CsvSource.from_file(path)

        return source.to_dataset()
from ..registry import register_function_call
from aegis_prime.aql.adapter.source.json_source import JsonFileSource

@register_function_call("json")
class JsonTableFunction:

    def execute(self, *args):
        path = args[0]

        source = JsonFileSource.from_file(path)

        return source.to_dataset()
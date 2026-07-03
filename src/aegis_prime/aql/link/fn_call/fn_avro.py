from ..registry import register_function_call
from aegis_prime.aql.adapter.source.avro_source import AvroSource

@register_function_call("avro")
class AvroTableFunction:

    def execute(self, *args):
        path = args[0]

        source = AvroSource.from_file(path)

        return source.to_dataset()
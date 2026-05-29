from ..registry import register_function_call
from aegis_prime.aql.adapter.source.protobuf_source import ProtobufSource

@register_function_call("protobuf")
class ProtobufTableFunction:

    def execute(self, *args):
        path = args[0]

        source = ProtobufSource.from_file(path)

        return source.to_dataset()
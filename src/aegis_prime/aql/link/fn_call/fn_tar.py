from ..registry import register_function_call
from aegis_prime.aql.adapter.source.tar_source import TarSource

@register_function_call("tar")
class TarTableFunction:

    def execute(self, *args):
        path = args[0]

        source = TarSource.from_file(path)

        return source.to_dataset()
from ..registry import register_function_call
from aegis_prime.aql.adapter.source.mbox_source import MboxSource

@register_function_call("mbox")
class MboxTableFunction:

    def execute(self, *args):
        path = args[0]

        source = MboxSource.from_file(path)

        return source.to_dataset()
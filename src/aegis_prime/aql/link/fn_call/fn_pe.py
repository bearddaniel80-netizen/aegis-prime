from ..registry import register_function_call
from aegis_prime.aql.adapter.source.pe_bin_source import PESource

@register_function_call("pe")
class PeTableFunction:

    def execute(self, *args):
        path = args[0]

        source = PESource.from_file(path)

        return source.to_dataset()
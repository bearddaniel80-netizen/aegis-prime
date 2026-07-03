from ..registry import register_function_call
from aegis_prime.aql.adapter.source.elf_bin_source import ELFSource

@register_function_call("elf")
class ElfTableFunction:

    def execute(self, *args):
        path = args[0]

        source = ELFSource.from_file(path)

        return source.to_dataset()
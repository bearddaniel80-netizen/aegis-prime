from ..registry import register_function_call
from aegis_prime.aql.adapter.source.elf_bin_source import ELFImportsSource

@register_function_call("elf_imports")
class ElfImportsTableFunction:

    def execute(self, *args):
        path = args[0]

        source = ELFImportsSource.from_file(path)

        return source.to_dataset()
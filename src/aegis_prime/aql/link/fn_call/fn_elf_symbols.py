from ..registry import register_function_call
from aegis_prime.aql.adapter.source.elf_bin_source import ELFSymbolsSource

@register_function_call("elf_symbols")
class ElfSymbolsTableFunction:

    def execute(self, *args):
        path = args[0]

        source = ELFSymbolsSource.from_file(path)

        return source.to_dataset()
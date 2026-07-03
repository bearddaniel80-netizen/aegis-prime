from ..registry import register_function_call
from aegis_prime.aql.adapter.source.pcap_source import PcapSource

@register_function_call("pcap")
class PcapTableFunction:

    def execute(self, *args):
        path = args[0]

        source = PcapSource.from_file(path)

        return source.to_dataset()
from ..registry import register_function_call
from aegis_prime.aql.adapter.source.xml_source import XmlSource

@register_function_call("xml")
class XmlTableFunction:

    def execute(self, *args):
        path = args[0]

        source = XmlSource.from_file(path)

        return source.to_dataset()
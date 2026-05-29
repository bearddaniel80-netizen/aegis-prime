from ..registry import register_function_call
from aegis_prime.aql.adapter.source.yml_source import YamlSource

@register_function_call("yaml")
class YamlTableFunction:

    def execute(self, *args):
        path = args[0]

        source = YamlSource.from_file(path)

        return source.to_dataset()
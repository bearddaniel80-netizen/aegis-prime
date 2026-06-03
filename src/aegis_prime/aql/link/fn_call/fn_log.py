from ..registry import register_function_call
from aegis_prime.aql.adapter.source.log_stdin import LogStdinSource

@register_function_call("log")
class LogTableFunction:

    def execute(self, *args):
        path = args[0]

        source = LogStdinSource.from_file(path)

        return source.to_dataset()
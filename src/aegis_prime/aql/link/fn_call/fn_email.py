from ..registry import register_function_call
from aegis_prime.aql.adapter.source.email_source import EmailSource

@register_function_call("email")
class EmailTableFunction:

    def execute(self, *args):
        path = args[0]

        source = EmailSource.from_file(path)

        return source.to_dataset()
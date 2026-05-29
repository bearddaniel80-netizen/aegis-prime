from ..registry import register_function_call
from aegis_prime.aql.adapter.source.maildir_source import MaildirSource

@register_function_call("maildir")
class MaildirTableFunction:

    def execute(self, *args):
        path = args[0]

        source = MaildirSource.from_dir(path)

        return source.to_dataset()
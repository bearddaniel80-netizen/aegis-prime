from ..registry import register_function_call
from aegis_prime.aql.adapter.source.sqlite_source import SQLiteSource

@register_function_call("sqlite")
class SqliteTableFunction:

    def execute(self, *args):
        db = args[0].value
        query = args[1].value

        source = SQLiteSource.from_query(
            db,
            query
        )

        return source.to_dataset()
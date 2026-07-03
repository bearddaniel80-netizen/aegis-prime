from .base import Stage
from ....language.ast.identifier import Identifier
from ....language.ast.function_call import FunctionCall
from ....link import scalars
from ....link.registry import FUNCTION_CALL_REGISTRY

class ProjectStage(Stage):

    def execute(self, context):

        query = context.query

        context.rows = (
            self.project_row(query.select, row)
            for row in context.rows
        )

        return context

    def project_row(self, fields, row):

        if not fields:
            return row

        if self.is_star(fields):
            return row

        result = {}

        for field in fields:

            if isinstance(field, Identifier):

                key = field.alias or field.name

                result[key] = row.get(field.name)

            elif isinstance(field, FunctionCall):

                fn_cls = FUNCTION_CALL_REGISTRY.get(
                    field.name
                )

                fn = fn_cls()

                args = [
                    row.get(arg.name)
                    for arg in field.arg
                ]

                key = field.alias or field.name

                result[key] = fn.evaluate(*args)

        return result

    def is_star(self, fields):

        return (
            len(fields) == 1 and
            getattr(fields[0], "name", None) == "*"
        )
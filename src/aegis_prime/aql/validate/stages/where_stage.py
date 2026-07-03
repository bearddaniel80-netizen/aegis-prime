from .base import ValidationStage
from ..rules.aggregate import contains_aggregate

class WhereStage(ValidationStage):

    def execute(self, context):

        where = context.query.where

        if where is None:
            return context

        if contains_aggregate(where):

            context.diagnostics.error(
                code="AQ1201",
                message="Aggregate functions are not allowed in WHERE.",
                hint="Use HAVING instead."
            )

        return context
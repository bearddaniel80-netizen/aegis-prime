from .base import ValidationStage
from ..rules.aggregate import contains_aggregate

class GroupByStage(ValidationStage):

    def execute(self, context):

        query = context.query

        if (
            context.analyzer.has_aggregate(query)
            and
            context.analyzer.has_non_aggregate(query)
            and
            query.group_by is None
        ):

            context.diagnostics.error(
                code="AQ1301",
                message="Mixing aggregate and non-aggregate fields requires GROUP BY."
            )

        return context
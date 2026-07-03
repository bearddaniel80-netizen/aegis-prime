from ..base import ValidationStage
from ..rules.aggregate import contains_aggregate
from ..rules.identifiers import validate_expression_identifiers


class HavingStage(ValidationStage):

    def execute(self, context):

        having = context.query.having

        if having is None:
            return context

        #
        # HAVING requires GROUP BY
        #
        if context.query.group_by is None:

            context.diagnostics.error(
                code="AQ1501",
                message="HAVING requires GROUP BY."
            )

        #
        # Validate identifiers
        #
        validate_expression_identifiers(
            having,
            context
        )

        #
        # HAVING should reference an aggregate.
        #
        if not contains_aggregate(having):

            context.diagnostics.warning(
                code="AQ1502",
                message="HAVING expression contains no aggregate function.",
                hint="Consider moving this condition to WHERE."
            )

        return context
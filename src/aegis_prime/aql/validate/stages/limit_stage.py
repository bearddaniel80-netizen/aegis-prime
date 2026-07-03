from ..base import ValidationStage


class LimitStage(ValidationStage):

    def execute(self, context):

        limit = context.query.limit

        if limit is None:
            return context

        #
        # LIMIT must be an integer
        #
        if not isinstance(limit, int):

            context.diagnostics.error(
                code="AQ1701",
                message="LIMIT must be an integer."
            )

            return context

        #
        # LIMIT cannot be negative
        #
        if limit < 0:

            context.diagnostics.error(
                code="AQ1702",
                message="LIMIT cannot be negative."
            )

        #
        # Optional warning
        #
        if limit == 0:

            context.diagnostics.warning(
                code="AQ1703",
                message="LIMIT 0 returns no rows."
            )

        return context
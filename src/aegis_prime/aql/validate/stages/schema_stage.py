from ..base import ValidationStage


class SchemaStage(ValidationStage):

    def execute(self, context):

        #
        # SourceStage failed.
        #
        if context.schema is None:
            return context

        #
        # Empty schema.
        #
        if not context.schema:

            context.diagnostics.error(
                code="AQ1010",
                message="Source contains no schema."
            )

            return context

        #
        # Cache useful lookups.
        #
        context.columns = {
            column.name.lower(): column
            for column in context.schema
        }

        return context
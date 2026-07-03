from ..base import ValidationStage


class SourceStage(ValidationStage):

    def execute(self, context):

        source = context.query.source

        try:
            resolver = context.engine_context.source_resolver

            resolved = resolver.resolve(source)

        except Exception as ex:

            context.diagnostics.error(
                code="AQ1001",
                message=str(ex)
            )

            return context

        if resolved is None:

            context.diagnostics.error(
                code="AQ1002",
                message=f"Unknown source '{source.name}'."
            )

            return context

        #
        # publish artifacts
        #

        context.source = resolved
        context.schema = resolved.schema
        context.capabilities = resolved.capabilities

        return context
from ..base import ValidationStage


class FinalStage(ValidationStage):

    def execute(self, context):

        #
        # Sort diagnostics.
        #
        context.diagnostics.sort()

        #
        # Abort if any fatal errors exist.
        #
        if context.diagnostics.has_errors():

            raise ValidationException(
                context.diagnostics
            )

        return context
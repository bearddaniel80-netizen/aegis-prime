from .base import ValidationStage
from ..query_analyzer import QueryAnalyzer

from ..rules.identifiers import validate_identifier
from ..rules.functions import validate_function


class SelectStage(ValidationStage):

    def execute(self, context):

        query = context.query

        for field in query.select:

            self.validate_field(field, context)

        return context

    def validate_field(self, field, context):

        if QueryAnalyzer.is_identifier(field):
            validate_identifier(field, context)

        elif QueryAnalyzer.is_function(field):
            validate_function(field, context)

        else:
            context.diagnostics.error(
                code="AQ1100",
                message=f"Unsupported SELECT expression: {field}"
            )
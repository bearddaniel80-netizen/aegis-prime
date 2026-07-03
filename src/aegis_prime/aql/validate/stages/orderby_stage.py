from ..base import ValidationStage

from ..rules.identifiers import validate_identifier
from ..rules.functions import validate_function


class OrderByStage(ValidationStage):

    def execute(self, context):

        order_by = context.query.order_by

        if order_by is None:
            return context

        expr = order_by.expression

        #
        # ORDER BY name
        #
        if hasattr(expr, "name"):

            validate_identifier(expr, context)

        #
        # ORDER BY UPPER(name)
        #
        elif hasattr(expr, "arg"):

            validate_function(expr, context)

        return context
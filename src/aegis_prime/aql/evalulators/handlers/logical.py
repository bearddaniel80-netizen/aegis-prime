from .base import BaseHandler
from aegis_prime.aql.language.ast.expressions.operators import LogicalOp
from ..registry import register_eval_handler
from ..op_enums import LogicalOpType

@register_eval_handler(priority=40)
class LogicalOpHandler(BaseHandler):
    def can_handle(self, node):
        return isinstance(node, LogicalOp)

    def process(self, node, ctx):
        op = LogicalOpType(node.operator)

        if op == LogicalOpType.AND:
            left = ctx.eval(node.left)
            if not left:
                return False
            return ctx.eval(node.right)

        if op == LogicalOpType.OR:
            left = ctx.eval(node.left)
            if left:
                return True
            return ctx.eval(node.right)
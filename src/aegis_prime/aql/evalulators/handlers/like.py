from .base import BaseHandler
from aegis_prime.aql.language.ast.expressions.operators import LikeOp
from ..registry import register_eval_handler
from .like.optimizer import fast_match

@register_eval_handler(priority=70)
class LikeOpHandler(BaseHandler):
    def can_handle(self, node):
        return isinstance(node, LikeOp)

    def process(self, node, ctx):
        from ..like.optimizer import fast_match

        value = ctx.eval(node.left)

        if value is None:
            return False

        return fast_match(str(value), node.compiled)
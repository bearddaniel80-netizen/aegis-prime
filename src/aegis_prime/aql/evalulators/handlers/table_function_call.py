from .base import BaseHandler
from aegis_prime.aql.language.ast.function_call import TableFunctionCall
from ..registry import register_eval_handler
from aegis_prime.aql.link.registry import FUNCTION_CALL_REGISTRY
from aegis_prime.aql.link import fn_call

@register_eval_handler(priority=15)
class TableFunctionHandler(BaseHandler):

    def can_handle(self, node):
        return isinstance(node, TableFunctionCall)

    def process(self, node, ctx):
        fn_cls = FUNCTION_CALL_REGISTRY.get(node.name)

        """ This will go in the validation pipeline """
        if not fn_cls:
            raise Exception(f"Unknown table function: {node.name}")

        fn = fn_cls()

        args = [
            ctx.eval(arg)
            for arg in node.args
        ]

        return fn.execute(*args)
from .registry import HANDLER_REGISTRY
from . import handlers
from aegis_prime.aql.planner.datacls.logical import LogicalPlan


class ExecutionEngine:
    def __init__(self, engine_context, config_context):
        self.engine_context = engine_context
        self.config_context = config_context
        self.handlers = self._load_handlers()

    def _load_handlers(self):
        instances = []

        for handler_cls in HANDLER_REGISTRY:
            instances.append(handler_cls(self.engine_context))

        return instances
#    def execute(self, plan):
#        if not isinstance(plan, LogicalPlan):
#            raise ValueError(f"Expected LogicalPlan, got {type(plan)}")
#
#        data = self.engine_context.source_resolver.resolve(plan.source)
#        return [self.engine_context.projector.project(data, plan.projections)]

#    def execute(self, plan, dialect, source):
#
#        if plan.operation == "full_pushdown":
#            return source.execute(plan.pushdown)
#
#        if plan.operation == "scan_filter_local":
#            rows = source.scan()
#            return self.apply_filter(rows, plan.residual)

#     def execute(self, graph, sources, dialects)
#         results = {}
# 
#         for node in graph.nodes:
# 
#             if node.execution_target == "sql_dialect":
# 
#                 dialect = dialects[node.source]
# 
#                 sql = dialect.compile(node.pushdown)
# 
#                 results[node.id] = sources[node.source].execute(sql)
# 
#             elif node.execution_target == "mongo_pipeline":
# 
#                 results[node.id] = sources[node.source].execute(node.pushdown)
# 
#             else:
# 
#                 results[node.id] = self.execute_local(node, results)

    def execute(self, ast):
        for handler in self.handlers:
            if handler.can_handle(ast):
                return handler.handle(ast)

        raise ValueError(f"No handler for AST: {ast}")
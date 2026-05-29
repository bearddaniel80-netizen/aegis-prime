from aegis_prime.aql.language.ast.statements.query import Query
from .base import BaseHandler
from ..registry import register_handler

@register_handler
class QueryHandler(BaseHandler):
    def __init__(self, engine_context):
        self.engine_context = engine_context
        self.data_sources = engine_context.data_sources
        self.evaluator = engine_context.evaluator
        self.projector = engine_context.projector

    def can_handle(self, ast):
        return isinstance(ast, Query)

    def handle(self, query):
        data = self.engine_context.source_resolver.resolve(query.source)

        if data is None:
            raise ValueError(f"Unknown source: {query.source}")

        rows = []

        if query.where:
            rows = (
                row for row in data
                if self.evaluator.evaluate(query.where, row)
            )

            rows = (
                self.projector.project(query.select, row)
                for row in rows
            )
        else:
            rows = self.projector.project(query.select, data)

        return list(rows)
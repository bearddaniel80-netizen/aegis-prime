from .base import StatementStrategy
from ...language.tokens import TokenType
from ...language.ast.statements.query import Query
from .clause_registry import CLAUSE_REGISTRY
from . import select_clauses
from ...context.analysis import AnalysisContext

class SelectStrategy(StatementStrategy):

    def can_handle(self, ctx):
        tok = ctx.peek()
        return tok and tok.type == TokenType.SELECT

    def parse(self, ctx, analysis_ctx: AnalysisContext):

        query = Query()

        for clause in CLAUSE_REGISTRY:
            query = clause.parse(ctx, query, analysis_ctx)

        return query
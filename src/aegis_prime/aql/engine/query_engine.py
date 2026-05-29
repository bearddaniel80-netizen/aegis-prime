from aegis_prime.aql.parser.parser import Parser
from aegis_prime.aql.lexer.lexer import Lexer
from aegis_prime.aql.adapter.source.factory import StdinSourceFactory
from aegis_prime.aql.planner.planner import Planner
from aegis_prime.aql.planner.context import PlanningContext
from .exe_source import SourceResolver
import sys

class EngineContext:
    def __init__(self, data_sources, evaluator, projector, registry, inspector):
        self.data_sources = data_sources
        self.evaluator = evaluator
        self.projector = projector
        self.registry = registry
        self.inspector = inspector
        self.source_resolver = SourceResolver(data_sources)

class QueryEngine:
    def __init__(self, execution_engine):
        self.executor = execution_engine
        self._add_adapters()

    def run(self, query: str):
        tokens = self._lex(query)
        ast = self._parse(tokens)
        result = self._execute(ast)
        
#        plan = self._planner(ast, None)
#        result = self._execute(plan)
        return result

    # ---- adding adapters ----
    def _add_adapters(self):
        if not hasattr(self.executor, "data_sources"):
            self.executor.data_sources = {}

        self.executor.data_sources["stdin"] = StdinSourceFactory

    # ---- pipeline stages ----

    def _lex(self, query: str):
        return Lexer(query).tokenize()

    def _parse(self, tokens):
        return Parser(tokens).parse()

    def _planner(self, ast, ddl_input):
        context = PlanningContext(
            has_stdin=not sys.stdin.isatty(),
            ddl=ddl_input
        )

        return Planner(context).plan(ast)

    def _execute(self, plan):
        return self.executor.execute(plan)
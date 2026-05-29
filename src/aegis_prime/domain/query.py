import typer
from typing import Optional
from rich import print_json

from aegis_prime.aql.schema.inspector import SchemaInspector
from aegis_prime.aql.adapter.source.factory import StdinSourceFactory
from aegis_prime.aql.evalulators.evalulate import Evaluator
from aegis_prime.aql.engine.projector import Projector
from aegis_prime.aql.engine.query_engine import QueryEngine, EngineContext
from aegis_prime.aql.engine.executor import ExecutionEngine
from aegis_prime.config.loader import load_config_context
from aegis_prime.config.cli_merge import CLIOverrides
from aegis_prime.config.resolver import ConfigResolver
from aegis_prime.core.model_registry import MODEL_REGISTRY
from aegis_prime import models

def normalize_query(query: str, data_sources: dict) -> str:
    if "FROM" not in query.upper() and data_sources["stdin"] is not None:
        return query.strip() + " FROM stdin"
    return query

def build_cli_overrides(
    q: str,
    source: str = None,
    format: str = None,
    limit: int = None,
    offset: int = None,
    debug: bool = None,
    profile: str = None,
):
    return CLIOverrides(
        source=source,
        format=format,
        limit=limit,
        offset=offset,
        debug=debug,
        profile=profile,
    )

def build_engine(data_sources, q, file, limit) -> QueryEngine:

    data_sources = {**MODEL_REGISTRY, **data_sources}
    config = load_config_context("aegis.toml")
    cli = build_cli_overrides(q)
    engine_context = EngineContext(
        data_sources=data_sources,
        evaluator=Evaluator(),
        projector=Projector(),
        registry=MODEL_REGISTRY,
        inspector=SchemaInspector(),
    )

    resolver = ConfigResolver(config, cli)
    config_ctx = resolver.resolve()
    execution_engine = ExecutionEngine(engine_context, config_ctx)
    return QueryEngine(execution_engine)

def query_results(q: str, file: str, limit: Optional[int]):
    data_sources = {}
    data_sources["stdin"] = StdinSourceFactory
    engine = build_engine(data_sources, q, file, limit)

    q = normalize_query(q, data_sources)

    # print_json(data=engine.run(q))
    result = engine.run(q)
    
    result = list(result)

    print_json(data=result)
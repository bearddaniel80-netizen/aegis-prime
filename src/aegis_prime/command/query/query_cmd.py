import typer
from typing import Optional

from aegis_prime.core.settings import CLUSTER
from aegis_prime.domain.query import query_results
from .build_subcmd import build_app

app = typer.Typer(invoke_without_command=True)

@app.callback()
def main(
    ctx: typer.Context,
    q: str = typer.Argument(..., help="AQL query string"),
    file: str = typer.Option(CLUSTER, "--file", "-f", help="Path to cluster JSON"),
    limit: Optional[int] = typer.Option(None, "--limit", "-l", help="Override LIMIT"),
):
    if ctx.invoked_subcommand is None:
        query_results(q, file, limit)

app.add_typer(build_app, name="build")
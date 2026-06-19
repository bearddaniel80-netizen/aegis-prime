import typer

from .command.graph import (
    app as graph_app,
)

app = typer.Typer(
    help="Traceplan Framework"
)

app.add_typer(
    graph_app,
    name="graph",
)
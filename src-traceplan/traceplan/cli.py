import typer

from .command.graph import app as graph_app
from .command.snapshot import app as snapshot_app
from .command.analyze import app as analyze_app

app = typer.Typer(
    help="TracePlan - Architecture Intelligence Platform"
)

app.add_typer(
    graph_app,
    name="graph"
)

app.add_typer(
    snapshot_app,
    name="snapshot"
)

app.add_typer(
    analyze_app,
    name="analyze"
)

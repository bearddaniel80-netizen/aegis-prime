import typer
from ..models import (
    OutputFormat,
    DepthType,
)

from ..core.snapshot import cmd_build
from ..core.diff import cmd_diff
from ..core.impact import cmd_impact

app = typer.Typer()

@app.command()
def build(
    _format: OutputFormat = typer.Option(
        OutputFormat.JSON,
        "--format",
        help="Output format"
    ),
    include_tests: bool = typer.Option(
        True,
        "--include-tests",
        help="Enable test cases",
    ),
    exclude: str = typer.Option(
        "node_modules",
        "--exclude",
        help="Enable result caching",
    ),
    incremental: bool = typer.Option(
        False,
        "--incremental",
        help="Enable incremental build",
    ),
    cache: str = typer.Option(
        "traceplan/cache",
        "--cache",
        help="Enable result caching",
    ),
):
    raise NotImplementedError("coming soon")

@app.command()
def show():
    raise NotImplementedError("coming soon")

@app.command()
def query():
    raise NotImplementedError("coming soon")

@app.command()
def impact(
    depth: DepthType = typer.Option(
        DepthType.ONE,
        "--depth",
        help="How much is effected"
    ),
    include_externals: bool = typer.Option(
        False,
        "--include-externals",
        help="Enable analysis of external dependencies",
    ),
    _format: OutputFormat = typer.Option(
        OutputFormat.JSON,
        "--format",
        help="Output format"
    ),
):
    raise NotImplementedError("coming soon")

@app.command()
def diff(
    semantics: bool = typer.Option(
        False,
        "--semantics",
        help="Enable analysis of semantics",
    ),
    api_only: bool = typer.Option(
        False,
        "--api-only",
        help="???",
    ),
    behavior: bool = typer.Option(
        False,
        "--behavior",
        help="???",
    ),
):
    raise NotImplementedError("coming soon")

@app.command()
def export():
    raise NotImplementedError("coming soon")

@app.command()
def stats():
    raise NotImplementedError("coming soon")

@app.command()
def watch():
    raise NotImplementedError("coming soon")

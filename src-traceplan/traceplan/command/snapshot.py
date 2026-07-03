import typer

from ..snapshots.storage import (
    list_snapshots
)

app = typer.Typer()


@app.command("list")
def snapshots():
    """
    List snapshots.
    """

    for snapshot in list_snapshots():
        typer.echo(snapshot)
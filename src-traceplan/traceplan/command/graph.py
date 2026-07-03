import typer

from pathlib import Path

from ..graph.build import build_snapshot
from ..snapshots.storage import load_snapshot, save_snapshot
from ..graph.diff import diff
from ..graph.summary import print_summary, print_diff_summary

app = typer.Typer()

@app.command("build")
def build(
    source: str,
    output: str = "snapshot.json"
):
    """
    Build graph snapshot from source code.
    """

    snapshot = build_snapshot(source)

    save_snapshot(
        snapshot,
        output
    )

    print_summary(snapshot)

    typer.echo(
        f"Snapshot written to {output}"
    )


@app.command("diff")
def graph_diff(
    old_snapshot: str,
    new_snapshot: str
):
    """
    Compare two snapshots.
    """

    old = load_snapshot(old_snapshot)
    new = load_snapshot(new_snapshot)

    delta = diff(old, new)

    print_diff_summary(delta)
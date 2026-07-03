from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from .models import GraphDelta

def _delta_style(value: int) -> str:
    """
    Red for increases.
    Green for decreases.
    White for unchanged.
    """

    if value > 0:
        return "bold red"

    if value < 0:
        return "bold green"

    return "white"

def print_diff_summary(
    delta: GraphDelta
) -> None:

    console = Console()

    added_nodes = len(delta.added_nodes)
    removed_nodes = len(delta.removed_nodes)
    modified_nodes = len(delta.modified_nodes)

    added_edges = len(delta.added_edges)
    removed_edges = len(delta.removed_edges)

    total_changes = (
        added_nodes
        + removed_nodes
        + modified_nodes
        + added_edges
        + removed_edges
    )

    risk_score = getattr(
        delta,
        "risk_score",
        0
    )

    summary = Table(
        title="Graph Delta Summary"
    )

    summary.add_column(
        "Metric",
        style="cyan"
    )

    summary.add_column(
        "Count",
        justify="right"
    )

    summary.add_row(
        "Added Nodes",
        f"[red]{added_nodes}[/red]"
    )

    summary.add_row(
        "Removed Nodes",
        f"[green]{removed_nodes}[/green]"
    )

    summary.add_row(
        "Modified Nodes",
        f"[yellow]{modified_nodes}[/yellow]"
    )

    summary.add_row(
        "Added Edges",
        f"[red]{added_edges}[/red]"
    )

    summary.add_row(
        "Removed Edges",
        f"[green]{removed_edges}[/green]"
    )

    summary.add_section()

    summary.add_row(
        "Unchanged Nodes",
        f"[white]{delta.unchanged_nodes}[/white]"
    )

    summary.add_row(
        "Unchanged Edges",
        f"[white]{delta.unchanged_edges}[/white]"
    )

    console.print(summary)

    risk_style = (
        "bold green"
        if risk_score == 0
        else "bold red"
    )

    console.print(
        Panel.fit(
            f"[{risk_style}]Risk Score: {risk_score}[/{risk_style}]",
            title="Change Risk"
        )
    )

    console.print(
        Panel.fit(
            (
                f"[yellow]Total Changes:[/yellow] "
                f"{total_changes}"
            ),
            title="Overview"
        )
    )

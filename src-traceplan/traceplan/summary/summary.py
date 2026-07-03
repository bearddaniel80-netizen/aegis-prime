from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from .models import GraphSummary

def print_summary(
    summary: GraphSummary
) -> None:

    console = Console()

    header = Table.grid(expand=True)

    header.add_row(
        f"[bold]Nodes:[/bold] {summary.total_nodes}",
        f"[bold]Edges:[/bold] {summary.total_edges}"
    )

    console.print(
        Panel(
            header,
            title="TracePlan Graph Summary",
            expand=False
        )
    )

    node_table = Table(
        title="Node Types"
    )

    node_table.add_column(
        "Type"
    )

    node_table.add_column(
        "Count",
        justify="right"
    )

    node_table.add_row(
        "Classes",
        str(summary.classes)
    )

    node_table.add_row(
        "Functions",
        str(summary.functions)
    )

    console.print(node_table)

    edge_table = Table(
        title="Edge Types"
    )

    edge_table.add_column(
        "Type"
    )

    edge_table.add_column(
        "Count",
        justify="right"
    )

    edge_table.add_row(
        "Calls",
        str(summary.calls)
    )

    edge_table.add_row(
        "Imports",
        str(summary.imports)
    )

    edge_table.add_row(
        "Contains",
        str(summary.contains)
    )

    console.print(edge_table)

    resolution_table = Table(
        title="Call Resolution"
    )

    resolution_table.add_column(
        "Metric"
    )

    resolution_table.add_column(
        "Value",
        justify="right"
    )

    resolution_table.add_row(
        "Resolved Calls",
        str(summary.resolved_calls)
    )

    resolution_table.add_row(
        "Unresolved Calls",
        str(summary.unresolved_calls)
    )

    resolution_table.add_row(
        "Average Confidence",
        f"{summary.avg_confidence:.2f}"
    )

    console.print(resolution_table)
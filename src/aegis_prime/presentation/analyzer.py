
from rich.table import Table
from rich.console import Console

def pretty_print(clusters: list):
    console = Console()

    table = Table(title="🔍 Failure Clusters:")

    table.add_column("Id", style="cyan", no_wrap=True)
    table.add_column("Error Type", style="magenta")
    table.add_column("Pattern", style="yellow")
    table.add_column("Frequency", style="white", no_wrap=True)
    table.add_column("Serverity", style="green")

    for cluster in clusters:
        table.add_row(
            str(cluster.cluster_id),
            cluster.error_type.value,
            cluster.signature().split(":")[1] if ":" in cluster.signature() else "",
            str(cluster.frequency),
            cluster.severity.value,
        )

    console.print(table)
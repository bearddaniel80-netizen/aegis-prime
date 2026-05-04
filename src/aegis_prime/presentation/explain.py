from aegis_prime.services.root_cause import detect_root_cause_from_logs
from rich.table import Table
from rich.console import Console

def pretty_print(clusters: list):
    console = Console()

    table = Table(title="🧠 Aegis Explanation:")

    table.add_column("Id", style="cyan", no_wrap=True)
    table.add_column("Error Type", style="magenta")
    table.add_column("Tests Effected", style="yellow")
    table.add_column("Root Cause", style="white")

    for cluster in clusters:
        tests = ', \n'.join(cluster['tests'])
        root = detect_root_cause_from_logs(cluster)
        table.add_row(
            str(cluster['cluster_id']),
            cluster['error_type'],
            tests,
            root
        )

    console.print(table)
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from .models import NodeAnalysis

def print_analysis(
    analysis: NodeAnalysis
) -> None:

    console = Console()

    node = analysis.node

    details = Table()

    details.add_column(
        "Property"
    )

    details.add_column(
        "Value"
    )

    details.add_row(
        "Name",
        node.name
    )

    details.add_row(
        "Type",
        node.type
    )

    details.add_row(
        "FQDN",
        node.fqdn
    )

    details.add_row(
        "File",
        node.file
    )

    details.add_row(
        "Line",
        str(node.line)
    )
    metrics = Table(
        title="Metrics"
    )

    metrics.add_column(
        "Metric"
    )

    metrics.add_column(
        "Value"
    )

    metrics.add_row(
        f"{_fan_in_icon(analysis.fan_in)} Fan In",
        str(analysis.fan_in)
    )

    metrics.add_row(
        "Fan Out",
        str(analysis.fan_out)
    )

    metrics.add_row(
        "Imports",
        str(analysis.import_count)
    )

    metrics.add_row(
        "Calls",
        str(analysis.call_count)
    )

    metrics.add_row(
        "Confidence",
        f"{analysis.confidence_avg:.2f}"
    )

    metrics.add_row(
        "Risk Score",
        str(
            _risk_score(
                analysis
            )
        )
    )

    metrics.add_row(
        "Criticality",
        _classify(
            analysis
        )
    )
    incoming = Table(
        title="Depends On Me"
    )

    incoming.add_column(
        "Node"
    )

    for dep in analysis.incoming:

        incoming.add_row(dep)
    outgoing = Table(
        title="I Depend On"
    )

    outgoing.add_column(
        "Node"
    )

    for dep in analysis.outgoing:

        outgoing.add_row(dep)

    console.print(
        Panel(
            details,
            title="Node Details"
        )
    )
    console.print(metrics)
    console.print(incoming)
    console.print(outgoing)

def _fan_in_icon(fan_in: int):

    if fan_in >= 20:
        return "🌋"

    if fan_in >= 10:
        return "🔥"

    if fan_in >= 5:
        return "⚡"

    return "🟢"

def _risk_score(
    analysis: NodeAnalysis
) -> int:

    score = 0

    score += (
        analysis.fan_in * 3
    )

    score += (
        analysis.fan_out * 1
    )

    return score

def _classify(
    analysis: NodeAnalysis
) -> str:

    if analysis.fan_in >= 20:
        return "Critical"

    if analysis.fan_in >= 10:
        return "High"

    if analysis.fan_in >= 5:
        return "Medium"

    return "Low"
import typer

from ..snapshots.storage import load_snapshot
from ..graph.analyze import analyze
from ..summary.analyze import print_analysis

app = typer.Typer()

@app.command("node")
def analyze_node(
    snapshot: str,
    node: str
):
    """
    Analyze a graph node.
    """

# context = analyze_context(snapshot, "Optimizer.optimize")
# 
# pipeline.run(context)

    graph = load_snapshot(snapshot)

    result = analyze(
        graph,
        node
    )

    print_analysis(result)
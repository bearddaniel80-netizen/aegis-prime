from collections import Counter

from .models import GraphSnapshot

from ..summary.models import GraphSummary

def summarize(
    snapshot: GraphSnapshot
) -> GraphSummary:

    node_types = Counter(
        node.type
        for node in snapshot.nodes.values()
    )

    edge_types = Counter(
        edge.type
        for edge in snapshot.edges
    )

    call_edges = [
        edge
        for edge in snapshot.edges
        if edge.type == "calls"
    ]

    resolved_calls = [
        edge
        for edge in call_edges
        if edge.confidence >= 0.80
    ]

    unresolved_calls = [
        edge
        for edge in call_edges
        if edge.confidence < 0.80
    ]

    avg_confidence = 0.0

    if call_edges:
        avg_confidence = (
            sum(
                edge.confidence
                for edge in call_edges
            )
            / len(call_edges)
        )

    return GraphSummary(
        total_nodes=len(snapshot.nodes),
        total_edges=len(snapshot.edges),

        classes=node_types.get("class", 0),
        functions=node_types.get("function", 0),

        imports=edge_types.get("imports", 0),
        calls=edge_types.get("calls", 0),
        contains=edge_types.get("contains", 0),

        resolved_calls=len(resolved_calls),
        unresolved_calls=len(unresolved_calls),

        avg_confidence=avg_confidence
    )

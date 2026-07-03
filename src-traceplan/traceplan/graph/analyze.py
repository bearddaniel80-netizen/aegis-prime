from .models import GraphSnapshot, NodeAnalysis

def analyze(
    snapshot: GraphSnapshot,
    node_id: str
) -> NodeAnalysis:

    node = snapshot.nodes.get(
        node_id
    )

    if not node:

        raise ValueError(
            f"Node not found: {node_id}"
        )

    incoming = []
    outgoing = []

    confidence_values = []

    import_count = 0
    call_count = 0

    for edge in snapshot.edges:

        if edge.dst == node_id:

            incoming.append(
                edge.src
            )

        if edge.src == node_id:

            outgoing.append(
                edge.dst
            )

            confidence_values.append(
                edge.confidence
            )

            if edge.type == "imports":
                import_count += 1

            if edge.type == "calls":
                call_count += 1

    avg_confidence = 0.0

    if confidence_values:

        avg_confidence = (
            sum(confidence_values)
            / len(confidence_values)
        )

    return NodeAnalysis(
        node=node,

        incoming=incoming,

        outgoing=outgoing,

        import_count=import_count,

        call_count=call_count,

        fan_in=len(incoming),

        fan_out=len(outgoing),

        confidence_avg=avg_confidence
    )

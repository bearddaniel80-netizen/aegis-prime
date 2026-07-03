from .models import Edge, GraphSnapshot, GraphDelta, Node

def diff(
    old: GraphSnapshot,
    new: GraphSnapshot
) -> GraphDelta:

    delta = GraphDelta()

    old_nodes = old.nodes
    new_nodes = new.nodes

    #
    # Added Nodes
    #

    for node_id in new_nodes:

        if node_id not in old_nodes:

            delta.added_nodes.append(
                new_nodes[node_id]
            )

    #
    # Removed Nodes
    #

    for node_id in old_nodes:

        if node_id not in new_nodes:

            delta.removed_nodes.append(
                old_nodes[node_id]
            )

    #
    # Modified Nodes
    #

    for node_id in (
        old_nodes.keys()
        & new_nodes.keys()
    ):

        old_node = old_nodes[node_id]
        new_node = new_nodes[node_id]

        if _node_changed(
            old_node,
            new_node
        ):

            delta.modified_nodes.append(
                (
                    old_node,
                    new_node
                )
            )

        else:

            delta.unchanged_nodes += 1

    #
    # Edge Diff
    #

    old_edges = set(
        _edge_key(edge)
        for edge in old.edges
    )

    new_edges = set(
        _edge_key(edge)
        for edge in new.edges
    )

    added_edge_keys = (
        new_edges - old_edges
    )

    removed_edge_keys = (
        old_edges - new_edges
    )

    for edge in new.edges:

        if _edge_key(edge) in added_edge_keys:

            delta.added_edges.append(
                edge
            )

    for edge in old.edges:

        if _edge_key(edge) in removed_edge_keys:

            delta.removed_edges.append(
                edge
            )

    delta.unchanged_edges = len(
        old_edges & new_edges
    )

    return delta

def _node_changed(
    old: Node,
    new: Node
) -> bool:

    return (
        old.fingerprint
        != new.fingerprint
    )

def _edge_key(
    edge: Edge
):

    return (
        edge.src,
        edge.dst,
        edge.type
    )
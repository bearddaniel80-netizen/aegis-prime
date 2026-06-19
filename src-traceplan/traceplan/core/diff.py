from ..models import (
    Node,
    Snapshot
)
def print_summary(delta: dict):
    added_nodes = delta["added_nodes"]
    removed_nodes = delta["removed_nodes"]
    added_edges = delta["added_edges"]
    removed_edges = delta["removed_edges"]

    print("\n=== TracePlan Graph Diff ===\n")

    # Nodes
    print("Added Nodes:")
    if added_nodes:
        for n in sorted(added_nodes, key=lambda x: x.id):
            print(f"  + {n.id} ({n.type})")
    else:
        print("  (none)")

    print("\nRemoved Nodes:")
    if removed_nodes:
        for n in sorted(removed_nodes, key=lambda x: x.id):
            print(f"  - {n.id} ({n.type})")
    else:
        print("  (none)")

    # Edges
    print("\nAdded Edges:")
    if added_edges:
        for e in sorted(added_edges, key=lambda x: (x.src, x.dst, x.type)):
            print(f"  + {e.src} -> {e.dst} [{e.type}]")
    else:
        print("  (none)")

    print("\nRemoved Edges:")
    if removed_edges:
        for e in sorted(removed_edges, key=lambda x: (x.src, x.dst, x.type)):
            print(f"  - {e.src} -> {e.dst} [{e.type}]")
    else:
        print("  (none)")

    # Lightweight summary stats
    print("\n=== Summary ===")
    print(f"Nodes: +{len(added_nodes)} / -{len(removed_nodes)}")
    print(f"Edges: +{len(added_edges)} / -{len(removed_edges)}")

    print("\n===========================\n")
    
def diff(a: Snapshot, b: Snapshot):
    added_nodes = b.nodes - a.nodes
    removed_nodes = a.nodes - b.nodes

    added_edges = b.edges - a.edges
    removed_edges = a.edges - b.edges

    return {
        "added_nodes": list(added_nodes),
        "removed_nodes": list(removed_nodes),
        "added_edges": list(added_edges),
        "removed_edges": list(removed_edges),
    }

def cmd_diff(a_path, b_path):
    a = load_snapshot(a_path)
    b = load_snapshot(b_path)

    delta = diff(a, b)

    print_summary(delta)
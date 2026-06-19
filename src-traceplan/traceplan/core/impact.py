from collections import deque
from ..models import ImpactResult

ALLOWED_REL = {"imports", "calls"}

def impact(graph, start):
    visited = set()
    queue = deque([(start, 0)])

    depth_map = {}
    affected = set()

    while queue:
        node, depth = queue.popleft()

        if node in visited:
            continue
        visited.add(node)

        for edge in graph.out_edges(node):
            target = edge.dst
            
            if edge.type not in ALLOWED_REL:
                continue

            if target not in visited:
                affected.add(target)
                depth_map[target] = depth + 1
                queue.append((target, depth + 1))

    return ImpactResult(
        root=start,
        nodes=affected,
        edges=set(),
        depth_map=depth_map
    )

def cmd_impact(graph, node_id):
    result = impact(graph, node_id)

    print(f"\n=== Impact: {node_id} ===\n")

    for node, depth in sorted(result.depth_map.items(), key=lambda x: x[1]):
        print(f"{'  ' * depth}→ {node} (depth {depth})")

    print(f"\nTotal affected: {len(result.nodes)}")
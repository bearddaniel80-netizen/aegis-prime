from dataclasses import dataclass, field

from ..graph.models import Edge, Node
CRITICALITY_ICONS = {
    "Critical": "🚨",
    "High":     "🔴",
    "Medium":   "🟡",
    "Low":      "🟢"
}
RISK_ICONS = {
    "Critical": "☢️",
    "High":     "⚠️",
    "Medium":   "🔍",
    "Low":      "✅"
}
# ----------- analyze.py --------
@dataclass
class NodeAnalysis:
    node: Node
    incoming: list[str]
    outgoing: list[str]
    import_count: int
    call_count: int
    fan_in: int
    fan_out: int
    confidence_avg: float

# ----- diff.py -------------
CHANGE_ICONS = {
    "added": "➕",
    "removed": "➖",
    "modified": "✏️",
    "renamed": "🔄",
    "moved": "📦"
}
@dataclass
class GraphDelta:
    added_nodes: list[Node] = field(default_factory=list)
    removed_nodes: list[Node] = field(default_factory=list)
    modified_nodes: list[tuple[Node, Node]] = field(default_factory=list)
    added_edges: list[Edge] = field(default_factory=list)
    removed_edges: list[Edge] = field(default_factory=list)
    unchanged_nodes: int = 0
    unchanged_edges: int = 0
    
    @property
    def changed(self):

        return bool(
            self.added_nodes
            or self.removed_nodes
            or self.modified_nodes
            or self.added_edges
            or self.removed_edges
        )

    @property
    def risk_score(self):

        score = 0

        score += len(
            self.modified_nodes
        ) * 2

        score += len(
            self.added_nodes
        )

        score += len(
            self.removed_nodes
        ) * 3

        score += len(
            self.added_edges
        )

        return score
# ----- summary.py ----------
@dataclass
class GraphSummary:
    total_nodes: int
    total_edges: int
    classes: int
    functions: int
    imports: int
    calls: int
    contains: int
    resolved_calls: int
    unresolved_calls: int
    avg_confidence: float
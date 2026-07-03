from dataclasses import dataclass, field

@dataclass
class ExtractionResult:
    nodes: list[Node]
    edges: list[Edge]
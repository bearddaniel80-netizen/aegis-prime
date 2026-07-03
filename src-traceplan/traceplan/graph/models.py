from dataclasses import dataclass, field

@dataclass(frozen=True)
class Node:
    id: str 
    name: str
    fqdn: str = "" # fully qualified domain name
    line: int = 0
    file: str = ""
    _type: str = ""
    fingerprint: str = ""
    service: str = ""  # NEW
    
@dataclass(frozen=True)
class Edge:
    src: str
    dst: str
    _type: str
    cross_service_call: str = ""
    confidence: float = 1.0
    truth_score: float = 1.0

@dataclass
class GraphSnapshot:
    nodes: dic[str, Node]
    edges: set[Edge]
    metadata: dict = field(default_factory=dict)





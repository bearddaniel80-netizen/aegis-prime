from enum import StrEnum
from dataclasses import dataclass, field

@dataclass
class ImpactResult:
    root: str
    nodes: set[str]
    edges: set[tuple]
    depth_map: dict[str, int]

@dataclass
class Snapshot:
    nodes: set[Node]
    edges: set[Edge]

@dataclass(frozen=True)
class Edge:
    src: str
    dst: str
    type: str        # imports | calls | contains

@dataclass(frozen=True)
class Node:
    id: str          # stable symbol id
    name: str
    type: str        # class | function | module
    file: str
"""
@dataclass
class GraphNode:
    id: str
    type: str
    fingerprint: str

@dataclass
class GraphEdge:
    src: str
    dst: str
    relationship: str

@dataclass
class GraphDelta:
    event: str
    entity_id: str
    payload: dict
"""
# -------- Commands -------------
class DepthType(StrEnum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    ALL = "all"

class OutputFormat(StrEnum):
    JSON = "json"
    PARQUET = "parquet"
    SQLITE = "sqlite"
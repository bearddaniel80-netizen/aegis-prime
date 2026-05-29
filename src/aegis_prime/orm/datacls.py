from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, List

# -----------------------------
# AST NODES (AQL INTERMEDIATE)
# -----------------------------

@dataclass
class Condition:
    key: str
    op: str
    value: Any

@dataclass
class SelectQuery:
    model: str
    fields: List[str]
    conditions: List[Condition] = field(default_factory=list)
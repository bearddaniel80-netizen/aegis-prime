from __future__ import annotations
from typing import Any, List, Dict
from .datacls import SelectQuery, Condition

# -----------------------------
# QUERY BUILDER (FLUENT API)
# -----------------------------

class Query:
    def __init__(self, model: str):
        self.model = model
        self.fields = ["*"]
        self.conditions: List[Condition] = []

    def select(self, *fields: str) -> Query:
        self.fields = list(fields)
        return self

    def where(self, **kwargs) -> Query:
        for k, v in kwargs.items():
            self.conditions.append(Condition(k, "=", v))
        return self

    def where_in(self, key: str, values: List[Any]) -> Query:
        self.conditions.append(Condition(key, "in", values))
        return self

    def compile(self) -> SelectQuery:
        return SelectQuery(
            model=self.model,
            fields=self.fields,
            conditions=self.conditions
        )

    def all(self) -> List[Dict[str, Any]]:
        return Executor.run(self.compile())
from __future__ import annotations
from typing import Any, List, Dict
from .datacls import SelectQuery

# -----------------------------
# COMPILER (AST -> EXECUTION)
# -----------------------------

class Executor:
    @staticmethod
    def run(query: SelectQuery) -> List[Dict[str, Any]]:
        rows = DB.get(query.model, [])
        
        def matches(row: Dict[str, Any]) -> bool:
            for c in query.conditions:
                if c.op == "=" and row.get(c.key) != c.value:
                    return False
                if c.op == "!=" and row.get(c.key) == c.value:
                    return False
                if c.op == "in" and row.get(c.key) not in c.value:
                    return False
            return True

        filtered = [r for r in rows if matches(r)]

        result = []
        for r in filtered:
            if query.fields == ["*"]:
                result.append(r)
            else:
                result.append({f: r.get(f) for f in query.fields})
        return result
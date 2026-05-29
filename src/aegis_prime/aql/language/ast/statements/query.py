from .base import Statement

class Query(Statement):
    def __init__(self, select, source, where=None, limit=None):
        self.select = select      # List[Field]
        self.source = source      # Identifier or str
        self.where = where        # Expression or None
        self.limit = limit        # int or None

    def __repr__(self):
        parts = [
            f"SELECT {', '.join(str(f) for f in self.select)}",
            f"FROM {self.source}"
        ]

        if self.where:
            parts.append(f"WHERE {self.where}")

        if self.limit is not None:
            parts.append(f"LIMIT {self.limit}")

        return " ".join(parts)

    def to_dict(self):
        return {
            "type": "query",
            "select": [f.to_dict() for f in self.select],
            "from": self.source.to_dict() if hasattr(self.source, "to_dict") else self.source,
            "where": self.where.to_dict() if self.where else None,
            "limit": self.limit
        }

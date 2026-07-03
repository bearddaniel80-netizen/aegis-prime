from aegis_prime.aql.language.ast.base import ASTNode

class ListLiteral(ASTNode):
    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f"ListLiteral([{', '.join(repr(v) for v in self.values)}])"

    def to_dict(self):
        return {
            "type": "list",
            "values": [v.to_dict() for v in self.values]
        }

class Literal(ASTNode):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Literal({self.value})"

    def to_dict(self):
        return {
            "type": "literal",
            "value": self.value
        }

    def __eq__(self, other):
        return isinstance(other, Literal) and self.value == other.value

    def __hash__(self):
        return hash((Literal, self.value))
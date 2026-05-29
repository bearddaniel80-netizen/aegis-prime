from .base import Pattern

class Literal(Pattern):
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
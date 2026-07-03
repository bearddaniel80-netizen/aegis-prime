from .base import ASTNode

class Identifier(ASTNode):
    def __init__(self, name: str, alias=None):
        self.name = name
        self.alias = alias

    def __repr__(self):
        return f"Identifier( name: {self.name} alias: {self.alias})"

    def to_dict(self):
        return {
            "type": "identifier",
            "name": self.name,
            "alias": self.alias,
        }

    def __eq__(self, other):
        return isinstance(other, Identifier) and self.name == other.name

    def __hash__(self):
        return hash((Identifier, self.name))
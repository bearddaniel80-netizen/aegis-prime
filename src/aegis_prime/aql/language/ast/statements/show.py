from aegis_prime.aql.language.ast.identifier import Identifier
from .base import Statement

class Show(Statement):
    def __init__(self, target: Identifier):
        self.target = target

    def __repr__(self):
        return f"Show({self.target})"

    def to_dict(self):
        return {
            "type": "show",
            "target": self.target.to_dict()
        }

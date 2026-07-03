from aegis_prime.aql.language.ast.identifier import Identifier
from .base import Statement

class Describe(Statement):
    def __init__(self, target: Identifier):
        self.target = target

    def __repr__(self):
        return f"Describe({self.target})"

    def to_dict(self):
        return {
            "type": "Describe",
            "target": self.target.to_dict()
        }

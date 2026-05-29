from aegis_prime.aql.language.ast.base import ASTNode

class Field(ASTNode):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Field({self.name})"

    def to_dict(self):
        return {
            "type": "field",
            "name": self.name
        }
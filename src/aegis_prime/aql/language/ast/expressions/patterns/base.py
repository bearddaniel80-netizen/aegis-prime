from aegis_prime.aql.language.ast.base import ASTNode

class Pattern(ASTNode):
    def to_dict(self):
        raise NotImplementedError
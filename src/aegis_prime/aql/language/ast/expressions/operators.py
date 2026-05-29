from aegis_prime.aql.language.ast.base import ASTNode

class BinaryOp(ASTNode):
    def __init__(self, left, operator: str, right):
        self.left = left          # Expression
        self.operator = operator  # '=', '<', '>'
        self.right = right        # Expression

    def __repr__(self):
        return f"BinaryOp({self.left} {self.operator} {self.right})"

    def to_dict(self):
        return {
            "type": "binary_op",
            "operator": self.operator,
            "left": self.left.to_dict(),
            "right": self.right.to_dict()
        }

class InOp(ASTNode):
    def __init__(self, left, right):
        self.left = left          # Expression
        self.right = right        # Expression

    def __repr__(self):
        return f"InOp({self.left} {self.right})"

    def to_dict(self):
        return {
            "type": "in_op",
            "left": self.left.to_dict(),
            "right": self.right.to_dict()
        }

class LogicalOp(ASTNode):
    def __init__(self, left, operator: str, right):
        self.left = left
        self.operator = operator  # "AND", "OR"
        self.right = right

    def __repr__(self):
        return f"LogicalOp({self.left} {self.operator} {self.right})"

    def to_dict(self):
        return {
            "type": "logical_op",
            "operator": self.operator,
            "left": self.left.to_dict(),
            "right": self.right.to_dict()
        }

class LikeOp(ASTNode):
    from functools import lru_cache
    from aegis_prime.aql.evalulators.handlers.like.optimizer import optimize_pattern
    from aegis_prime.aql.evalulators.handlers.like.parser import parse_like_pattern
    def __init__(self, left, pattern: str):
        self.left = left
        self.pattern = self.compile_like(pattern)

    def __repr__(self):
        return f"LikeOp({self.left} {self.pattern})"

    def to_dict(self):
        return {
            "type": "like_op",
            "left": self.left.to_dict(),
            "pattern": self.pattern
        }


    @lru_cache(maxsize=128)
    def compile_like(self, pattern):
        return optimize_pattern(parse_like_pattern(pattern))
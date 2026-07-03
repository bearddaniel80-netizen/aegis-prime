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

class RegexMatch:
    def __init__(self, field, pattern):
        self.field = field
        self.pattern = pattern

    def __repr__(self):
        return f"RegexMatch( field: {self.field.to_dict()} pattern: {self.pattern.to_dict()})"

    def to_dict(self):
        return {
            "type": "regexmatch",
            "field": self.field.to_dict(),
            "pattern": self.pattern.to_dict()
        }

class AndOp:
    def evaluate(self, row):
        return (
            self.left.evaluate(row)
            and
            self.right.evaluate(row)
        )

class OrOp:
    def evaluate(self, row):
        return (
            self.left.evaluate(row)
            or
            self.right.evaluate(row)
        )

class NotOp:
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"NotOp( expr: {self.expr.to_dict()} )"

    def to_dict(self):
        return {
            "type": "NotOp",
            "expr": self.expr.to_dict()
        }

class BetweenOp:
    def __init__(self, expr, lower, upper):
        self.expr = expr
        self.lower = lower
        self.upper = upper
        
class AndOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class OrOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right
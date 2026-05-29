from .base import ASTNode

# example SELECT upper(...)
class ScalarFunctionCall(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __repr__(self):
        return f"ScalarFunctionCall({self.name} {self.args})"

    def to_dict(self):
        return {
            "type": "ScalarFunctionCall",
            "name": self.name,
            "args": self.args.__repr__()
        }

# example FROM json(...)
class TableFunctionCall(ASTNode):
    def __init__(self, name, arg):
        self.name = name
        self.arg = arg

    def __repr__(self):
        return f"TableFunctionCall({self.name} {self.arg})"

    def to_dict(self):
        return {
            "type": "TableFunctionCall",
            "name": self.name,
            "arg": self.arg
        }
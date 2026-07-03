from .base import ASTNode

# example SELECT upper(...)
class FunctionCall(ASTNode):
    def __init__(self, name, args, alias=None):
        self.name = name
        self.arg = args
        self.alias = alias

    def __repr__(self):
        return f"FunctionCall( name: {self.name} arg: {self.arg} alias: {self.alias})"

    def to_dict(self):
        return {
            "type": "FunctionCall",
            "name": self.name,
            "args": self.args,
            "alias": self.alias,
        }

# example FROM json(...)
class TableFunctionCall(ASTNode):
    def __init__(self, name, arg, alias=None):
        self.name = name
        self.arg = arg
        self.alias = alias

    def __repr__(self):
        return f"TableFunctionCall( name: {self.name} arg: {self.arg} alias: {self.alias})"

    def to_dict(self):
        return {
            "type": "TableFunctionCall",
            "name": self.name,
            "arg": self.arg,
            "alias": self.alias,
        }

# example SELECT PARSE_KV(...)
class TransformCall(ASTNode):
    def __init__(self, name, arg, alias=None):
        self.name = name
        self.arg = arg
        self.alias = alias

    def __repr__(self):
        return f"TransformCall( name: {self.name} arg: {self.arg} alias: {self.alias})"

    def to_dict(self):
        return {
            "type": "TransformCall",
            "name": self.name,
            "arg": self.arg,
            "alias": self.alias,
        }
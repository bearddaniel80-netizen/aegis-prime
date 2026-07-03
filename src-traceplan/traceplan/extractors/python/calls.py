import ast

from ....graph.model import Edge
from ....resolver.resolve import Resolver

class CallVisitor(ast.NodeVisitor):

    def __init__(
        self,
        file,
        symbol_table=None
    ):

        self.file = file

        self.edges = []

        self.symbol_table = symbol_table

        self.current_class = None
        self.current_function = None
        self.resolver = Resolver(symbol_table)

    def visit_ClassDef(self, node):

        previous = self.current_class

        self.current_class = node.name

        self.generic_visit(node)

        self.current_class = previous

    def visit_FunctionDef(self, node):

        previous = self.current_function

        if self.current_class:

            self.current_function = (
                f"{self.current_class}.{node.name}"
            )

        else:

            self.current_function = node.name

        self.generic_visit(node)

        self.current_function = previous

    def visit_Call(self, node):

        if not self.current_function:
            return

        target = self.resolver.resolve(node)

        if target:

            self.edges.append(
                Edge(
                    src=self.current_function,
                    dst=target,
                    _type="calls"
                )
            )

        self.generic_visit(node)

    def visit_AsyncFunctionDef(
        self,
        node
    ):
        return self.visit_FunctionDef(
            node
        )
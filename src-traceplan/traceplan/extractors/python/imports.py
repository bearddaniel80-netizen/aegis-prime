import ast

from ....graph.model import (
    Edge
)

class ImportVisitor(ast.NodeVisitor):

    def __init__(self, file):

        self.module = file.stem

        self.edges = []

    def visit_Import(self, node):

        for alias in node.names:

            self.edges.append(
                Edge(
                    src=self.module,
                    dst=alias.name,
                    _type="imports"
                )
            )

    def visit_ImportFrom(self, node):

        module = node.module or ""

        self.edges.append(
            Edge(
                src=self.module,
                dst=module,
                _type="imports"
            )
        )
import ast
from pathlib import Path

from ....graph.model import (
    Node,
    Edge
)
from .fingerprints import (
    fingerprint_node
)
from .fqdn import (
    module_name_from_path
)


class SymbolVisitor(ast.NodeVisitor):

    def __init__(self, file: Path):

        self.file = str(file)

        self.module = module_name_from_path(
            file
        )

        self.nodes = []
        self.edges = []

        self.current_class = None

    def visit_ClassDef(
        self,
        node: ast.ClassDef
    ):

        fqdn = (
            f"{self.module}.{node.name}"
        )

        self.nodes.append(
            Node(
                id=fqdn,
                name=node.name,
                fqdn=fqdn,
                fingerprint=fingerprint_node(node),
                _type="class",

                file=self.file,
                line=node.lineno
            )
        )

        previous = self.current_class

        self.current_class = node.name

        self.generic_visit(node)

        self.current_class = previous

    def visit_FunctionDef(
        self,
        node: ast.FunctionDef
    ):

        if self.current_class:

            fqdn = (
                f"{self.module}."
                f"{self.current_class}."
                f"{node.name}"
            )

            parent = (
                f"{self.module}."
                f"{self.current_class}"
            )

            self.edges.append(
                Edge(
                    src=parent,
                    dst=fqdn,
                    _type="contains"
                )
            )

        else:

            fqdn = (
                f"{self.module}."
                f"{node.name}"
            )

        self.nodes.append(
            Node(
                id=fqdn,
                name=node.name,
                fqdn=fqdn,
                fingerprint=fingerprint_node(node),
                _type="function",

                file=self.file,
                line=node.lineno
            )
        )

        self.generic_visit(node)
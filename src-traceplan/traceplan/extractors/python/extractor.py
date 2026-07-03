import ast

from pathlib import Path

from ....graph.model import (
    Node,
    Edge
)

from ..models import (
    ExtractionResult
)

from .symbols import SymbolVisitor
from .imports import ImportVisitor
from .calls import CallVisitor


class PythonExtractor:

    @classmethod
    def extract(
        cls,
        file: Path,
        symbol_table=None
    ) -> ExtractionResult:

        source = file.read_text(
            encoding="utf-8"
        )

        tree = ast.parse(
            source,
            filename=str(file)
        )

        symbols = SymbolVisitor(file)
        symbols.visit(tree)

        imports = ImportVisitor(file)
        imports.visit(tree)

        calls = CallVisitor(
            file=file,
            symbol_table=symbol_table
        )
        calls.visit(tree)

        nodes = []
        edges = []

        nodes.extend(symbols.nodes)

        edges.extend(symbols.edges)
        edges.extend(imports.edges)
        edges.extend(calls.edges)

        return ExtractionResult(
            nodes=nodes,
            edges=edges
        )
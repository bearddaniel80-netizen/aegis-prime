from time import time

from .model import (
    GraphSnapshot,
    Node,
    Edge
)

from ..extractors.python.extractor import PythonExtractor
from .resolver import SymbolResolver
from traceplan_core.graph.fingerprint import Fingerprinter

class GraphBuilder:
    """
    Builds a GraphSnapshot from a source input.
    """

    def __init__(
        self,
        extractor=None,
        resolver=None,
        fingerprinter=None
    ):

        self.extractor = extractor or PythonExtractor()
        self.resolver = resolver or SymbolResolver()
        self.fingerprinter = fingerprinter or Fingerprinter()


    def build(self, source: str) -> GraphSnapshot:

        start = time()

        #
        # 1. Extract raw symbols
        #

        raw_model = self.extractor.extract(source)

        #
        # 2. Resolve symbols (imports, calls, fqns)
        #

        resolved = self.resolver.resolve(raw_model)

        #
        # 3. Fingerprint nodes (for diffing / compatibility)
        #

        fingerprinted = self.fingerprinter.apply(resolved)

        #
        # 4. Build graph structures
        #

        nodes = self._build_nodes(fingerprinted)
        edges = self._build_edges(fingerprinted)

        #
        # 5. Snapshot
        #

        snapshot = GraphSnapshot(
            nodes={n.id: n for n in nodes},
            edges=edges,
            metadata={
                "duration_ms": (time() - start) * 1000,
                "source": source
            }
        )

        return snapshot

    def _build_nodes(self, model):

        nodes = []

        for symbol in model.symbols:

            nodes.append(
                Node(
                    id=symbol.fqdn,
                    name=symbol.name,
                    type=symbol.type,
                    file=symbol.file,
                    line=symbol.line,
                    fingerprint=symbol.fingerprint
                )
            )

        return nodes

    def _build_edges(self, model):

        edges = []

        #
        # Imports
        #

        for imp in model.imports:

            edges.append(
                Edge(
                    src=imp.source_fqdn,
                    dst=imp.target_fqdn,
                    type="imports",
                    confidence=1.0
                )
            )

        #
        # Calls
        #

        for call in model.calls:

            edges.append(
                Edge(
                    src=call.caller_fqdn,
                    dst=call.callee_fqdn,
                    type="calls",
                    confidence=call.confidence
                )
            )

        #
        # Contains (hierarchy)
        #

        for relation in model.contains:

            edges.append(
                Edge(
                    src=relation.parent,
                    dst=relation.child,
                    type="contains",
                    confidence=1.0
                )
            )

        return edges
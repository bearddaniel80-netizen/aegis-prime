from datetime import datetime
from pathlib import Path

from ..extractors.python.extractor import (
    PythonExtractor
)

from .models import (
    GraphSnapshot,
    Node,
    Edge
)


SUPPORTED_EXTENSIONS = {
    ".py": PythonExtractor,
}


def build_snapshot(
    source: str | Path
) -> GraphSnapshot:
    """
    Build a graph snapshot from a source tree.
    """

    source = Path.cwd() / source

    nodes: dict[str, Node] = {}
    edges: set[Edge] = set()

    for file in iter_source_files(source):

        extractor = get_extractor(file)

        if not extractor:
            continue

        result = extractor.extract(file)

        for node in result.nodes:
            nodes[node.id] = node

        edges.update(result.edges)

        return GraphSnapshot(
            nodes=nodes,
            edges=list(edges),

            version=None,

            created_at=datetime.utcnow(),

            source_root=str(source)
        )

def iter_source_files(
    root: Path
):
    """
    Recursively find source files.
    """

    for file in root.rglob("*"):

        if not file.is_file():
            continue

        if file.suffix not in SUPPORTED_EXTENSIONS:
            continue

        yield file

def get_extractor(
    file: Path
):
    extractor_cls = SUPPORTED_EXTENSIONS.get(
        file.suffix
    )

    if not extractor_cls:
        return None

    return extractor_cls()


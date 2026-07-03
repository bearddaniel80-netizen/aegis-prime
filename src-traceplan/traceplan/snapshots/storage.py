from pathlib import Path
import json

from ..graph.models import (
    Node,
    Edge,
    GraphSnapshot
)


class SnapshotStorage:

    @staticmethod
    def save(
        snapshot: GraphSnapshot,
        path: str | Path
    ) -> None:

        path = Path.cwd() / path

        payload = {
            "metadata": snapshot.metadata,
            "nodes": [
                node.__dict__
                for node in snapshot.nodes.values()
            ],
            "edges": [
                edge.__dict__
                for edge in snapshot.edges
            ]
        }

        path.write_text(
            json.dumps(
                payload,
                indent=2
            ),
            encoding="utf-8"
        )

    @staticmethod
    def load(
        path: str | Path
    ) -> GraphSnapshot:

        path = Path.cwd() / path

        payload = json.loads(
            path.read_text(
                encoding="utf-8"
            )
        )

        nodes = {}

        for item in payload["nodes"]:

            node = Node(**item)

            nodes[node.id] = node

        edges = [
            Edge(**edge)
            for edge in payload["edges"]
        ]

        return GraphSnapshot(
            nodes=nodes,
            edges=edges,
            metadata=payload.get(
                "metadata",
                {}
            )
        )
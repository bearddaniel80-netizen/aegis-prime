import ast
import json
from ..models import (
    Node,
    Snapshot
)

def save_snapshot(snapshot, path):
    json.dump({
        "nodes": [n.__dict__ for n in snapshot.nodes],
        "edges": [e.__dict__ for e in snapshot.edges],
    }, open(path, "w"), indent=2)

def build_snapshot(path: str):
    nodes = set()
    edges = set()

    for file in iter_py_files(path):
        tree = ast.parse(open(file).read())

        module = file.replace("/", ".").replace(".py", "")

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_id = f"{module}.{node.name}"

                nodes.add(Node(
                    id=class_id,
                    name=node.name,
                    type="class",
                    file=file
                ))

            elif isinstance(node, ast.FunctionDef):
                func_id = f"{module}.{node.name}"

                nodes.add(Node(
                    id=func_id,
                    name=node.name,
                    type="function",
                    file=file
                ))

    return Snapshot(nodes=nodes, edges=edges)
    
def cmd_build(path, out):
    snapshot = build_snapshot(path)
    save_snapshot(snapshot, out)

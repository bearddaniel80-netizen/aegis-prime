import ast
import hashlib


def fingerprint_node(
    node: ast.AST
) -> str:

    payload = ast.dump(
        node,
        annotate_fields=True,
        include_attributes=False
    )

    return hashlib.sha256(
        payload.encode()
    ).hexdigest()
import ast


def get_name(node):

    if isinstance(node, ast.Name):
        return node.id

    if isinstance(node, ast.Attribute):
        return node.attr

    return None
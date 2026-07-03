from ..base import ASTNode

class StructValue(ASTNode):
    data: dict[str, Any]
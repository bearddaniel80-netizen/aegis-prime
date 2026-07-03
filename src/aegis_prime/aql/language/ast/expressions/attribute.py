from ..base import ASTNode
from .identifier import Field

class AttributeAccess(ASTNode):
    field: Field
    attr: str
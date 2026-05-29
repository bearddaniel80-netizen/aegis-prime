from enum import Enum
import operator

class BinaryOpType(str, Enum):
    EQ = "="
    LT = "<"
    GT = ">"

    def func(self):
        return {
            BinaryOpType.EQ: operator.eq,
            BinaryOpType.LT: operator.lt,
            BinaryOpType.GT: operator.gt,
        }[self]


class LogicalOpType(str, Enum):
    AND = "AND"
    OR = "OR"
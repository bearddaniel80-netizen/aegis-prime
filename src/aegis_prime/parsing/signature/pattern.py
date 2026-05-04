from aegis_prime.core.model_enums import PatternType
from aegis_prime.parsing.signature.ir import MessageAST, TokenType

class PatternExtractor:

    def extract(self, ast: MessageAST) -> PatternType:
        tokens = ast.tokens

        values = [t.value for t in tokens if t.type == TokenType.WORD]

        # Look for operators structurally
        for t in tokens:
            if t.value == "==":
                return PatternType.ASSERT_EQ
            if t.value == "!=":
                return PatternType.ASSERT_NE
            if t.value == "<":
                return PatternType.ASSERT_LT
            if t.value == ">":
                return PatternType.ASSERT_GT

        # "in" is semantic, not symbolic
        if "in" in values:
            return PatternType.ASSERT_IN

        return PatternType.OTHER
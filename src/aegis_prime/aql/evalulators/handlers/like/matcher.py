from aegis_prime.aql.language.ast.expressions.patterns.base import Pattern
from aegis_prime.aql.language.ast.expressions.patterns.charclass import CharClass
from aegis_prime.aql.language.ast.expressions.patterns.suffix import SingleChar
from aegis_prime.aql.language.ast.expressions.patterns.literals import Literal
from aegis_prime.aql.language.ast.expressions.patterns.wildcard import Wildcard
from .parser import parse_like_pattern

def match_like(text: str, pattern_nodes: list[Pattern]) -> bool:
    return _match_from(text, 0, pattern_nodes, 0)

def _match_from(text: str, ti: int, nodes: list[Pattern], ni: int) -> bool:
    while True:
        # pattern finished
        if ni == len(nodes):
            return ti == len(text)

        node = nodes[ni]

        # Literal match
        if isinstance(node, Literal):
            val = node.value
            if not text.startswith(val, ti):
                return False
            ti += len(val)
            ni += 1

        # Single char
        elif isinstance(node, SingleChar):
            if ti >= len(text):
                return False
            ti += 1
            ni += 1

        # Char class
        elif isinstance(node, CharClass):
            if ti >= len(text) or text[ti] not in node.chars:
                return False
            ti += 1
            ni += 1

        # Wildcard *
        elif isinstance(node, Wildcard):
            # Try all suffix matches (greedy with fallback)
            if ni + 1 == len(nodes):
                return True  # trailing * matches rest

            next_node = nodes[ni + 1]

            # Try to advance text until next node matches
            while ti <= len(text):
                if _match_from(text, ti, nodes, ni + 1):
                    return True
                ti += 1

            return False

        else:
            raise ValueError(f"Unknown node: {node}")

class LikeEvaluator:
    def __init__(self, pattern: str):
        self.pattern = pattern
        self.nodes = parse_like_pattern(pattern)

    def matches(self, text: str) -> bool:
        return match_like(text, self.nodes)
from .matcher import match_like
from aegis_prime.aql.language.ast.expressions.patterns.literals import Literal
from aegis_prime.aql.language.ast.expressions.patterns.wildcard import Wildcard

def optimize_pattern(nodes):
    # Single literal → substring search
    if len(nodes) == 1 and isinstance(nodes[0], Literal):
        return ("contains", nodes[0].value)

    # prefix
    if isinstance(nodes[0], Literal) and isinstance(nodes[-1], Wildcard):
        return ("prefix", nodes[0].value)

    # suffix
    if isinstance(nodes[-1], Literal) and isinstance(nodes[0], Wildcard):
        return ("suffix", nodes[-1].value)

    return ("full", nodes)

def fast_match(text, compiled):
    kind, value = compiled

    if kind == "contains":
        return value in text
    elif kind == "prefix":
        return text.startswith(value)
    elif kind == "suffix":
        return text.endswith(value)
    else:
        return match_like(text, value)
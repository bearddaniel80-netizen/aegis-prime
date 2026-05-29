from aegis_prime.aql.language.ast.expressions.patterns.base import Pattern
from aegis_prime.aql.language.ast.expressions.patterns.charclass import CharClass
from aegis_prime.aql.language.ast.expressions.patterns.suffix import SingleChar
from aegis_prime.aql.language.ast.expressions.patterns.literals import Literal
from aegis_prime.aql.language.ast.expressions.patterns.wildcard import Wildcard

def parse_like_pattern(pattern: str) -> list[Pattern]:
    nodes: List[Pattern] = []
    i = 0
    buffer = []

    def flush_literal():
        if buffer:
            nodes.append(Literal("".join(buffer)))
            buffer.clear()

    while i < len(pattern):
        c = pattern[i]

        if c == "\\":
            # escape next char
            i += 1
            if i < len(pattern):
                buffer.append(pattern[i])
        elif c == "*":
            flush_literal()
            nodes.append(Wildcard())
        elif c == "?":
            flush_literal()
            nodes.append(SingleChar())
        elif c == "[":
            flush_literal()
            i += 1
            char_set = set()

            while i < len(pattern) and pattern[i] != "]":
                if i + 2 < len(pattern) and pattern[i + 1] == "-":
                    # range
                    start = pattern[i]
                    end = pattern[i + 2]
                    for ch in range(ord(start), ord(end) + 1):
                        char_set.add(chr(ch))
                    i += 3
                else:
                    char_set.add(pattern[i])
                    i += 1

            nodes.append(CharClass(char_set))
        else:
            buffer.append(c)

        i += 1

    flush_literal()
    return nodes
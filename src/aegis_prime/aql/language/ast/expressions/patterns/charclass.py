from .base import Pattern

class CharClass(Pattern):
    def __init__(self, chars: set[str]):
        self.chars = chars

    def __repr__(self):
        # sort for stable/debug-friendly output
        chars_display = "".join(sorted(self.chars))
        return f"CharClass([{chars_display}])"

    def __eq__(self, other):
        return isinstance(other, CharClass) and self.chars == other.chars

    def __hash__(self):
        return hash((CharClass, frozenset(self.chars)))

    def to_dict(self):
        return {
            "type": "CharClass",
            "chars": sorted(self.chars)
        }

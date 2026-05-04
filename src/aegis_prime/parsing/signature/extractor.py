from dataclasses import dataclass
from typing import Optional


@dataclass
class Assertion:
    raw: str


class AssertionExtractor:

    def extract(self, text: str) -> Optional[Assertion]:
        lines = text.splitlines()

        # Priority 1: pytest rewritten assertion (the E line is richer)
        for line in lines:
            line = line.strip()
            if line.startswith("E") and "AssertionError" in line and "assert" in line:
                return Assertion(raw=self._clean(line))

        # Priority 2: original assert line (">       assert ...")
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("assert "):
                return Assertion(raw=stripped)

            if stripped.startswith(">") and "assert" in stripped:
                return Assertion(raw=self._clean(stripped))

        return None

    def _clean(self, line: str) -> str:
        # Remove pytest prefixes like "E       "
        line = line.lstrip("E").strip()

        # Remove leading ">"
        if line.startswith(">"):
            line = line[1:].strip()

        return line
        
from dataclasses import dataclass, field
from .severity import Severity

@dataclass
class AnalysisContext:

    #
    # Input
    #
    text: str = ""

    artifacts: dict = field(default_factory=dict)

    #
    # Analysis
    #

    @property
    def has_errors(self):

        return any(
            d.severity in (
                Severity.ERROR,
                Severity.FATAL,
                Severity.INTERNAL
            )
            for d in self.artifacts["diagnostics"].diagnostics
        )

    @property
    def has_fatal(self):

        return any(
            d.severity in (
                Severity.FATAL,
                Severity.INTERNAL
            )
            for d in self.artifacts["diagnostics"].diagnostics
        )

    #
    # Shared scratch space
    #

    metadata: dict = field(default_factory=dict)

    statistics: dict = field(default_factory=dict)

    def __repr__(self):
        return (
            f"AnalysisContext( text: {self.text})"
        )

    def to_dict(self):
        return {
            "type": "AnalysisContext",
            "text": self.text,
        }
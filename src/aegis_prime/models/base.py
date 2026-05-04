from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List

from aegis_prime.core.model_enums import ErrorType

@dataclass
class BaseCluster(ABC):
    error_type: ErrorType
    message: str
    files: List[str] = field(default_factory=list)
    line: int | None = None
    tests: List[str] = field(default_factory=list)
    stack_traces: List[str] = field(default_factory=list)

    @abstractmethod
    def signature(self) -> str:
        pass

    def add_test(self, test: str):
        if test not in self.tests:
            self.tests.append(test)

    def add_trace(self, trace: str):
        if trace not in self.stack_traces:
            self.stack_traces.append(trace)
from dataclasses import dataclass
from aegis_prime.models.base import BaseCluster

@dataclass
class FailureCluster(BaseCluster):

    def signature(self) -> str:
        return f"{self.error_type}:{self.message}"

    def to_dict(self):
        return {
            'error_type': self.error_type,
            'message': self.message,
            'files': self.files,
            'line': self.line,
            'tests': self.tests,
            'stack_traces': self.stack_traces,
        }
        
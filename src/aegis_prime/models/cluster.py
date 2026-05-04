from dataclasses import dataclass, field
from aegis_prime.models.base import BaseCluster
from aegis_prime.models.failure import FailureCluster
from aegis_prime.core.model_enums import Severity, Status
from aegis_prime.strategies.signature import SignatureStrategy, DefaultSignatureStrategy

@dataclass
class ClusterModel(BaseCluster):
    cluster_id: int = 0
    frequency: int = 1
    severity: Severity = Severity.LOW
    status: Status = Status.OPEN
    _signature: str = ""

    _signature_strategy: SignatureStrategy = field(
        default_factory=DefaultSignatureStrategy
    )

    def signature(self) -> str:
        self._signature = f"{self.error_type.value}:{self._signature_strategy.generate(self.message)}"
        return self._signature.replace(' ', '')

    @classmethod
    def from_failure(cls, cluster_id: int, failure: FailureCluster):
        return cls(
            cluster_id=cluster_id,
            error_type=failure.error_type,
            message=failure.message,
            files=[failure.files],  # or deepcopy if needed
            line=failure.line,
            tests=[failure.tests],
            stack_traces=[failure.stack_traces],
        )

    def to_dict(self):
        return {
            "cluster_id": self.cluster_id,
            "error_type": self.error_type.value,
            "message": self.message,
            "signature": self.signature(),
            "files": self.files,
            "line": self.line or 0,
            "tests": self.tests,
            "stack_traces": self.stack_traces,
            "frequency": self.frequency or 1,
            "status": self.status.value,
            "severity": self.severity.value,
        }

    def __hash__(self):
        return hash(self._signature)

    def __eq__(self, other):
        return isinstance(other, ClusterModel) and self._signature == other._signature

    def __add__(self, other):
        cluster_id = f'{self.cluster_id}:{other.cluster_id}'
        message = f'{self.message}, {other.message}'

        files = self.files + other.files
        tests = self.tests + other.tests
        stack_traces = self.stack_traces + other.stack_traces

        return ClusterModel(
            cluster_id=cluster_id,
            error_type=self.error_type,  # keep consistent
            message=message,
            files=files,
            line=0,
            tests=tests,
            stack_traces=stack_traces,
        )
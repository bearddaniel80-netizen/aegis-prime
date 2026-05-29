
from aegis_prime.core.model_enums import ErrorType, Severity, Status
from dataclasses import dataclass, field
from aegis_prime.models.base import BaseCluster
from aegis_prime.models.failure import FailureCluster
from aegis_prime.core.model_enums import Severity, Status
from aegis_prime.strategies.signature import SignatureStrategy, DefaultSignatureStrategy
from aegis_prime.core.model_registry import aegis_model
from aegis_prime.orm.model import Model
from aegis_prime.aql.adapter.dataset import Dataset
from aegis_prime.core.settings import CLUSTER
import json

@aegis_model("clusters")
@dataclass
class ClusterModel(BaseCluster, Model):
    cluster_id: int = 0
    frequency: int = 1
    severity: Severity = Severity.LOW
    status: Status = Status.OPEN
    _signature: str = ""

    _signature_strategy: SignatureStrategy = field(
        default_factory=DefaultSignatureStrategy
    )

    @classmethod
    def to_dataset(cls):
        rows = load_clusters()  # list[ClusterModel]
        return Dataset(rows, cls)

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
    
def load_clusters() -> list[ClusterModel]:
    with open(CLUSTER) as f:
        data = json.load(f)

    clusters = []
    for c in data:
        clusters.append(
            ClusterModel(
                cluster_id=c["cluster_id"],
                error_type=ErrorType(c["error_type"]),
                frequency=int(c["frequency"]),
                severity=Severity(c["severity"]),
                message=c["message"],
                tests=c["tests"],
                files=c["files"],
                stack_traces=c["stack_traces"],
            )
        )

    return clusters
    # -------- Projections ---------

# @aegis_model("hot_cluster")
# class HotCluster(ClusterModel):
#     __where__ = {"severity": "high"}
# 
# @aegis_model("cold_cluster")
# class ColdCluster(ClusterModel):
#     __where__ = {"severity": "low"}
#     __fields__ = ["cluster_id", "error_type"]
#     def __init__(self):
#         ColdCluster.all()
# 
# @aegis_model("first_hot_cluster")
# class FirstHotCluster(HotCluster):
#     __where__ = {"cluster_id": 1}
# 
# @aegis_model("first_cold_cluster")
# class FirstColdCluster(ColdCluster):
#     __where__ = {"cluster_id": 1}
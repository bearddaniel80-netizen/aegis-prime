
from aegis_prime.core.model_enums import ErrorType, Severity, Status
from dataclasses import dataclass
from aegis_prime.models.base import BaseCluster
from aegis_prime.orm.model import Model
from aegis_prime.core.model_registry import aegis_model
from aegis_prime.aql.adapter.dataset import Dataset
from aegis_prime.core.settings import PROD_LOG
import json

@aegis_model("failures")
@dataclass
class FailureCluster(BaseCluster, Model):

    def signature(self) -> str:
        return f"{self.error_type}:{self.message}"

    @classmethod
    def to_dataset(cls):
        rows = load_failures()
        return Dataset(rows, cls)

    def to_dict(self):
        return {
            'error_type': self.error_type,
            'message': self.message,
            'files': self.files,
            'line': self.line,
            'tests': self.tests,
            'stack_traces': self.stack_traces,
        }

def load_failures() -> list[FailureCluster]:
    with open(PROD_LOG) as f:
        data = json.load(f)

    failures = []
    for c in data:
        failures.append(
            FailureCluster(
                error_type=ErrorType(c["error_type"]),
                message=c["message"],
            )
        )

    return failures
        
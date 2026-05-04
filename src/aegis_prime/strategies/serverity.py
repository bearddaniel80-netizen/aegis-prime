from abc import ABC, abstractmethod

from aegis_prime.models.cluster import ClusterModel
from aegis_prime.core.model_enums import ErrorType, Severity

class SeverityStrategy(ABC):
    @abstractmethod
    def calculate(self, cluster: ClusterModel) -> Severity:
        pass


class DefaultSeverityStrategy(SeverityStrategy):

    def calculate(self, cluster: ClusterModel) -> Severity:
        score = 0

        if cluster.frequency > 5:
            score += 2
        elif cluster.frequency > 2:
            score += 1

        if len(cluster.tests) > 5:
            score += 2
        elif len(cluster.tests) > 2:
            score += 1

        if cluster.error_type == ErrorType.EXCEPTION:
            score += 3
        elif cluster.error_type in (ErrorType.TYPE, ErrorType.ATTRIBUTE):
            score += 2

        if score >= 5:
            return Severity.CRITICAL
        elif score >= 3:
            return Severity.HIGH
        elif score >= 1:
            return Severity.MEDIUM
        return Severity.LOW
from collections import defaultdict
from functools import reduce

from aegis_prime.models.cluster import ClusterModel
from aegis_prime.strategies.serverity import DefaultSeverityStrategy, SeverityStrategy

class ClusterMerger:

    def __init__(self, severity_strategy: SeverityStrategy | None = None):
        self.severity_strategy = severity_strategy or DefaultSeverityStrategy()

    def merge(self, clusters: list[ClusterModel]) -> list[ClusterModel]:
        grouped = defaultdict(list)
        
        for c in clusters:
            c.signature()
            grouped[c._signature].append(c)

        merged_clusters = []

        for key, group in grouped.items():

            if len(group) > 1:
                merged = reduce(lambda a, b: a + b, group)
                merged.severity = self.severity_strategy.calculate(merged)
                merged_clusters.append(merged)
            else:
                merged_clusters.append(group[0])

        return merged_clusters
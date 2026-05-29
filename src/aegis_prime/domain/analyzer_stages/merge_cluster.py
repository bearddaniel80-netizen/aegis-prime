from .base import Stage
from ..analyzer_registry import register_analyze_stage
from aegis_prime.services.merger import ClusterMerger

@register_analyze_stage(priority=7)
class MergeClusters(Stage):
    def run(self, data):
        cluster_merger = ClusterMerger()
        items = cluster_merger.merge(data)
        return items
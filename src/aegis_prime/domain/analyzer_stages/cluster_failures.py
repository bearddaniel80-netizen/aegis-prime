from .base import Stage
from ..analyzer_registry import register_analyze_stage
from aegis_prime.models.cluster import ClusterModel

@register_analyze_stage(priority=4)
class ClusterFailures(Stage):
    def run(self, data):    
        clusters = []
        for failure in data:
            clusters.append(ClusterModel.from_failure(cluster_id=len(clusters), failure=failure))
        return clusters
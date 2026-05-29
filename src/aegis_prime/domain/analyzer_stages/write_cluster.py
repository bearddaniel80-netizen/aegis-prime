from .base import Stage
from ..analyzer_registry import register_analyze_stage
from aegis_prime.models.cluster import ClusterModel
from aegis_prime.core.settings import CLUSTER
import json

@register_analyze_stage(priority=5)
class WriteClusters(Stage):
    def run(self, data):
        with open(CLUSTER, "w") as f:
            items = [item.to_dict() for item in data]
            json.dump(data, f, indent=4)
        return items
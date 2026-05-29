from .base import Stage
from ..analyzer_registry import register_analyze_stage
from aegis_prime.core.settings import MERGED_CLUSTER
import json

@register_analyze_stage(priority=8)
class WriteMergeClusters(Stage):
    def run(self, data):
        with open(MERGED_CLUSTER, "w") as f:
            items = [item.to_dict() for item in data]
            json.dump(items, f, indent=4)
        return items
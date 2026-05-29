from .base import Stage
from ..analyzer_registry import register_analyze_stage
from aegis_prime.core.settings import PROD_LOG
import json

@register_analyze_stage(priority=3)
class WriteFailures(Stage):
    def run(self, data):
        with open(PROD_LOG, "w") as f:
            failures = [failure.to_dict() for failure in data]
            json.dump(failures, f, indent=4)
        return failures
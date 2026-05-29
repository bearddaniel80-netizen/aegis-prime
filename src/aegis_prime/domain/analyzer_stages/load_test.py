from .base import Stage
from ..analyzer_registry import register_analyze_stage
from aegis_prime.core.settings import LAST_RUN
import json

@register_analyze_stage(priority=1)
class LoadTest(Stage):
    def run(self, data):
        try:
            with open(LAST_RUN, "r") as f:
                output = json.load(f)
        except FileNotFoundError:
            print("❌ No previous run found")
        return output
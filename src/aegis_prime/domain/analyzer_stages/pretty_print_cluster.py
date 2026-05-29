from .base import Stage
from ..analyzer_registry import register_analyze_stage
from aegis_prime.presentation.analyzer import pretty_print

@register_analyze_stage(priority=6)
class PrettyPrint(Stage):
    def run(self, data):
        pretty_print(data)
        return data
from .base import Stage
from ..analyzer_registry import register_analyze_stage
from aegis_prime.parsing.pytest_parser import parse_pytest_failures

@register_analyze_stage(priority=2)
class FilterTest(Stage):
    def run(self, data):
        return parse_pytest_failures(data)
from .analyzer_registry import ANALYZE_STAGE_REGISTRY
from . import analyzer_stages

def build_chain():
    """
    ------- Pipeline Order -------
    LoadTest -> FilterTest -> WriteFailures
    ClusterFailures -> WriteClusters -> PrettyPrint
    MergeClusters -> WriteMergeClusters
    ------- Pipeline Order -------
    """
    # sort by priority
    sorted_stages = sorted(ANALYZE_STAGE_REGISTRY, key=lambda x: x[0])

    instances = [cls() for _, cls in sorted_stages]

    for i in range(len(instances) - 1):
        instances[i].next = instances[i + 1]

    return instances[0] if instances else None

def analyze_results():
    data = None
    for link in build_chain():
        data = link.run(data)


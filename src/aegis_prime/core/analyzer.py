from aegis_prime.parsing.pytest_parser import parse_pytest_failures
from aegis_prime.core.clustering import cluster_failures
from aegis_prime.models.failure import FailureCluster
from aegis_prime.models.cluster import ClusterModel
from aegis_prime.services.merger import ClusterMerger
from aegis_prime.presentation.analyzer import pretty_print
from aegis_prime.core.settings import LAST_RUN, PROD_LOG, CLUSTER
import json

def analyze_results():
    """
    Analyze latest test run and produce failure clusters
    (public-facing simplified version)
    """

    try:
        with open(LAST_RUN, "r") as f:
            output = json.load(f)
    except FileNotFoundError:
        print("❌ No previous run found")
        return

    failures = parse_pytest_failures(output)

    with open(PROD_LOG, "w") as f:
        data = [failure.to_dict() for failure in failures]
        json.dump(data, f, indent=4)

    clusters = []
    for failure in failures:
        clusters.append(ClusterModel.from_failure(cluster_id=len(clusters), failure=failure))

    cluster_merger = ClusterMerger()
    items = cluster_merger.merge(clusters)

    with open(CLUSTER, "w") as f:
        data = [item.to_dict() for item in items]
        json.dump(data, f, indent=4)

    pretty_print(clusters)
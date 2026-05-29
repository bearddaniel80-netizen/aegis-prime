from typing import Dict, List, Any
from aegis_prime.data.loaders import load_clusters, load_failures
from aegis_prime.core.settings import CLUSTER, PROD_LOG

# registry.py (or similar)

MODEL_REGISTRY = {}

def register_model(name: str, model_cls: type):
    """
    Register a model under a logical AQL name.
    """
    MODEL_REGISTRY[name] = model_cls


def resolve_target(identifier):
    """
    Resolve an Identifier node into a concrete model class.
    """

    # If Identifier wraps a string like Identifier("clusters")
    name = identifier.value if hasattr(identifier, "value") else str(identifier)

    try:
        return MODEL_REGISTRY[name]
    except KeyError:
        raise ValueError(f"Unknown target: {name}. Available: {list(MODEL_REGISTRY.keys())}")

def load_tables(path_prefix: str = ".") -> Dict[str, List[Any]]:
    return {
        "clusters": load_clusters(CLUSTER),
        "failures": load_failures(PROD_LOG),
    }
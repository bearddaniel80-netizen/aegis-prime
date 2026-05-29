from aegis_prime.presentation.explain import pretty_print
from aegis_prime.core.settings import CLUSTER
import json

def explain_latest_group(verbose: bool = False):
    """
    Explain most recent failure group (public UX version)
    """

    try:
        with open(CLUSTER, "r") as f:
            clusters = json.load(f)
    except FileNotFoundError:
        print("❌ Run 'aegis analyze' first")
        return

    pretty_print(clusters)

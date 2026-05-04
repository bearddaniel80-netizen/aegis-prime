from difflib import SequenceMatcher


def extract_error_signature(line: str) -> str:
    """
    Normalize error messages into comparable signatures
    """
    for e in ['AssertionError', 'Timeout']:
        if e in line:
            return e
    if "500" in line:
        return "ServerError"
    if "401" in line:
        return "Unauthorized"
    return 'error'


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def cluster_failures(failures, threshold: float = 0.6):
    """
    Group similar failures into clusters for analysis
    """

    clusters = []
    used = set()

    for i, f1 in enumerate(failures):
        if i in used:
            continue

        group = [f1]
        used.add(i)

        sig1 = extract_error_signature(f1)

        for j, f2 in enumerate(failures):
            if j in used:
                continue

            sig2 = extract_error_signature(f2)

            if similarity(sig1, sig2) > threshold:
                group.append(f2)
                used.add(j)

        clusters.append(group)

    return clusters
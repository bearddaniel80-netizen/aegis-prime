
def detect_root_cause_from_logs(log):
    text = log["message"].lower()

    if "connection refused" in text:
        return "Database connection failure"

    if "timeout" in text:
        return "Service latency or timeout issue"

    if "nullpointer" in text:
        return "Unhandled null exception"

    if "assert" in text:
        return "Bad test"

    return "Unknown backend issue"
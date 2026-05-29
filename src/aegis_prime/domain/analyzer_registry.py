ANALYZE_STAGE_REGISTRY = []

def register_analyze_stage(priority=100):
    def decorator(cls):
        ANALYZE_STAGE_REGISTRY.append((priority, cls))
        return cls
    return decorator
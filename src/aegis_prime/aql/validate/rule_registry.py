RULES = {
    "select": [],
    "where": []
}

def register_rule(stages, order=100):

    def decorator(cls):

        for stage in stages:
            RULES.setdefault(stage, []).append(
                (order, cls())
            )

        return cls

    return decorator
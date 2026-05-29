FUNCTION_CALL_REGISTRY = {}

def register_function_call(name):
    def decorator(cls):
        FUNCTION_CALL_REGISTRY[name] = cls
        return cls
    return decorator
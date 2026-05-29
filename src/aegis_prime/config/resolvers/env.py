import os
import re

ENV_PATTERN = re.compile(r"\$\{(.+?)\}")


def resolve_env_vars(obj):
    if isinstance(obj, dict):
        return {k: resolve_env_vars(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return [resolve_env_vars(v) for v in obj]

    if isinstance(obj, str):
        def replace(match):
            key = match.group(1)
            return os.getenv(key, "")

        return ENV_PATTERN.sub(replace, obj)

    return obj
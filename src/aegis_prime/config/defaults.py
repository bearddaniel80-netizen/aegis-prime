"""
aegis_prime/config/defaults.py

Default configuration values and helper utilities.
"""

from copy import deepcopy


DEFAULT_CONFIG = {
    "version": "1.0",

    "source": {
        "type": "stdin",
    },

    "format": {
        "type": "json",
        "infer_types": True,
        "strict": False,
    },

    "transform": {
        "flatten": False,
        "explode_arrays": False,
        "cast_types": True,
        "normalize_keys": True,
    },

    "optimize": {
        "enabled": True,
        "level": "balanced",

        "pushdown_filters": True,
        "projection_pruning": True,

        # None means auto-detect
        "memory_limit_mb": None,
    },

    "output": {
        "type": "stdout",
        "format": "table",
        "mode": "overwrite",
    },

    "secrets": {
        "provider": "env",
        "mappings": {},
    },
}


def get_default_config() -> dict:
    """
    Return a deep copy of the default config.

    Prevents accidental mutation of global defaults.
    """

    return deepcopy(DEFAULT_CONFIG)


def merge_defaults(config: dict) -> dict:
    """
    Merge user config with defaults recursively.

    User values always override defaults.
    """

    merged = deepcopy(DEFAULT_CONFIG)

    return deep_merge(merged, config)


def deep_merge(base: dict, override: dict) -> dict:
    """
    Recursively merge dictionaries.

    Example:
        base = {
            "format": {
                "type": "json",
                "strict": False
            }
        }

        override = {
            "format": {
                "strict": True
            }
        }

    Result:
        {
            "format": {
                "type": "json",
                "strict": True
            }
        }
    """

    for key, value in override.items():

        if (
            key in base
            and isinstance(base[key], dict)
            and isinstance(value, dict)
        ):
            base[key] = deep_merge(base[key], value)

        else:
            base[key] = value

    return base


def apply_runtime_defaults(config):
    """
    Apply runtime/computed defaults.

    This should be called AFTER parsing and validation.

    Example use cases:
    - auto memory limits
    - inferred output formats
    - source-specific defaults
    """

    # Example:
    optimize = getattr(config, "optimize", None)

    if optimize:
        if optimize.memory_limit_mb is None:
            optimize.memory_limit_mb = 512

    return config
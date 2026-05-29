"""
aegis_prime/config/resolvers/source.py

Source resolution layer (plugin-driven).

Responsibilities:
- Normalize source configuration
- Resolve runtime source adapters via plugin entrypoints
- Attach capability metadata for planner/optimizer
- Apply source-specific defaults

This layer should NOT:
- Execute queries
- Parse AQL
- Perform planning or optimization
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Dict, Any, Callable

from aegis_prime.config.errors import ConfigError

# =========================================================
# PLUGIN LOADER (ENTRYPOINT SYSTEM)
# =========================================================

def load_source_plugins() -> dict[str, Callable]:
    """
    Loads source factories from installed entrypoints.

    Expected entrypoint group:
        aegis_prime.sources
    """

    try:
        from importlib.metadata import entry_points
    except Exception as exc:
        raise ConfigError(f"EntryPoint system unavailable: {exc}") from exc

    factories: dict[str, Callable] = {}

    eps = entry_points()

    # Python 3.10+ style
    group = eps.select(group="aegis_prime.sources") if hasattr(eps, "select") else eps.get("aegis_prime.sources", [])

    for ep in group:
        try:
            factories[ep.name] = ep.load()
        except Exception as exc:
            raise ConfigError(
                f"Failed loading source plugin '{ep.name}': {exc}"
            ) from exc

    return factories


# =========================================================
# RESOLVER ENTRYPOINT
# =========================================================

def resolve_source(config) -> ResolvedSource:
    """
    Resolve config → runtime source via plugin entrypoints.
    """

    source = getattr(config, "source", None)

    if source is None:
        raise ConfigError("Missing source configuration")

    source_type = getattr(source, "type", None)

    if not source_type:
        raise ConfigError("Source type is not specified")

    factories = load_source_plugins()

    factory = factories.get(source_type)

    if factory is None:
        raise ConfigError(
            f"Unsupported source type: {source_type}. "
            f"Available: {list(factories.keys())}"
        )

    try:
        return factory(config)
    except Exception as exc:
        raise ConfigError(
            f"Source plugin '{source_type}' failed: {exc}"
        ) from exc
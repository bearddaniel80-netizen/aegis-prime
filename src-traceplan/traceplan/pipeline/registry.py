from dataclasses import dataclass
from typing import Type
from collections import defaultdict

STRATEGIES = {}
RENDERERS = defaultdict(dict)

@dataclass(slots=True)
class StrategyRegistration:

    name: str

    cls: Type

    aliases: list[str]

    version: str

    description: str

    priority: int

    capabilities: list[str]

def strategy(
    name: str,
    aliases: list[str] | None = None,
    version: str = "1.0",
    description: str = "",
    priority: int = 100,
    capabilities: list[str] | None = None
):
    """
    Registers a pipeline strategy.

    Example:

    @strategy(
        "analyze",
        aliases=["inspect"],
        description="Analyze a graph node"
    )
    class AnalyzeStrategy(...):
        ...
    """

    aliases = aliases or []

    def wrapper(cls):

        registration = StrategyRegistration(
            name=name,
            cls=cls,
            aliases=aliases,
            version=version,
            description=description,
            priority=priority
        )

        #
        # Primary name
        #

        STRATEGIES[name] = registration

        #
        # Aliases
        #

        for alias in aliases:

            STRATEGIES[alias] = registration

        return cls

    return wrapper

def renderer(name, format):
    def wrapper(cls):
        RENDERERS[name][_format] = cls
        return cls
    return wrapper

def get(command, _format):
    strategy_cls = STRATEGIES[command]
    renderer_cls = RENDERERS[command][_format]

    return strategy_cls, renderer_cls
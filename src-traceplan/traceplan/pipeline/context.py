from dataclasses import dataclass, field
from typing import Any

@dataclass
class PipelineContext:

    # -------------------------
    # Generic input payload
    # -------------------------
    data: Any = None

    # -------------------------
    # Graph inputs
    # -------------------------
    snapshot: Any = None

    old_snapshot: Any = None
    new_snapshot: Any = None

    # -------------------------
    # Target selection
    # -------------------------
    node_id: str | None = None

    symbol: str | None = None

    file_path: str | None = None

    # -------------------------
    # Execution metadata
    # -------------------------
    config: dict = field(
        default_factory=dict
    )

    env: dict = field(
        default_factory=dict
    )

    # -------------------------
    # Runtime tracking
    # -------------------------
    trace_id: str | None = None

    command: str | None = None

    artifacts: dict[str, Any] = field(
        default_factory=dict
    )

def analyze_context(
    snapshot,
    node_id: str,
    config: dict | None = None
) -> PipelineContext:

    return PipelineContext(
        snapshot=snapshot,
        node_id=node_id,
        config=config or {},
        command="analyze"
    )

def diff_context(
    old_snapshot,
    new_snapshot
) -> PipelineContext:

    return PipelineContext(
        old_snapshot=old_snapshot,
        new_snapshot=new_snapshot,
        command="diff"
    )

def build_context(
    path: str,
    config: dict | None = None
) -> PipelineContext:

    return PipelineContext(
        data=path,
        config=config or {},
        command="build"
    )


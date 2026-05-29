from dataclasses import dataclass
from typing import Optional


@dataclass
class OptimizeConfig:
    input_mode: Optional[str] = None  # streaming | batch

    pushdown_filters: Optional[bool] = True
    projection_pruning: Optional[bool] = True

    memory_limit_mb: Optional[int] = None
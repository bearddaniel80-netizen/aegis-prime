from dataclasses import dataclass
from typing import Optional


@dataclass
class QueryConfig:
    default: Optional[str] = None
    timeout: Optional[str] = None
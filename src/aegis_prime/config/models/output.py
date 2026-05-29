from dataclasses import dataclass
from typing import Optional


@dataclass
class OutputConfig:
    type: str = "stdout"  # stdout | file | postgres

    path: Optional[str] = None
    format: Optional[str] = "table"

    mode: Optional[str] = "overwrite"  # append | overwrite
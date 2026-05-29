from dataclasses import dataclass
from typing import Optional


@dataclass
class FormatConfig:
    type: str  # json | csv | xml | log | auto

    # CSV
    delimiter: Optional[str] = ","
    header: Optional[bool] = True

    # Log parsing
    pattern: Optional[str] = None

    # Schema / DDL
    ddl: Optional[str] = None
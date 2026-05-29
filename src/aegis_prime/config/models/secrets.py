from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class SecretsConfig:
    provider: Optional[str] = None  # env | aws | vault

    mappings: Optional[Dict[str, str]] = None
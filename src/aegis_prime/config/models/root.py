from dataclasses import dataclass
from typing import Optional

from .source import SourceConfig
from .format import FormatConfig
from .transform import TransformConfig
from .optimize import OptimizeConfig
from .output import OutputConfig
from .secrets import SecretsConfig


@dataclass
class AegisConfig:
    version: str = "1.0"

    source: SourceConfig = None
    format: Optional[FormatConfig] = None
    transform: Optional[TransformConfig] = None
    optimize: Optional[OptimizeConfig] = None
    output: Optional[OutputConfig] = None
    secrets: Optional[SecretsConfig] = None
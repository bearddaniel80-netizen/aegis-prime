from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TransformConfig:
    flatten: Optional[bool] = False
    explode_arrays: Optional[bool] = False

    cast_types: Optional[bool] = True
    normalize_keys: Optional[bool] = True

    # future: computed fields
    projections: Optional[List[str]] = None
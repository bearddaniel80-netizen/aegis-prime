from dataclasses import dataclass
from typing import Optional, Any

from .loader import load_config

@dataclass
class CLIOverrides:
    source: Optional[str] = None
    format: Optional[str] = None
    ddl: Optional[str] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    debug: Optional[bool] = None
    profile: Optional[str] = None

# def query(
#     q: str,
#     source: str = None,
#     format: str = None,
#     limit: int = None,
#     offset: int = None,
#     debug: bool = None,
#     profile: str = None,
# ):
#     config = load_config("aegis.toml")
# 
#     cli = CLIOverrides(
#         source=source,
#         format=format,
#         limit=limit,
#         offset=offset,
#         debug=debug,
#         profile=profile,
#     )
# 
#     ctx = ConfigResolver(config, cli).resolve()
# 
#     print(engine.run(q, ctx))
from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class ConnectionConfig:
    uri: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None
    database: Optional[str] = None
    user: Optional[str] = None
    password: Optional[str] = None


@dataclass
class SourceConfig:
    type: str  # stdin | file | postgres | mongo | etc.

    connection: Optional[ConnectionConfig] = None

    # file-specific
    path: Optional[str] = None
    recursive: Optional[bool] = False

    # http-specific
    url: Optional[str] = None
    method: Optional[str] = "GET"
    headers: Optional[Dict[str, str]] = None
from dataclasses import dataclass

@dataclass
class Symbol:
    name: str
    fqdn: str
    _type: str
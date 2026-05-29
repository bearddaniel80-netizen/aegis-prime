import tomllib

# ----------- Config Builder -------------
from .models.root import AegisConfig

def load_config(path: str) -> AegisConfig:
    with open(path, "rb") as f:
        data = tomllib.load(f)

    # TODO: map dict → dataclasses (use dacite or manual)
    return data

# ----------- Config Context ---------------
from dataclasses import dataclass
@dataclass
class Config:
    engine: dict
    sources: dict
    query: dict
    debug: dict
    profiles: dict

def load_config_context(path: str) -> Config:
    try:
        with open(path, "rb") as f:
            raw = tomllib.load(f)
    except FileNotFoundError:
        print("❌ No config file found")

    return Config(
        engine=raw.get("engine", {}),
        sources=raw.get("sources", {}),
        query=raw.get("query", {}),
        debug=raw.get("debug", {}),
        profiles=raw.get("profiles", {}),
    )
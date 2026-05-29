from .errors import ConfigError


def validate_config(cfg):
    if not cfg.source:
        raise ConfigError("Missing [source] section")

    if cfg.source.type == "file" and not cfg.source.path:
        raise ConfigError("File source requires 'path'")

    if cfg.source.type == "postgres" and not cfg.source.connection:
        raise ConfigError("Postgres requires connection config")
from .cli_merge import CLIOverrides
from aegis_prime.aql.engine.config_context import ConfigContext
from .loader import Config

class ConfigResolver:
    def __init__(self, config: Config, cli: CLIOverrides):
        self.config = config
        self.cli = cli

    def resolve(self) -> ConfigContext:
        profile_data = self._resolve_profile()

        source = self.cli.source or self._default_source(profile_data)
        source_cfg = self.config.sources.get(source, {})

        format_ = (
            self.cli.format
            or source_cfg.get("format")
            or "auto"
        )

        return ConfigContext(
            source=source,
            format=format_,
            ddl=self.cli.ddl,
            limit=self.cli.limit or profile_data.get("limit", 100),
            offset=self.cli.offset or profile_data.get("offset", 0),
            debug=self.cli.debug if self.cli.debug is not None else profile_data.get("debug", False),
            profile=self.cli.profile,
            extras={
                "source_cfg": source_cfg,
                "engine_cfg": self.config.engine,
            },
        )

    def _resolve_profile(self):
        if self.cli.profile:
            return self.config.profiles.get(self.cli.profile, {})

        return {}
    
    def _default_source(self, profile):
        return profile.get("source", "stdin")
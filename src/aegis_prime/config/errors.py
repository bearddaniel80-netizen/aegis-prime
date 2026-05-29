class ConfigError(Exception):
    """Base config exception."""


class ConfigValidationError(ConfigError):
    """Raised when config validation fails."""


class ConfigLoadError(ConfigError):
    """Raised when config loading fails."""


class ConfigWriteError(ConfigError):
    """Raised when config writing fails."""


class PromptAbortError(ConfigError):
    """Raised when interactive prompt flow is aborted."""
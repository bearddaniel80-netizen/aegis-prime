"""
aegis_prime/config/validator.py

Validation logic for Aegis configuration.

Responsibilities:
- structural validation
- semantic validation
- source-specific validation
- output validation
- optimization validation

This layer should NOT:
- load files
- resolve environment variables
- execute queries
"""

from pathlib import Path

from .errors import (
    ConfigValidationError,
)


SUPPORTED_SOURCES = {
    "stdin",
    "file",
    "postgres",
    "mongo",
    "neo4j",
    "http",
}


SUPPORTED_FORMATS = {
    "json",
    "csv",
    "xml",
    "log",
    "parquet",
    "auto",
}


SUPPORTED_OUTPUTS = {
    "stdout",
    "file",
}


SUPPORTED_OPTIMIZATION_LEVELS = {
    "minimal",
    "balanced",
    "aggressive",
}


def validate_config(config):
    """
    Main validation entrypoint.

    Raises:
        ConfigValidationError
    """

    if config is None:
        raise ConfigValidationError(
            "Config object cannot be None"
        )

    validate_source(config)
    validate_format(config)
    validate_transform(config)
    validate_optimize(config)
    validate_output(config)
    validate_secrets(config)

    return True


# =========================================================
# SOURCE VALIDATION
# =========================================================

def validate_source(config):

    source = getattr(config, "source", None)

    if source is None:
        raise ConfigValidationError(
            "Missing required [source] section"
        )

    if not source.type:
        raise ConfigValidationError(
            "source.type is required"
        )

    if source.type not in SUPPORTED_SOURCES:
        raise ConfigValidationError(
            f"Unsupported source type: {source.type}"
        )

    if source.type == "file":
        validate_file_source(source)

    elif source.type == "postgres":
        validate_postgres_source(source)

    elif source.type == "http":
        validate_http_source(source)


def validate_file_source(source):

    if not source.path:
        raise ConfigValidationError(
            "File source requires 'path'"
        )

    path = Path(source.path)

    if not path.exists():
        raise ConfigValidationError(
            f"File does not exist: {source.path}"
        )


def validate_postgres_source(source):

    if source.connection is None:
        raise ConfigValidationError(
            "Postgres source requires connection config"
        )

    conn = source.connection

    if not conn.uri:
        raise ConfigValidationError(
            "Postgres source requires connection.uri"
        )


def validate_http_source(source):

    if not source.url:
        raise ConfigValidationError(
            "HTTP source requires url"
        )

    if source.method not in {
        "GET",
        "POST",
        "PUT",
        "DELETE",
    }:
        raise ConfigValidationError(
            f"Unsupported HTTP method: {source.method}"
        )


# =========================================================
# FORMAT VALIDATION
# =========================================================

def validate_format(config):

    fmt = getattr(config, "format", None)

    if fmt is None:
        return

    if fmt.type not in SUPPORTED_FORMATS:
        raise ConfigValidationError(
            f"Unsupported format type: {fmt.type}"
        )

    if fmt.type == "csv":
        validate_csv_format(fmt)

    if fmt.type == "log":
        validate_log_format(fmt)


def validate_csv_format(fmt):

    if fmt.delimiter is not None:
        if len(fmt.delimiter) != 1:
            raise ConfigValidationError(
                "CSV delimiter must be one character"
            )


def validate_log_format(fmt):

    if fmt.pattern is not None:
        if not isinstance(fmt.pattern, str):
            raise ConfigValidationError(
                "Log pattern must be string"
            )


# =========================================================
# TRANSFORM VALIDATION
# =========================================================

def validate_transform(config):

    transform = getattr(config, "transform", None)

    if transform is None:
        return

    if (
        transform.flatten
        and transform.explode_arrays
    ):
        raise ConfigValidationError(
            "flatten and explode_arrays "
            "cannot both be enabled"
        )


# =========================================================
# OPTIMIZATION VALIDATION
# =========================================================

def validate_optimize(config):

    optimize = getattr(config, "optimize", None)

    if optimize is None:
        return

    if (
        optimize.level
        not in SUPPORTED_OPTIMIZATION_LEVELS
    ):
        raise ConfigValidationError(
            "Invalid optimization level: "
            f"{optimize.level}"
        )

    if (
        optimize.memory_limit_mb is not None
        and optimize.memory_limit_mb <= 0
    ):
        raise ConfigValidationError(
            "memory_limit_mb must be > 0"
        )


# =========================================================
# OUTPUT VALIDATION
# =========================================================

def validate_output(config):

    output = getattr(config, "output", None)

    if output is None:
        return

    if output.type not in SUPPORTED_OUTPUTS:
        raise ConfigValidationError(
            f"Unsupported output type: {output.type}"
        )

    if output.type == "file":
        validate_file_output(output)


def validate_file_output(output):

    if not output.path:
        raise ConfigValidationError(
            "File output requires path"
        )


# =========================================================
# SECRETS VALIDATION
# =========================================================

def validate_secrets(config):

    secrets = getattr(config, "secrets", None)

    if secrets is None:
        return

    supported = {
        "env",
        "aws",
        "vault",
        None,
    }

    if secrets.provider not in supported:
        raise ConfigValidationError(
            f"Unsupported secrets provider: "
            f"{secrets.provider}"
        )
"""
aegis_prime/config/resolvers/secrets.py

Secret resolution layer.

Responsibilities:
- resolve secrets from providers
- inject runtime credentials
- normalize secret access

This layer should NOT:
- validate config structure
- execute queries
- mutate raw config files
"""

import os

from aegis_prime.config.errors import ConfigError


SUPPORTED_SECRET_PROVIDERS = {
    "env",
    "aws",
    "vault",
    None,
}


def resolve_secrets(config):
    """
    Main secret resolution entrypoint.

    Returns:
        updated config object
    """

    secrets_cfg = getattr(config, "secrets", None)

    if secrets_cfg is None:
        return config

    provider = secrets_cfg.provider

    if provider not in SUPPORTED_SECRET_PROVIDERS:
        raise ConfigError(
            f"Unsupported secrets provider: {provider}"
        )

    if provider in (None, "env"):
        return resolve_env_secrets(config)

    if provider == "aws":
        return resolve_aws_secrets(config)

    if provider == "vault":
        return resolve_vault_secrets(config)

    return config


# =========================================================
# ENV PROVIDER
# =========================================================

def resolve_env_secrets(config):
    """
    Resolve secrets from environment variables.

    Example:
        password = "${DB_PASSWORD}"

    OR via mappings:
        [secrets.mappings]
        password = "DB_PASSWORD"
    """

    mappings = {}

    if config.secrets:
        mappings = config.secrets.mappings or {}

    source = getattr(config, "source", None)

    if source is None:
        return config

    connection = getattr(source, "connection", None)

    if connection is None:
        return config

    # -----------------------------------------------------
    # password mapping
    # -----------------------------------------------------

    if not connection.password:

        env_key = mappings.get("password")

        if env_key:
            connection.password = os.getenv(env_key)

    else:
        connection.password = interpolate_env(
            connection.password
        )

    # -----------------------------------------------------
    # username interpolation
    # -----------------------------------------------------

    if connection.user:
        connection.user = interpolate_env(
            connection.user
        )

    # -----------------------------------------------------
    # uri interpolation
    # -----------------------------------------------------

    if connection.uri:
        connection.uri = interpolate_env(
            connection.uri
        )

    return config


# =========================================================
# AWS SECRETS MANAGER
# =========================================================

def resolve_aws_secrets(config):
    """
    Placeholder for AWS Secrets Manager integration.

    Future:
        boto3.client("secretsmanager")
    """

    raise NotImplementedError(
        "AWS secrets provider not implemented yet"
    )


# =========================================================
# HASHICORP VAULT
# =========================================================

def resolve_vault_secrets(config):
    """
    Placeholder for Vault integration.
    """

    raise NotImplementedError(
        "Vault secrets provider not implemented yet"
    )


# =========================================================
# UTILITIES
# =========================================================

def interpolate_env(value: str):
    """
    Resolve ${ENV_VAR} placeholders.

    Example:
        postgres://${DB_USER}:${DB_PASS}@localhost/db
    """

    if not isinstance(value, str):
        return value

    import re

    pattern = re.compile(r"\$\{(.+?)\}")

    def replace(match):
        key = match.group(1)

        env_value = os.getenv(key)

        if env_value is None:
            raise ConfigError(
                f"Missing environment variable: {key}"
            )

        return env_value

    return pattern.sub(replace, value)
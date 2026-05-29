"""
aegis_prime/config/builder/cli.py

Interactive config builder CLI.

Responsibilities:
- run builder prompt flow
- generate config structure
- validate config
- write TOML output

This layer should NOT:
- execute queries
- optimize plans
- resolve runtime sources
"""

from pathlib import Path

from aegis_prime.config.errors import (
    ConfigError,
    ConfigValidationError,
    PromptAbortError,
)

from aegis_prime.config.validator import (
    validate_config,
)

from aegis_prime.config.builder.prompts import (
    run_builder,
)

from aegis_prime.config.builder.generator import (
    build_config_dict,
)

from aegis_prime.config.builder.writer import (
    write_toml,
)

from aegis_prime.config.defaults import (
    merge_defaults,
)

from aegis_prime.config.loader import (
    parse_config_dict,
)


# =========================================================
# MAIN ENTRYPOINT
# =========================================================

def build_config_cli(
    output_path: str = "./aegis.toml",
):
    """
    Main interactive config builder command.

    Example:
        aegis config build
    """

    try:

        print_banner()

        # -------------------------------------------------
        # prompt flow
        # -------------------------------------------------

        answers = run_builder()

        # -------------------------------------------------
        # generate config dict
        # -------------------------------------------------

        raw_config = build_config_dict(
            answers
        )

        # -------------------------------------------------
        # merge defaults
        # -------------------------------------------------

        merged_config = merge_defaults(
            raw_config
        )

        # -------------------------------------------------
        # parse → typed models
        # -------------------------------------------------

        parsed_config = parse_config_dict(
            merged_config
        )

        # -------------------------------------------------
        # validate
        # -------------------------------------------------

        validate_config(parsed_config)

        # -------------------------------------------------
        # preview
        # -------------------------------------------------

        preview_config(merged_config)

        confirm = input(
            "\nSave config? [Y/n]: "
        ).strip().lower()

        if confirm == "n":
            raise PromptAbortError(
                "Config creation aborted"
            )

        # -------------------------------------------------
        # write file
        # -------------------------------------------------

        write_toml(
            merged_config,
            output_path,
        )

        print_success(output_path)

    except KeyboardInterrupt:
        print(
            "\n\n❌ Builder cancelled"
        )

    except PromptAbortError as e:
        print(
            f"\n⚠ {e}"
        )

    except ConfigValidationError as e:
        print(
            f"\n❌ Validation Error:\n{e}"
        )

    except ConfigError as e:
        print(
            f"\n❌ Config Error:\n{e}"
        )

    except Exception as e:
        print(
            f"\n❌ Unexpected Error:\n{e}"
        )


# =========================================================
# PREVIEW
# =========================================================

def preview_config(config: dict):
    """
    Print generated config preview.
    """

    print("\n📄 Generated Config\n")

    try:
        import tomli_w

        toml_str = tomli_w.dumps(config)

        print(toml_str)

    except Exception:
        print(config)


# =========================================================
# BANNER
# =========================================================

def print_banner():

    print(
        "\n"
        "🛠  Aegis Config Builder\n"
    )


# =========================================================
# SUCCESS
# =========================================================

def print_success(path: str):

    resolved = Path(path).resolve()

    print(
        "\n✅ Config created successfully"
    )

    print(
        f"\nSaved to:\n{resolved}"
    )

    print(
        "\nNext step:"
    )

    print(
        f'  aegis query --config "{path}" '
        '"SELECT * FROM stdin"'
    )


# =========================================================
# OPTIONAL:
# NON-INTERACTIVE ENTRYPOINT
# =========================================================

def build_config_from_dict(
    data: dict,
    output_path: str = "./aegis.toml",
):
    """
    Non-interactive config generation.

    Useful for:
    - tests
    - templates
    - CI/CD
    - future API support
    """

    merged = merge_defaults(data)

    parsed = parse_config_dict(merged)

    validate_config(parsed)

    write_toml(
        merged,
        output_path,
    )

    return output_path
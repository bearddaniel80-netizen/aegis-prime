from .prompts import BuilderAnswers

def remove_none(obj):
    """
    Recursively remove None values.
    """

    if isinstance(obj, dict):
        return {
            k: remove_none(v)
            for k, v in obj.items()
            if v is not None
        }

    if isinstance(obj, list):
        return [
            remove_none(v)
            for v in obj
            if v is not None
        ]

    return obj
def build_output(
    answers: BuilderAnswers,
) -> dict:

    output = {
        "type": answers.output_type,
    }

    if answers.output_type == "file":
        output["path"] = answers.output_path

    return output
def build_optimize(
    answers: BuilderAnswers,
) -> dict:

    return {
        "enabled": answers.optimize_enabled,
        "level": answers.optimize_level,
    }
def build_format(
    answers: BuilderAnswers,
) -> dict:

    format_cfg = {
        "type": answers.format_type,
    }

    if answers.ddl:
        format_cfg["ddl"] = answers.ddl

    return format_cfg
def build_source(
    answers: BuilderAnswers,
) -> dict:

    source = {
        "type": answers.source_type,
    }

    if answers.source_type == "file":
        source["path"] = answers.file_path

    elif answers.source_type == "postgres":
        source["connection"] = {
            "uri": answers.postgres_uri,
        }

    return source
def build_config_dict(
    answers: BuilderAnswers,
) -> dict:
    """
    Convert builder answers into TOML-ready dict.
    """

    config = {
        "version": "1.0",
    }

    config["source"] = build_source(answers)
    config["format"] = build_format(answers)
    config["optimize"] = build_optimize(answers)
    config["output"] = build_output(answers)

    return remove_none(config)
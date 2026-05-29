from dataclasses import dataclass
from typing import Optional


@dataclass
class BuilderAnswers:
    config_name: Optional[str] = None

    source_type: Optional[str] = None

    # file
    file_path: Optional[str] = None

    # postgres
    postgres_uri: Optional[str] = None

    # format
    format_type: Optional[str] = None
    ddl: Optional[str] = None

    # optimize
    optimize_enabled: bool = True
    optimize_level: str = "balanced"

    # output
    output_type: str = "stdout"
    output_path: Optional[str] = None

def prompt_output(answers: BuilderAnswers):
    print("\n📤 Output")
    print("1. stdout")
    print("2. file")

    choice = input("> ").strip()

    mapping = {
        "1": "stdout",
        "2": "file",
    }

    answers.output_type = mapping.get(choice, "stdout")

    if answers.output_type == "file":
        answers.output_path = input(
            "Output path: "
        ).strip()

def prompt_optimize(answers: BuilderAnswers):
    print("\n⚡ Optimization")

    enabled = input(
        "Enable optimization? [Y/n]: "
    ).strip().lower()

    answers.optimize_enabled = enabled != "n"

    if answers.optimize_enabled:
        level = input(
            "Optimization level [balanced]: "
        ).strip()

        answers.optimize_level = level or "balanced"

def prompt_format(answers: BuilderAnswers):
    print("\n🧩 Format")
    print("1. json")
    print("2. csv")
    print("3. xml")
    print("4. log")

    choice = input("> ").strip()

    mapping = {
        "1": "json",
        "2": "csv",
        "3": "xml",
        "4": "log",
    }

    answers.format_type = mapping.get(choice)

    if answers.format_type == "log":
        answers.ddl = input(
            "\nDDL / Pattern (optional): "
        ).strip() or None

def prompt_postgres_source(answers: BuilderAnswers):
    answers.postgres_uri = input(
        "\nPostgres URI: "
    ).strip()

def prompt_file_source(answers: BuilderAnswers):
    answers.file_path = input(
        "\nFile path: "
    ).strip()

def prompt_source(answers: BuilderAnswers):
    print("\n📦 Source Type")
    print("1. stdin")
    print("2. file")
    print("3. postgres")

    choice = input("> ").strip()

    mapping = {
        "1": "stdin",
        "2": "file",
        "3": "postgres",
    }

    answers.source_type = mapping.get(choice)

def prompt_project(answers: BuilderAnswers):
    print("\n🛠 Aegis Config Builder\n")

    answers.config_name = input(
        "Config name [aegis-config]: "
    ).strip() or "aegis-config"


    if answers.source_type == "file":
        prompt_file_source(answers)

    elif answers.source_type == "postgres":
        prompt_postgres_source(answers)

# --------- Entrypoint ---------------

def run_builder() -> BuilderAnswers:
    """
    Main interactive builder flow.
    """

    answers = BuilderAnswers()

    prompt_project(answers)
    prompt_source(answers)
    prompt_format(answers)
    prompt_optimize(answers)
    prompt_output(answers)

    return answers
from pathlib import Path


def module_name_from_path(
    file: Path
) -> str:

    parts = list(
        file.with_suffix("").parts
    )

    return ".".join(parts)
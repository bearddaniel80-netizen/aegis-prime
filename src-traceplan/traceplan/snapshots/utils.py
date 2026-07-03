def exists(
    path: str | Path
) -> bool:

    return Path(path).exists()

def delete(
    path: str | Path
) -> None:

    path = Path.cwd() / path

    if path.exists():
        path.unlink()

def list_snapshots(
    directory: str | Path
):

    root = Path.cwd() / directory

    if not root.exists():
        return []

    return sorted(
        root.glob("*.json")
    )
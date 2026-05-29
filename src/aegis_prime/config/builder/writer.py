import tomli_w


def write_config(data: dict, path: str):
    with open(path, "wb") as f:
        tomli_w.dump(data, f)
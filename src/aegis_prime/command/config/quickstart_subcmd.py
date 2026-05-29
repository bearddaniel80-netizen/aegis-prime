import typer

quickstart_app = typer.Typer()

@quickstart_app.callback(invoke_without_command=True)
def main():
    """
    Outputs a tiny usable config with sane defaults.
    """
    typer.echo("quickstart")
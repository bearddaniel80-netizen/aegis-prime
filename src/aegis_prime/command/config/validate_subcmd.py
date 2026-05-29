import typer

validate_app = typer.Typer()

@validate_app.callback(invoke_without_command=True)
def main():
    """
    Validate config specs.
    """
    typer.echo("validate")
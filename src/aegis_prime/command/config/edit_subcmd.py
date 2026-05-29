import typer

edit_app = typer.Typer()

@edit_app.callback(invoke_without_command=True)
def main():
    """
    Interactive guided schema editor.
    """
    typer.echo("edit")
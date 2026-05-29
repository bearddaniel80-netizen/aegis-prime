import typer
from .edit_subcmd import edit_app
from .init_subcmd import init_app
from .quickstart_subcmd import quickstart_app
from .validate_subcmd import validate_app

app = typer.Typer(invoke_without_command=True)

@app.callback()
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        pass

app.add_typer(edit_app, name="edit")
app.add_typer(init_app, name="init")
app.add_typer(quickstart_app, name="quickstart")
app.add_typer(validate_app, name="validate")
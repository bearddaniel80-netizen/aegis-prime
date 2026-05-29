# aegis_prime.command.analyze

import typer
from .explain_subcmd import explain_app
from aegis_prime.domain.analyzer import analyze_results

app = typer.Typer(invoke_without_command=True)

@app.callback()
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        analyze_results()

app.add_typer(explain_app, name="explain")
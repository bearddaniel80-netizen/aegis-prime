import typer
from aegis_prime.domain.reporter import generate_html_report

app = typer.Typer(invoke_without_command=True)

@app.callback()
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        generate_html_report()
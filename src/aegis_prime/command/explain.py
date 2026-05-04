# aegis_prime.command.explain

import typer
from aegis_prime.core.explain import explain_latest_group

explain_app = typer.Typer()

@explain_app.callback(invoke_without_command=True)
def explain(
    verbose: bool = typer.Option(False, "--verbose", "-v")
):
    explain_latest_group(verbose=verbose)
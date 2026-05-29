import typer
from aegis_prime.domain.config_dom import config_build
init_app = typer.Typer()

@init_app.callback(invoke_without_command=True)
def main():
    """
    Interactive guided schema builder.
    """
    config_build()
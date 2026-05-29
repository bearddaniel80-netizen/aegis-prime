import typer

build_app = typer.Typer()

@build_app.callback(invoke_without_command=True)
def build(
    show_finished_query: bool = typer.Option(
        False,
        "--show-finished-query",
        help="Print final AQL query after building"
    )
):
    """
    Interactive guided query builder.
    """
#    builder = QueryBuilderCLI()
#    state = builder.run()
#
#    if show_finished_query:
#        compiler = AQLCompiler()
#        aql = compiler.compile(state)
#
#        typer.echo("\nGenerated AQL:\n")
    typer.echo("builder")
import typer
import aegis_prime.command.analyze.analyze_cmd as analyze
import aegis_prime.command.config.config_cmd as config
import aegis_prime.command.query.query_cmd as query
import aegis_prime.command.reporter_cmd as report

app = typer.Typer()

app.add_typer(analyze.app, name="analyze")
app.add_typer(config.app, name="config")
app.add_typer(query.app, name="query")
app.add_typer(report.app, name="report")

def main():
    print("Aegis Prime running")
    app()

if __name__ == "__main__":
    main()
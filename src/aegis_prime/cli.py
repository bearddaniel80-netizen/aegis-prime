import typer
import aegis_prime.command.analyze as analyze
import aegis_prime.command.reporter as report

app = typer.Typer()

app.add_typer(analyze.app, name="analyze")
app.add_typer(report.app, name="report")

def main():
    print("Aegis Prime running")
    app()

if __name__ == "__main__":
    main()
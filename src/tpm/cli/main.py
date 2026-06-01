import typer
import yaml

app = typer.Typer(
    help="CLI Base para Trusted Cognitive Platform (TPM).", no_args_is_help=True
)


@app.command("init")
def init():
    """
    Inicializa o TPM gerando o arquivo tpm.yaml
    """
    classification = typer.prompt("Classificação dos dados")
    criticality = typer.prompt("Criticidade")
    environment = typer.prompt("Ambiente")
    multi_tenant_str = typer.prompt("Multi-tenant (true/false)")
    multi_tenant = multi_tenant_str.lower() == "true"

    config = {
        "project": {
            "classification": classification,
            "criticality": criticality,
            "environment": environment,
            "multi_tenant": multi_tenant,
        }
    }

    with open("tpm.yaml", "w") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)

    typer.echo("Arquivo tpm.yaml gerado com sucesso!")


# Precisamos garantir que haja pelo menos dois comandos, ou add dummy assim o typer vai se portar como grupo
@app.command("dummy", hidden=True)
def dummy():
    pass


@app.command("serve")
def serve(host: str = "127.0.0.1", port: int = 8000):
    """Sobe o FastAPI Gateway do TPM"""
    import uvicorn

    typer.echo(f"Iniciando TPM Gateway em http://{host}:{port}")
    uvicorn.run("tpm.gateway.app:app", host=host, port=port, reload=False)


if __name__ == "__main__":
    app()

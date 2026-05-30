import os
import yaml
from typer.testing import CliRunner
from tpm.cli.main import app

runner = CliRunner()


def test_tpm_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "CLI Base para Trusted Cognitive Platform" in result.stdout


def test_tpm_init():
    if os.path.exists("tpm.yaml"):
        os.remove("tpm.yaml")

    result = runner.invoke(
        app, ["init"], input="confidential\nhigh\nenterprise\ntrue\n"
    )
    assert result.exit_code == 0
    assert "Arquivo tpm.yaml gerado com sucesso!" in result.stdout
    assert os.path.exists("tpm.yaml")

    with open("tpm.yaml", "r") as f:
        data = yaml.safe_load(f)

    assert "project" in data
    assert data["project"]["classification"] == "confidential"
    assert data["project"]["criticality"] == "high"
    assert data["project"]["environment"] == "enterprise"
    assert data["project"]["multi_tenant"] is True

    if os.path.exists("tpm.yaml"):
        os.remove("tpm.yaml")

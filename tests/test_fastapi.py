import pytest
from fastapi.testclient import TestClient
from tpm.gateway.app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    # Sqlite in memory should reply healthy
    assert "healthy" in response.json()["database"]


def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json()["version"] == "0.1.0"


def test_runtime_status():
    response = client.get("/runtime-status")
    assert response.status_code == 200
    assert response.json()["status"] == "running"

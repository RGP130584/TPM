from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from tpm.persistence.database import SessionLocal
from tpm.versioning.semver.model import SemanticVersion

app = FastAPI(title="TPM Gateway", version="0.1.0")


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health_check(db: Session = Depends(get_db_session)):
    """Status do gateway e persistência"""
    try:
        db.execute(text("SELECT 1"))
        db_status = "healthy"
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"

    return {"status": "ok", "database": db_status}


@app.get("/version")
def get_version():
    """Retorna versão atestada pelo SemanticVersion Runtime"""
    v = SemanticVersion(major=0, minor=1, patch=0)
    return {"version": v.version_string}


@app.get("/runtime-status")
def get_runtime_status():
    """Reporta os states correntes dos componentes em memória."""
    # Como não temos um StateManager Global nesta PR mockado de components reais do Uvicorn start,
    # mockamos uma resposta com o schema que o manager preencheria:
    return {
        "status": "running",
        "active_plugins": [],
        "active_workflows": 0,
        "mcp_loaded": True,
    }

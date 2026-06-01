import pytest
from tpm.registry.mcps.engineering import EngineeringMCP
from tpm.runtime.execution.context import ExecutionContext
from tpm.persistence.database import Base, engine

Base.metadata.create_all(bind=engine)


def test_engineering_mcp_flow():
    mcp = EngineeringMCP()
    ctx = ExecutionContext(tenant_id="mcp-tenant-1", workspace_id="ws1")

    mcp.start(ctx)
    assert mcp.state.value == "running"

    doc_id = mcp.store_documents("Spec", "My spec", {"version": "1.0"})
    assert doc_id is not None

    fetched = mcp.retrieve_documents(doc_id)
    assert fetched["title"] == "Spec"
    assert fetched["metadata"]["version"] == "1.0"

    # query test
    res = mcp.query_metadata("version", "1.0")
    assert len(res) >= 1

    mcp.stop()
    assert mcp.state.value == "stopped"

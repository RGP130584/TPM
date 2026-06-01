from typing import Any, Dict
from pydantic import BaseModel, Field
import uuid


class ExecutionContext(BaseModel):
    """
    Representa o escopo ou contexto de uma execução individual na Runtime Architecture.
    """

    execution_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    tenant_id: str
    workspace_id: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

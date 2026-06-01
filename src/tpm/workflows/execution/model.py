from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
from tpm.runtime.lifecycle.state import LifecycleState
import uuid


class StepExecution(BaseModel):
    step_id: str
    state: LifecycleState = LifecycleState.INITIALIZED
    result: Optional[Dict[str, Any]] = None


class WorkflowExecution(BaseModel):
    execution_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    workflow_id: str
    state: LifecycleState = LifecycleState.INITIALIZED
    step_executions: Dict[str, StepExecution] = Field(default_factory=dict)

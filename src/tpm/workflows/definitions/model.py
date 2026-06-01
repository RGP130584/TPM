from pydantic import BaseModel, Field
from typing import List, Dict, Any


class WorkflowStepDefinition(BaseModel):
    step_id: str
    action: str  # id de um MCP ou Skill
    parameters: Dict[str, Any] = Field(default_factory=dict)
    next_steps: List[str] = Field(default_factory=list)


class WorkflowDefinition(BaseModel):
    workflow_id: str
    name: str
    version: str
    steps: List[WorkflowStepDefinition] = Field(default_factory=list)

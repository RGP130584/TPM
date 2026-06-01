from pydantic import BaseModel, Field
from typing import Dict, Any


class Environment(BaseModel):
    env_id: str
    name: str  # Ex: "dev", "staging", "prod"
    config: Dict[str, Any] = Field(default_factory=dict)


class Workspace(BaseModel):
    workspace_id: str
    name: str
    environments: list[Environment] = Field(default_factory=list)


class Tenant(BaseModel):
    tenant_id: str
    name: str
    workspaces: list[Workspace] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)

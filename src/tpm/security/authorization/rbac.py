from typing import List
from pydantic import BaseModel, Field


class Permission(BaseModel):
    resource: str
    action: str  # Ex: "read", "write", "execute", "*"


class Role(BaseModel):
    role_id: str
    name: str
    permissions: List[Permission] = Field(default_factory=list)

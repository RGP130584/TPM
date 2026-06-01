from pydantic import BaseModel, Field
from typing import List


class RuntimeAuthorizationContext(BaseModel):
    user_id: str
    tenant_id: str
    active_roles: List[str] = Field(default_factory=list)

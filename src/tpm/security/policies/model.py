from pydantic import BaseModel
from typing import Dict, Any


class SecurityPolicy(BaseModel):
    policy_id: str
    name: str
    effect: str  # "allow" ou "deny"
    conditions: Dict[str, Any]

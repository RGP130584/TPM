from pydantic import BaseModel
from typing import Optional


class DeprecationRule(BaseModel):
    component_name: str
    deprecated_since: str
    removal_in_version: str
    replacement_suggestion: Optional[str] = None

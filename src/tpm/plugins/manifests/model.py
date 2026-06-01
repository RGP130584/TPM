from pydantic import BaseModel, Field
from typing import Dict, Any, List


class PluginManifest(BaseModel):
    plugin_id: str
    name: str
    version: str
    description: str = ""
    author: str = ""
    plugin_type: str = Field(..., description="mcp, skill, transformer, agent")
    dependencies: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)

from datetime import datetime, timezone
import uuid
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


class BaseEvent(BaseModel):
    """
    Modelo de Evento Base da plataforma TPM, preparado para infraestruturas como Kafka.
    """

    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=_utc_now)
    event_type: str
    source: str
    tenant_id: Optional[str] = None
    payload: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class AgentEvent(BaseEvent):
    event_type: str = "agent_event"
    agent_id: str


class SkillEvent(BaseEvent):
    event_type: str = "skill_event"
    skill_id: str


class TransformerEvent(BaseEvent):
    event_type: str = "transformer_event"
    transformer_id: str


class MCPEvent(BaseEvent):
    event_type: str = "mcp_event"
    mcp_id: str


class SecurityEvent(BaseEvent):
    event_type: str = "security_event"
    severity: str = Field(default="info", description="Ex: info, warning, critical")
    actor: str

from pydantic import BaseModel, Field


class ExecutionMetrics(BaseModel):
    execution_type: str = Field(..., description="skill, agent, transformer")
    entity_id: str
    latency_ms: float
    error_rate: float = 0.0


class AITokenMetrics(BaseModel):
    context_size: int = Field(default=0, description="Tamanho do contexto provido")
    prompt_tokens: int = Field(default=0)
    completion_tokens: int = Field(default=0)
    total_tokens: int = Field(default=0)
    cost_estimation: float = Field(
        default=0.0, description="Custo estimado tracking em USD"
    )

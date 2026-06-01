from pydantic import BaseModel, Field


class ProjectSpec(BaseModel):
    classification: str = Field(..., description="Classificação dos dados")
    criticality: str = Field(..., description="Criticidade")
    environment: str = Field(..., description="Ambiente")
    multi_tenant: bool = Field(..., description="Multi-tenant")


class TPMSpec(BaseModel):
    project: ProjectSpec

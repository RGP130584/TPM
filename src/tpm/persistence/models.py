from sqlalchemy import Column, String, JSON, Integer
from tpm.persistence.database import Base
import uuid


class DocumentModel(Base):
    """
    Entidade básica persistida usada principalmente no EngineeringMCP para armazenar docs e metadados.
    """

    __tablename__ = "documents"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String, index=True)
    title = Column(String, index=True)
    content = Column(String)
    metadata_json = Column(JSON, default=dict)

from typing import Dict, Any, List, Optional
from tpm.persistence.database import SessionLocal
from tpm.persistence.repository import BaseRepository
from tpm.persistence.models import DocumentModel
from tpm.persistence.uow import UnitOfWork
from tpm.runtime.interfaces import IRuntimeComponent
from tpm.runtime.lifecycle.state import LifecycleState
from tpm.runtime.execution.context import ExecutionContext
import uuid


class EngineeringMCP(IRuntimeComponent):
    """
    Model Context Protocol abstrato para contexto de engenharia.
    Realiza o intermédio entre o LLM (Agents/Skills) e a Base de Dados de RAG de Engenharia/Metadados.
    """

    def __init__(self):
        self._state = LifecycleState.INITIALIZED
        self.current_context = None
        self.doc_repo = BaseRepository(DocumentModel)

    @property
    def state(self) -> LifecycleState:
        return self._state

    def start(self, context: ExecutionContext) -> None:
        self.current_context = context
        self._state = LifecycleState.RUNNING

    def stop(self) -> None:
        self.current_context = None
        self._state = LifecycleState.STOPPED

    def store_documents(
        self, title: str, content: str, metadata: Dict[str, Any] = None
    ) -> str:
        if self.state != LifecycleState.RUNNING:
            raise RuntimeError("MCP must be in RUNNING state to execute actions.")

        new_doc = DocumentModel(
            id=str(uuid.uuid4()),
            tenant_id=self.current_context.tenant_id,
            title=title,
            content=content,
            metadata_json=metadata or {},
        )
        with UnitOfWork() as uow:
            self.doc_repo.create(uow.session, new_doc)
            return new_doc.id

    def retrieve_documents(self, doc_id: str) -> Optional[Dict[str, Any]]:
        if self.state != LifecycleState.RUNNING:
            raise RuntimeError("MCP must be in RUNNING state to execute actions.")
        with UnitOfWork() as uow:
            doc = self.doc_repo.get(uow.session, doc_id)
            if doc and self.current_context and doc.tenant_id == self.current_context.tenant_id:
                return {
                    "id": doc.id,
                    "title": doc.title,
                    "content": doc.content,
                    "metadata": doc.metadata_json,
                }
        return None

    def register_metadata(self, doc_id: str, key: str, value: Any) -> bool:
        if self.state != LifecycleState.RUNNING:
            raise RuntimeError("MCP must be in RUNNING state to execute actions.")
        with UnitOfWork() as uow:
            doc = self.doc_repo.get(uow.session, doc_id)
            if doc and self.current_context and doc.tenant_id == self.current_context.tenant_id:
                metadata = dict(doc.metadata_json)
                metadata[key] = value
                doc.metadata_json = metadata
                # Como UnitOfWork finaliza com commit, objeto trackeado será feito update automático (SQLAlchemy dirty flag)
                return True
        return False

    def query_metadata(self, key: str, value: Any) -> List[Dict[str, Any]]:
        results = []
        with UnitOfWork() as uow:
            # Atenção: busca linear/python base para exemplificação do runtime v1.
            # Em prod seria indexado e procurado com func.json_extract ou vector search.
            docs = (
                uow.session.query(DocumentModel)
                .filter(DocumentModel.tenant_id == self.current_context.tenant_id)
                .all()
            )
            for d in docs:
                if d.metadata_json and d.metadata_json.get(key) == value:
                    results.append(
                        {"id": d.id, "title": d.title, "metadata": d.metadata_json}
                    )
        return results

import pytest
from tpm.persistence.database import Base, engine, SessionLocal
from tpm.persistence.repository import BaseRepository
from tpm.persistence.models import DocumentModel

Base.metadata.create_all(bind=engine)


def test_base_repository():
    db = SessionLocal()
    repo = BaseRepository(DocumentModel)

    doc = DocumentModel(tenant_id="tenant_1", title="Doc 1", content="Text")
    repo.create(db, doc)

    fetched = repo.get(db, doc.id)
    assert fetched.title == "Doc 1"
    assert fetched.tenant_id == "tenant_1"
    db.close()

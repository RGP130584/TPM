from sqlalchemy.orm import Session
from tpm.persistence.database import SessionLocal


class UnitOfWork:
    """
    Controla o escopo de transação no modelo de persistência.
    """

    def __init__(self, session_factory=SessionLocal):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is not None:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()

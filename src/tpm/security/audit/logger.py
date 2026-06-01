from abc import ABC, abstractmethod
from tpm.runtime.events.models import SecurityEvent


class AuditLogger(ABC):
    @abstractmethod
    def log(self, event: SecurityEvent) -> None:
        """Registra um evento de segurança em um repositório de auditoria"""
        pass

from abc import ABC, abstractmethod
from tpm.runtime.events.models import SecurityEvent
from tpm.security.authorization_runtime.model import RuntimeAuthorizationContext


class IAuditExecution(ABC):
    @abstractmethod
    def capture_execution(
        self, context: RuntimeAuthorizationContext, action: str, resource: str
    ) -> SecurityEvent:
        """Gera um evento de segurança em tempo de execução para trilha de auditoria contínua"""
        pass

from abc import ABC, abstractmethod
from typing import Dict, Any
from tpm.security.authorization_runtime.model import RuntimeAuthorizationContext
from tpm.security.policies.model import SecurityPolicy


class IPolicyEvaluator(ABC):
    @abstractmethod
    def evaluate(
        self,
        policy: SecurityPolicy,
        context: RuntimeAuthorizationContext,
        resource_data: Dict[str, Any],
    ) -> bool:
        """Avalia se uma policy permite a execução com base no contexto em tempo real"""
        pass

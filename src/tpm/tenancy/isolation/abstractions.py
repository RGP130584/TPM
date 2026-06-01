from abc import ABC, abstractmethod
from tpm.tenancy.models.core import Tenant, Workspace


class IsolationContext(ABC):
    """
    Abstração para garantia de isolamento entre Tenantes no MCCA Runtime.
    """

    @abstractmethod
    def enforce_isolation(self, tenant: Tenant, workspace: Workspace) -> bool:
        """
        Garante que as operações subsequentes estarão isoladas ao Tenant/Workspace especificado.
        """
        pass

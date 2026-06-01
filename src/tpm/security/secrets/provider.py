from abc import ABC, abstractmethod
from typing import Optional


class SecretProvider(ABC):
    """
    Abstração para buscar segredos de cofres como Vault, AWS Secrets, etc.
    """

    @abstractmethod
    def get_secret(self, key: str, tenant_id: str) -> Optional[str]:
        pass

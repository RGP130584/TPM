from abc import ABC, abstractmethod
from typing import Any, Dict


class MigrationScript(ABC):
    @property
    @abstractmethod
    def from_version(self) -> str:
        pass

    @property
    @abstractmethod
    def to_version(self) -> str:
        pass

    @abstractmethod
    def migrate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Aplica as transformações para up-grade de schema"""
        pass

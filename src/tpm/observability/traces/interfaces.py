from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class ITracer(ABC):
    @abstractmethod
    def start_span(self, name: str, parent_id: Optional[str] = None) -> str:
        """Inicia um span de rastreabilidade e retorna o span_id"""
        pass

    @abstractmethod
    def end_span(self, span_id: str, tags: Dict[str, Any] = None) -> None:
        pass

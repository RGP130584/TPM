from abc import ABC, abstractmethod
from typing import Dict


class IMetricsReporter(ABC):
    @abstractmethod
    def record_counter(
        self, name: str, value: int = 1, tags: Dict[str, str] = None
    ) -> None:
        pass

    @abstractmethod
    def record_histogram(
        self, name: str, value: float, tags: Dict[str, str] = None
    ) -> None:
        pass

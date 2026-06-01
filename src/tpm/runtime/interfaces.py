from abc import ABC, abstractmethod
from tpm.runtime.lifecycle.state import LifecycleState
from tpm.runtime.execution.context import ExecutionContext


class IRuntimeComponent(ABC):
    """
    Interface base para componentes executáveis da arquitetura Runtime.
    """

    @property
    @abstractmethod
    def state(self) -> LifecycleState:
        pass

    @abstractmethod
    def start(self, context: ExecutionContext) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

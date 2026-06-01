from abc import ABC, abstractmethod
from tpm.workflows.definitions.model import WorkflowDefinition
from tpm.workflows.execution.model import WorkflowExecution


class IWorkflowEngine(ABC):
    @abstractmethod
    def start_workflow(self, definition: WorkflowDefinition) -> WorkflowExecution:
        pass

    @abstractmethod
    def advance_step(self, execution: WorkflowExecution, current_step_id: str) -> None:
        pass

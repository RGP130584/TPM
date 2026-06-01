from tpm.workflows.definitions.model import WorkflowDefinition, WorkflowStepDefinition
from tpm.workflows.execution.model import WorkflowExecution


def test_workflow_definition():
    step = WorkflowStepDefinition(step_id="step1", action="skill-hello")
    workflow = WorkflowDefinition(
        workflow_id="wf-01", name="HelloWF", version="1.0.0", steps=[step]
    )
    assert len(workflow.steps) == 1
    assert workflow.steps[0].action == "skill-hello"


def test_workflow_execution():
    execution = WorkflowExecution(workflow_id="wf-01")
    assert execution.workflow_id == "wf-01"
    assert execution.state.value == "initialized"

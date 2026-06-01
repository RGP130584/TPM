from tpm.runtime.lifecycle.state import LifecycleState
from tpm.runtime.events.models import AgentEvent, SecurityEvent
from tpm.tenancy.models.core import Tenant, Workspace, Environment
from tpm.security.authorization.rbac import Role, Permission


def test_lifecycle_states():
    assert LifecycleState.INITIALIZED.value == "initialized"
    assert LifecycleState.RUNNING.value == "running"


def test_event_models():
    event = AgentEvent(source="test_runner", agent_id="agent-01")
    assert event.event_type == "agent_event"
    assert event.agent_id == "agent-01"
    assert event.event_id is not None
    assert event.timestamp is not None


def test_security_event():
    sec_evt = SecurityEvent(source="auth_module", actor="user-x")
    assert sec_evt.event_type == "security_event"
    assert sec_evt.severity == "info"
    assert sec_evt.actor == "user-x"


def test_tenancy_hierarchy():
    env = Environment(env_id="env-1", name="prod")
    ws = Workspace(workspace_id="ws-1", name="core-workspace", environments=[env])
    tenant = Tenant(tenant_id="tenant-1", name="acme-corp", workspaces=[ws])

    assert tenant.tenant_id == "tenant-1"
    assert len(tenant.workspaces) == 1
    assert tenant.workspaces[0].environments[0].name == "prod"


def test_rbac_models():
    perm = Permission(resource="agent", action="read")
    role = Role(role_id="role-1", name="viewer", permissions=[perm])

    assert role.name == "viewer"
    assert len(role.permissions) == 1
    assert role.permissions[0].action == "read"

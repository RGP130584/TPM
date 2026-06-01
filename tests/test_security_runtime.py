from tpm.security.authorization_runtime.model import RuntimeAuthorizationContext


def test_runtime_auth_context():
    ctx = RuntimeAuthorizationContext(
        user_id="u1", tenant_id="t1", active_roles=["admin", "user"]
    )
    assert ctx.tenant_id == "t1"
    assert "admin" in ctx.active_roles

from tpm.security.identity.jwt_utils import create_access_token, decode_access_token
import pytest


def test_jwt_flow():
    token = create_access_token({"sub": "user-01"})
    payload = decode_access_token(token)
    assert payload["sub"] == "user-01"
    assert "exp" in payload

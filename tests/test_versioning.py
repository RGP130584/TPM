from tpm.versioning.semver.model import SemanticVersion
from tpm.versioning.compatibility.engine import CompatibilityEngine


def test_semantic_version():
    ver = SemanticVersion.parse("1.2.3-alpha")
    assert ver.major == 1
    assert ver.minor == 2
    assert ver.patch == 3
    assert ver.pre_release == "alpha"
    assert ver.version_string == "1.2.3-alpha"


def test_compatibility():
    old = SemanticVersion(major=1, minor=0, patch=0)
    new = SemanticVersion(major=1, minor=2, patch=0)
    breaking = SemanticVersion(major=2, minor=0, patch=0)

    assert CompatibilityEngine.is_backward_compatible(old, new) is True
    assert CompatibilityEngine.is_backward_compatible(old, breaking) is False

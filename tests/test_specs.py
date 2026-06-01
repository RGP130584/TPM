import pytest
import yaml
from tpm.specs.loader import SpecLoader
from tpm.validators.engine import SpecificationError
from tpm.models.spec import TPMSpec


@pytest.fixture
def valid_yaml_file(tmp_path):
    data = {
        "project": {
            "classification": "confidential",
            "criticality": "high",
            "environment": "enterprise",
            "multi_tenant": True,
        }
    }
    filepath = tmp_path / "tpm.yaml"
    with open(filepath, "w") as f:
        yaml.dump(data, f)
    return str(filepath)


@pytest.fixture
def invalid_yaml_file(tmp_path):
    data = {
        "project": {
            "classification": "confidential",
            # missing required fields
        }
    }
    filepath = tmp_path / "tpm.yaml"
    with open(filepath, "w") as f:
        yaml.dump(data, f)
    return str(filepath)


def test_load_and_validate_success(valid_yaml_file):
    loader = SpecLoader(filepath=valid_yaml_file)
    spec = loader.load_and_validate()

    assert isinstance(spec, TPMSpec)
    assert spec.project.classification == "confidential"
    assert spec.project.criticality == "high"
    assert spec.project.environment == "enterprise"
    assert spec.project.multi_tenant is True


def test_load_and_validate_failure(invalid_yaml_file):
    loader = SpecLoader(filepath=invalid_yaml_file)
    with pytest.raises(SpecificationError):
        loader.load_and_validate()

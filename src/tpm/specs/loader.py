import yaml
import os
from typing import Dict, Any
from tpm.validators.engine import ValidationEngine, SpecificationError
from tpm.models.spec import TPMSpec


class SpecLoader:
    def __init__(self, filepath: str = "tpm.yaml"):
        self.filepath = filepath
        self.engine = ValidationEngine()

    def load_raw(self) -> Dict[str, Any]:
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Specification file not found: {self.filepath}")

        with open(self.filepath, "r") as f:
            data = yaml.safe_load(f)

        if not isinstance(data, dict):
            raise SpecificationError("YAML content must be a dictionary")

        return data

    def load_and_validate(self) -> TPMSpec:
        raw_data = self.load_raw()
        return self.engine.validate(raw_data)

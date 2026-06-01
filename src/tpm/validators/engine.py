from typing import Any, Dict
from pydantic import ValidationError
from tpm.models.spec import TPMSpec


class SpecificationError(Exception):
    pass


class ValidationEngine:
    @staticmethod
    def validate(data: Dict[str, Any]) -> TPMSpec:
        try:
            return TPMSpec(**data)
        except ValidationError as e:
            raise SpecificationError(f"Erro de validação: {e}") from e

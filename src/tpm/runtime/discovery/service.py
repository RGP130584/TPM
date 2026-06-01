from typing import Any, Dict, List, Optional
from tpm.registry.base import BaseRegistry


class ComponentDiscovery:
    """
    Abstração para buscar, descobrir e resolver componentes da plataforma em tempo de execução.
    """

    def __init__(self, registries: Dict[str, BaseRegistry[Any]]):
        self._registries = registries

    def discover(
        self, component_type: str, name: str, version: Optional[str] = None
    ) -> Any:
        registry = self._registries.get(component_type)
        if not registry:
            raise ValueError(f"Registry type '{component_type}' not found.")

        component = registry.get(name, version)
        if not component:
            raise ValueError(
                f"Component '{name}' not found in registry '{component_type}'."
            )
        return component

    def list_components(self, component_type: str) -> Dict[str, List[str]]:
        registry = self._registries.get(component_type)
        if not registry:
            return {}
        return registry.list_all()

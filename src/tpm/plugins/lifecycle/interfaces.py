from abc import ABC, abstractmethod
from tpm.plugins.manifests.model import PluginManifest


class IPluginLifecycle(ABC):
    @abstractmethod
    def on_load(self, manifest: PluginManifest) -> None:
        pass

    @abstractmethod
    def on_enable(self) -> None:
        pass

    @abstractmethod
    def on_disable(self) -> None:
        pass

    @abstractmethod
    def on_unload(self) -> None:
        pass

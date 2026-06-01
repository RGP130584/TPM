from typing import Dict, Any
from tpm.plugins.manifests.model import PluginManifest
from tpm.plugins.lifecycle.interfaces import IPluginLifecycle
from tpm.registry.base import BaseRegistry


class PluginLoader:
    def __init__(self, registry: BaseRegistry[Any]):
        self.registry = registry
        self.loaded_plugins: Dict[str, PluginManifest] = {}
        self.active_plugins: Dict[str, IPluginLifecycle] = {}

    def load_plugin(
        self, manifest: PluginManifest, plugin_instance: IPluginLifecycle
    ) -> None:
        # Registra no registro global
        self.registry.register(
            name=manifest.name, version=manifest.version, item=plugin_instance
        )

        # Gerenciamento de ciclo de vida do loader
        self.loaded_plugins[manifest.plugin_id] = manifest
        plugin_instance.on_load(manifest)

        # Mantém referência da instância carregada
        self.active_plugins[manifest.plugin_id] = plugin_instance

    def enable_plugin(self, plugin_id: str) -> None:
        plugin = self.active_plugins.get(plugin_id)
        if plugin:
            plugin.on_enable()

    def disable_plugin(self, plugin_id: str) -> None:
        plugin = self.active_plugins.get(plugin_id)
        if plugin:
            plugin.on_disable()

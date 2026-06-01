from tpm.plugins.manifests.model import PluginManifest


def test_plugin_manifest():
    manifest = PluginManifest(
        plugin_id="plugin-01", name="test-plugin", version="1.0.0", plugin_type="mcp"
    )
    assert manifest.plugin_id == "plugin-01"
    assert manifest.plugin_type == "mcp"

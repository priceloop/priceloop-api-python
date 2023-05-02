from enum import Enum


class WebhookPluginEvent(str, Enum):
    PLUGININSTALLED = "PluginInstalled"
    PLUGINUNINSTALLED = "PluginUninstalled"
    PLUGINTOKENSUPDATED = "PluginTokensUpdated"
    PLUGINCUSTOM = "PluginCustom"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class AddPluginWebhookEvent(str, Enum):
    PLUGININSTALLED = "PluginInstalled"
    PLUGINUNINSTALLED = "PluginUninstalled"
    PLUGINTOKENSUPDATED = "PluginTokensUpdated"

    def __str__(self) -> str:
        return str(self.value)

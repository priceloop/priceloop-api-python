from enum import Enum


class WebhookPluginEvent(str, Enum):
    PLUGINDATAUPDATED = "PluginDataUpdated"
    PLUGININSTALLED = "PluginInstalled"
    PLUGINTABLEROLETRIGGER = "PluginTableRoleTrigger"
    PLUGINTOKENSUPDATED = "PluginTokensUpdated"
    PLUGINUNINSTALLED = "PluginUninstalled"

    def __str__(self) -> str:
        return str(self.value)

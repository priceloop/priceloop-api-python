from enum import Enum


class ListPluginWebhooksPluginName(str, Enum):
    APE = "ape"

    def __str__(self) -> str:
        return str(self.value)

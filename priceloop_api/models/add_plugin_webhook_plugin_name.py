from enum import Enum


class AddPluginWebhookPluginName(str, Enum):
    APE = "ape"

    def __str__(self) -> str:
        return str(self.value)

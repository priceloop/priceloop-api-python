from enum import Enum


class DeletePluginWebhookPluginName(str, Enum):
    APE = "ape"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class PluginRequirement(str, Enum):
    AMAZONAUTHENTICATION = "AmazonAuthentication"

    def __str__(self) -> str:
        return str(self.value)

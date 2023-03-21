from enum import Enum


class GetPluginPlugin(str, Enum):
    APE = "ape"

    def __str__(self) -> str:
        return str(self.value)

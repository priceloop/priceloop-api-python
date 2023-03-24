from enum import Enum


class CreatePluginPlugin(str, Enum):
    APE = "ape"

    def __str__(self) -> str:
        return str(self.value)

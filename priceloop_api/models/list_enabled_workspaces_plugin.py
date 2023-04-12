from enum import Enum


class ListEnabledWorkspacesPlugin(str, Enum):
    APE = "ape"

    def __str__(self) -> str:
        return str(self.value)

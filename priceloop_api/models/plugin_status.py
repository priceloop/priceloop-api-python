from enum import Enum


class PluginStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class PluginTableRoleSemantic(str, Enum):
    PUBLISHINPUT = "PublishInput"

    def __str__(self) -> str:
        return str(self.value)

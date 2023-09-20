from enum import Enum


class NumberDisplayStyle(str, Enum):
    CUSTOM = "custom"
    DEFAULT = "default"
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)

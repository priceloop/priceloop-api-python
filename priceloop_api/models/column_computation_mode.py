from enum import Enum


class ColumnComputationMode(str, Enum):
    EAGER = "eager"
    LAZY = "lazy"

    def __str__(self) -> str:
        return str(self.value)

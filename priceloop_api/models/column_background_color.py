from enum import Enum


class ColumnBackgroundColor(str, Enum):
    LIME = "lime"
    PURPLE = "purple"

    def __str__(self) -> str:
        return str(self.value)

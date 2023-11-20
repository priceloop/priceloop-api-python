from enum import Enum


class ColumnGroupColor(str, Enum):
    BLUE = "blue"
    LIME = "lime"
    PURPLE = "purple"
    RED = "red"
    YELLOW = "yellow"

    def __str__(self) -> str:
        return str(self.value)

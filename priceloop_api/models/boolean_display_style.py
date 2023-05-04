from enum import Enum


class BooleanDisplayStyle(str, Enum):
    TEXT = "text"
    CHECKBOX = "checkbox"

    def __str__(self) -> str:
        return str(self.value)

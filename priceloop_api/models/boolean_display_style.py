from enum import Enum


class BooleanDisplayStyle(str, Enum):
    CHECKBOX = "checkbox"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)

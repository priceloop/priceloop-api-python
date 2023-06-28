from enum import Enum


class StringDisplayStyle(str, Enum):
    MARKDOWN = "markdown"
    RAW = "raw"

    def __str__(self) -> str:
        return str(self.value)

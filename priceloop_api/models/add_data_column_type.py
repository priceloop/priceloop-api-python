from enum import Enum


class AddDataColumnType(str, Enum):
    STRING = "string"
    NUMBER = "number"
    BOOLEAN = "boolean"
    DATE = "date"
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)

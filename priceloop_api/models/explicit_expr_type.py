from enum import Enum


class ExplicitExprType(str, Enum):
    NUMBER = "number"
    STRING = "string"
    BOOLEAN = "boolean"
    DATE = "date"
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)

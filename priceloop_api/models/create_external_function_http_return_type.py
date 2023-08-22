from enum import Enum


class CreateExternalFunctionHttpReturnType(str, Enum):
    BOOLEAN = "boolean"
    DATE = "date"
    JSON = "json"
    NUMBER = "number"
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)

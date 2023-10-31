from enum import Enum


class ApiOnConflict(str, Enum):
    FAIL = "fail"
    IGNORE = "ignore"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)

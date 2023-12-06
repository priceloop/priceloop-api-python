from enum import Enum


class ApiDeleteMode(str, Enum):
    DELETE_MATCHING = "delete_matching"
    DELETE_NOT_MATCHING = "delete_not_matching"

    def __str__(self) -> str:
        return str(self.value)

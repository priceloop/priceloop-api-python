from enum import Enum


class TableImportMode(str, Enum):
    APPEND_DATA = "append_data"
    DELETE_AND_RECREATE = "delete_and_recreate"
    NEW = "new"
    REPLACE_DATA = "replace_data"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class CreateCsvImportJobMode(str, Enum):
    NEW = "new"
    DELETE_AND_RECREATE = "delete_and_recreate"
    REPLACE_DATA = "replace_data"
    APPEND_DATA = "append_data"

    def __str__(self) -> str:
        return str(self.value)

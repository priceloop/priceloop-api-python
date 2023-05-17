from enum import Enum


class ExternalFunctionRuntime(str, Enum):
    GO = "go"
    NODEJS = "nodejs"
    PYTHON = "python"
    PYTHON_NUMPY = "python_numpy"
    PYTHON_PANDAS = "python_pandas"

    def __str__(self) -> str:
        return str(self.value)

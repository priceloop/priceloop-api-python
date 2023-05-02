from enum import Enum


class ExternalFunctionRuntime(str, Enum):
    PYTHON = "python"
    PYTHON_NUMPY = "python_numpy"
    PYTHON_PANDAS = "python_pandas"
    NODEJS = "nodejs"
    GO = "go"

    def __str__(self) -> str:
        return str(self.value)

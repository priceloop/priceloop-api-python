import os

import pandas as pd
import pytest

from priceloop_api.priceloop.extras import (
    Column,
    ColumnType,
    PatchMode,
    TableUtils,
)

from priceloop_api.priceloop.extras.helpers import get_priceloop_client


@pytest.fixture
def sample_dataframe1() -> pd.DataFrame:
    df = pd.DataFrame(
        data={
            "name": ["John", "Alice", "Bob"],
            "age": [25, 30, 22],
            "date_of_birth": pd.to_datetime(["1997-05-15", "1992-08-22", "2000-01-10"]),
            "gpa": [3.3, 2.9, 3.0],
            "json_field": ["{}", '{"a":"object"}', '{"1":3}'],
        },
    )
    return df


class TestTableUtils:
    def test(self) -> None:
        assert True

    def test_initiate_table_on_platform(self) -> None:
        client = get_priceloop_client()
        assert TableUtils.initialize_table(
            os.environ["NOCODE_WORKSPACE"],
            "table1",
            [
                Column("name", ColumnType.Text),
                Column("age", ColumnType.Number),
                Column("date_of_birth", ColumnType.Date),
                Column("gpa", ColumnType.Number),
                Column("json_field", ColumnType.Json),
            ],
            client,
        )
        assert TableUtils.is_table_on_platform(
            os.environ["NOCODE_WORKSPACE"],
            "table1",
            client,
        )

    def test_get_table_data(self) -> None:
        client = get_priceloop_client()
        assert (
            TableUtils.read_table(
                os.environ["NOCODE_WORKSPACE"],
                "table1",
                client,
            )
            is not None
        )

    def test_truncate_table(self) -> None:
        client = get_priceloop_client()
        assert TableUtils.truncate(
            os.environ["NOCODE_WORKSPACE"],
            "table1",
            client,
        )

    def test_patch_table(self, sample_dataframe1: pd.DataFrame) -> None:
        client = get_priceloop_client()

        TableUtils.patch_table(
            os.environ["NOCODE_WORKSPACE"],
            "table1",
            sample_dataframe1,
            client,
            PatchMode.Append,
            data_columns=["name", "age", "json_field"],
        )
        assert True
        TableUtils.patch_table(
            os.environ["NOCODE_WORKSPACE"],
            "table1",
            sample_dataframe1,
            client,
            PatchMode.Update,
            match_on_columns=["name", "age"],
            data_columns=["date_of_birth", "gpa"],
        )
        assert True
        TableUtils.patch_table(
            os.environ["NOCODE_WORKSPACE"],
            "table1",
            sample_dataframe1,
            client,
            PatchMode.Delete,
            match_on_columns=["name", "age"],
        )
        assert True

        table = TableUtils.read_table(
            os.environ["NOCODE_WORKSPACE"],
            "table1",
            client,
        )
        assert table.shape[0] == 0

    def test_delete_table(self) -> None:
        client = get_priceloop_client()
        assert TableUtils.delete_table(
            os.environ["NOCODE_WORKSPACE"],
            "table1",
            client,
        )

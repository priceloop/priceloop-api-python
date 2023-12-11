from enum import Enum
from http import HTTPStatus
from io import StringIO
from typing import Any, Callable, List, Literal, Optional

import os
import attr
import numpy as np
import pandas as pd
import requests

from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type


from priceloop_api.api.import_api import create_csv_import_job, get_csv_import_job
from priceloop_api.api.table_api import (
    create_table,
    delete_table,
    get_incomplete_table_query_data,
    get_table,
    get_table_data,
    patch_table_data,
    truncate_table,
)
from priceloop_api.client import AuthenticatedClient
from priceloop_api.errors import UnexpectedStatus
from priceloop_api.models import (
    ApiDeleteMode,
    ApiColumnSchema,
    ApiColumnWithNullableValues,
    ApiColumnWithValues,
    ApiOnConflict,
    ApiTable,
    ApiTableData,
    ApiTableSchema,
    Append,
    Delete,
    ExplicitExprType,
    ImportJob,
    Insert,
    TableImportMode,
    TableRow,
    Update,
)
from priceloop_api.types import UNSET, Unset

from .exceptions import (
    PlatformException,
)

NUM_OF_RETRIES = int(os.getenv("NUM_OF_RETRIES", 3))
CELL_LIMIT = 30000


class ImportMode(str, Enum):
    Append = "append"
    Overwrite = "overwrite"


class PatchMode(str, Enum):
    Append = "append"
    Delete = "delete"
    InsertOnConflictIgnore = "insert_on_conflict_ignore"
    InsertOnConflictFail = "insert_on_conflict_fail"
    InsertOnConflictUpdate = "insert_on_conflict_update"
    Update = "update"


class ColumnType(str, Enum):
    Number = "number"
    Text = "string"
    Boolean = "boolean"
    Date = "date"
    Json = "json"
    Formula = "formula"


@attr.s(auto_attribs=True)
class Column:
    name: str
    ctype: ColumnType

    def __repr__(self) -> str:
        return f"Column Object <name: {self.name}, type: {self.ctype}>"


@attr.s(auto_attribs=True)
class TableUtils:
    """
    Utility class for interacting with tables on Priceloop Nocode Platform.

    Methods:
        is_table_on_platform(
            workspace_name: str,
            table_name: str,
            client: AuthenticatedClient
        ) -> bool:
            Checks if a table exists on the platform.

        initialize_table(workspace_name: str,
          table_name: str,
          columns: List[Column],
          client: AuthenticatedClient
        ) -> bool:
            Initializes a table with the given name and columns on the platform.

        delete_table(workspace_name: str,
        table_name: str,
        client: AuthenticatedClient
        ) -> bool:
            Deletes a table from the platform.

        read_table(
            workspace_name: str,
            table_name: str, client: AuthenticatedClient,
            columns: Optional[List[str]] = None,
            exclude_formulas: bool = False
            ) -> pd.DataFrame:
            Reads data from a table on the platform and returns it as a DataFrame.

        truncate(workspace_name: str, table_name: str, client: AuthenticatedClient) -> bool:
            Truncates a table on the platform, removing all its data.

        get_data(workspace_name: str, table_name: str, nocode_client: AuthenticatedClient,
                 rows_limit: int, columns: List[str], func: Callable) -> List[TableRow] | Unset:
            Gets data from a table on the platform using a specified function.

        get_metadata(workspace_name: str, table_name: str, client: AuthenticatedClient,
                     exclude_formulas: bool = False) -> ApiTable:
            Retrieves metadata for a table on the platform.

        get_slice_of_data(workspace_name: str, table_name: str, limit: int, offset: int,
                          list_of_columns: List[str], client: AuthenticatedClient) -> ApiTableData:
            Retrieves a slice of data from a table on the platform.

        get_table_data_sync(workspace_name, table_name, client, limit, offset, list_of_columns):
            Synchronously retrieves table data with optional columns from the platform.

        get_rows(workspace_name: str, table_name: str, client: AuthenticatedClient, limit: int,
                 offset: int, list_of_columns: List[str], exclude_formulas: bool = False) -> ApiTableData:
            Retrieves rows of data from a table on the platform.

    Note:
        This class provides utility methods for common operations on tables such as checking existence,
        initialization, deletion, and data retrieval on a specified platform.

    """

    @staticmethod
    @retry(stop=stop_after_attempt(NUM_OF_RETRIES), wait=wait_fixed(1), retry=retry_if_exception_type(PlatformException))
    def is_table_on_platform(
        workspace_name: str,
        table_name: str,
        client: AuthenticatedClient,
    ) -> bool:
        """
        Checks if a table exists on the specified platform.

        Args:
            workspace_name (str): The name of the workspace.
            table_name (str): The name of the table.
            client (AuthenticatedClient): The authenticated client for platform interaction.

        Returns:
            bool: True if the table exists, False otherwise.

        Raises:
            PlatformException: If an unexpected platform error occurs.
        """
        try:
            response = get_table.sync_detailed(
                workspace_name,
                table_name,
                client=client,
            )
            status_code = response.status_code
            if status_code == HTTPStatus.OK:
                return True
            elif status_code == HTTPStatus.NOT_FOUND:
                return False
            else:
                raise PlatformException
        except UnexpectedStatus as e:
            if e.status_code == 404:
                return False
            elif e.status_code < 500:
                raise
            else:
                raise PlatformException

    @retry(stop=stop_after_attempt(NUM_OF_RETRIES), wait=wait_fixed(3), retry=retry_if_exception_type(UnexpectedStatus))
    @staticmethod
    def initialize_table(
        workspace_name: str,
        table_name: str,
        columns: List[Column],
        client: AuthenticatedClient,
    ) -> bool:
        """
        Initializes a table with the given name and columns on the specified platform.

        Args:
            workspace_name (str): The name of the workspace.
            table_name (str): The name of the table to be initialized.
            columns (List[Column]): List of Column objects representing the table's columns.
            client (AuthenticatedClient): The authenticated client for platform interaction.

        Returns:
            bool: True if the table is successfully initialized, False otherwise.

        Raises:
            UnexpectedStatus: If an unexpected status code is received during initialization.
        """
        try:
            create_table.sync_detailed(
                workspace=workspace_name,
                client=client,
                json_body=[
                    ApiTableSchema(
                        name=table_name,
                        attributes=UNSET,
                        columns=[
                            ApiColumnSchema(name=column.name, tpe=ExplicitExprType(column.ctype)) for column in columns
                        ],
                    )
                ],
            )
            return True
        except UnexpectedStatus:
            raise

    @retry(stop=stop_after_attempt(NUM_OF_RETRIES), wait=wait_fixed(3), retry=retry_if_exception_type(UnexpectedStatus))
    @staticmethod
    def delete_table(
        workspace_name: str,
        table_name: str,
        client: AuthenticatedClient,
    ) -> bool:
        """
        Deletes a table from the specified platform.

        Args:
            workspace_name (str): The name of the workspace.
            table_name (str): The name of the table to be deleted.
            client (AuthenticatedClient): The authenticated client for platform interaction.

        Returns:
            bool: True if the table is successfully deleted, False otherwise.

        Raises:
            UnexpectedStatus: If an unexpected status code is received during deletion.
            PlatformException: If an unexpected platform error occurs.
        """
        try:
            req = delete_table.sync_detailed(
                workspace_name,
                table_name,
                client=client,
            )
            if req.status_code == HTTPStatus.OK:
                return True
            return False
        except UnexpectedStatus as e:
            if e.status_code < 500:
                raise
            else:
                raise PlatformException

    @retry(stop=stop_after_attempt(NUM_OF_RETRIES), wait=wait_fixed(3), retry=retry_if_exception_type(UnexpectedStatus))
    @staticmethod
    def read_table(
        workspace_name: str,
        table_name: str,
        client: AuthenticatedClient,
        columns: Optional[List[str]] = None,
        exclude_formulas: bool = False,
    ) -> pd.DataFrame:
        """
        Reads data from a table on the specified platform and returns it as a DataFrame.

        Args:
            workspace_name (str): The name of the workspace.
            table_name (str): The name of the table to read data from.
            client (AuthenticatedClient): The authenticated client for platform interaction.
            columns (Optional[List[str]]): List of column names to retrieve. If None, all columns are retrieved.
            exclude_formulas (bool): If True, excludes formula columns from the retrieved data.

        Returns:
            pd.DataFrame: A DataFrame containing the table data.

        Raises:
            UnexpectedStatus: If an unexpected status code is received during data retrieval.
            PlatformException: If an unexpected platform error occurs.
        """

        if columns is None:
            metadata = TableUtils.get_metadata(
                workspace_name,
                table_name,
                client,
                exclude_formulas=exclude_formulas,
            )
            if isinstance(metadata.columns, Unset):
                raise PlatformException
            columns = [column.name for column in metadata.columns]
        rows_limit = int(CELL_LIMIT / len(columns))
        api_rows = TableUtils.get_data(
            workspace_name,
            table_name,
            client,
            rows_limit,
            columns,
            TableUtils.get_slice_of_data,
        )
        if isinstance(api_rows, Unset):
            raise PlatformException
        return pd.DataFrame(
            data=[row.values for row in api_rows],
            columns=columns,
        )

    @retry(stop=stop_after_attempt(NUM_OF_RETRIES), wait=wait_fixed(5), retry=retry_if_exception_type(PlatformException))
    @staticmethod
    def truncate(
        workspace_name: str,
        table_name: str,
        client: AuthenticatedClient,
    ) -> bool:
        """
        Truncates a table on the specified platform, removing all its data.

        Args:
            workspace_name (str): The name of the workspace.
            table_name (str): The name of the table to be truncated.
            client (AuthenticatedClient): The authenticated client for platform interaction.

        Returns:
            bool: True if the table is successfully truncated, False otherwise.

        Raises:
            UnexpectedStatus: If an unexpected status code is received during truncation.
            PlatformException: If an unexpected platform error occurs.
        """
        try:
            response = truncate_table.sync_detailed(workspace_name, table_name, client=client)
            if response.status_code == HTTPStatus.OK:
                return True
            return False
        except UnexpectedStatus as e:
            if e.status_code < 500:
                raise
            else:
                raise PlatformException

    @staticmethod
    def get_data(
        workspace_name: str,
        table_name: str,
        nocode_client: AuthenticatedClient,
        rows_limit: int,
        columns: List[str],
        func: Callable,
    ) -> List[TableRow] | Unset:
        """
        Gets data from a table on the specified platform using a specified function.

        Args:
            workspace_name (str): The name of the workspace.
            table_name (str): The name of the table to retrieve data from.
            nocode_client (AuthenticatedClient): The authenticated client for platform interaction.
            rows_limit (int): The maximum number of rows to retrieve.
            columns (List[str]): List of column names to retrieve.
            func (Callable): The function to use for retrieving data.

        Returns:
            List[TableRow] | Unset: List of TableRow objects representing the retrieved data or Unset if no data is retrieved.

        Raises:
            UnexpectedStatus: If an unexpected status code is received during data retrieval.
            PlatformException: If an unexpected platform error occurs.
        """
        table_data: ApiTableData = func(
            workspace_name,
            table_name,
            rows_limit,
            0,
            columns,
            nocode_client,
        )
        if isinstance(table_data.rows, Unset):
            raise PlatformException
        return table_data.rows

    @staticmethod
    @retry(stop=stop_after_attempt(NUM_OF_RETRIES), wait=wait_fixed(5), retry=retry_if_exception_type(PlatformException))
    def get_metadata(
        workspace_name: str,
        table_name: str,
        client: AuthenticatedClient,
        exclude_formulas: bool = False,
        columns: Optional[List[str]] = None,
    ) -> ApiTable:
        try:
            table_metadata = get_table.sync(workspace_name, table_name, client=client)
            if table_metadata is None:
                raise PlatformException
            else:
                columns_subset = []
                if isinstance(table_metadata.columns, Unset):
                    raise PlatformException
                if exclude_formulas:
                    for column in table_metadata.columns:
                        if column.formula is None:
                            columns_subset.append(column)
                    table_metadata.columns = columns_subset
                elif columns is not None:
                    for column in table_metadata.columns:
                        if column.name in columns:
                            columns_subset.append(column)
                    table_metadata.columns = columns_subset

                return table_metadata
        except UnexpectedStatus as e:
            if e.status_code < 500:
                raise
            else:
                raise PlatformException

    @staticmethod
    @retry(stop=stop_after_attempt(NUM_OF_RETRIES), wait=wait_fixed(3), retry=retry_if_exception_type(PlatformException))
    def get_slice_of_data(
        workspace_name: str,
        table_name: str,
        limit: int,
        offset: int,
        list_of_columns: List[str],
        client: AuthenticatedClient,
    ) -> ApiTableData:
        try:
            table_data = get_incomplete_table_query_data.sync(
                workspace_name,
                table_name,
                client=client,
                json_body=list_of_columns,
                limit=limit,
                offset=offset,
            )
            if table_data is None:
                raise PlatformException
            else:
                return table_data
        except UnexpectedStatus as e:
            if e.status_code < 500:
                raise
            else:
                raise PlatformException

    @staticmethod
    def get_table_data_sync(
        workspace_name: str,
        table_name: str,
        client: AuthenticatedClient,
        limit: int,
        offset: int,
        list_of_columns: List[str],
    ) -> ApiTableData:
        if list_of_columns is None:
            table_data = get_table_data.sync(workspace_name, table_name, client=client, limit=limit, offset=offset)

        else:
            table_data = get_incomplete_table_query_data.sync(
                workspace_name,
                table_name,
                client=client,
                json_body=list_of_columns,
                limit=limit,
                offset=offset,
            )
        if isinstance(table_data, Unset) or table_data is None:
            raise PlatformException
        return table_data

    @staticmethod
    def get_rows(
        workspace_name: str,
        table_name: str,
        client: AuthenticatedClient,
        limit: int,
        offset: int,
        list_of_columns: List[str],
        exclude_formulas: bool = False,
    ) -> ApiTableData:
        table_data = TableUtils.get_slice_of_data(
            workspace_name,
            table_name,
            limit,
            offset,
            list_of_columns,
            client,
        )
        if not exclude_formulas and table_data.scheduled_jobs > 0:
            TableUtils.get_slice_of_data(
                workspace_name,
                table_name,
                limit,
                offset,
                list_of_columns,
                client,
                )
        return table_data

    @staticmethod
    def get_import_job_status(job_id: int, workspace_name: str, client: AuthenticatedClient) -> ImportJob:
        import_job = get_csv_import_job.sync(
            workspace_name,
            job_id,
            client=client,
        )
        job = import_job
        if job is None:
            raise PlatformException
        return job

    @staticmethod
    def get_patch_insert(
        match_columns_names: List[str],
        data_columns_names: List[str],
        df: pd.DataFrame,
        on_conflict: Literal["ignore", "update", "fail"] = "ignore",
    ) -> Insert:
        return Insert(
            op="Insert",
            on_conflict=ApiOnConflict(on_conflict),
            match_columns=[
                ApiColumnWithValues(
                    name=name,
                    values=TableUtils.column_to_values(df, name),
                )
                for name in match_columns_names
            ],
            data_columns=[
                ApiColumnWithNullableValues(
                    name=name,
                    values=TableUtils.column_to_values(df, name),
                )
                for name in data_columns_names
            ],
        )

    @staticmethod
    def get_patch_delete(
        match_columns_names: List[str],
        delete_mode: Literal["delete_matching", "delete_not_matching"],
        df: pd.DataFrame,
    ) -> Delete:
        return Delete(
            op="Delete",
            delete_mode=ApiDeleteMode(delete_mode),
            match_columns=[
                ApiColumnWithValues(
                    name=name,
                    values=TableUtils.column_to_values(df, name),
                )
                for name in match_columns_names
            ],
        )

    @staticmethod
    def get_patch_update(
        match_columns_names: List[str],
        data_columns_names: List[str],
        df: pd.DataFrame,
    ) -> Update:
        return Update(
            op="Update",
            match_columns=[
                ApiColumnWithValues(
                    name=name,
                    values=TableUtils.column_to_values(df, name),
                )
                for name in match_columns_names
            ],
            data_columns=[
                ApiColumnWithNullableValues(
                    name=name,
                    values=TableUtils.column_to_values(df, name),
                )
                for name in data_columns_names
            ],
        )

    @staticmethod
    def get_patch_append(
        data_columns_names: List[str],
        df: pd.DataFrame,
    ) -> Append:
        return Append(
            "Append",
            data_columns=[
                ApiColumnWithNullableValues(
                    name=name,
                    values=TableUtils.column_to_values(df, name),
                )
                for name in data_columns_names
            ],
        )

    @staticmethod
    def column_to_values(df: pd.DataFrame, column_name: str) -> List[Any]:
        df.replace({np.nan: None}, inplace=True)
        if pd.api.types.is_datetime64_any_dtype(df[column_name]):
            return [None if x == "NaT" else x for x in list(np.datetime_as_string(df[column_name].values, unit="D"))]  # type: ignore
        else:
            return [str(x) if x is not None else None for x in df[column_name].values.tolist()]

    @retry(stop=stop_after_attempt(NUM_OF_RETRIES), wait=wait_fixed(5), retry=retry_if_exception_type(PlatformException))
    @staticmethod
    def import_data(
        workspace_name: str,
        table_name: str,
        table_df: pd.DataFrame,
        client: AuthenticatedClient,
        import_mode: TableImportMode = TableImportMode.REPLACE_DATA,
    ) -> Any:
        """
        Replaces data in a table on the specified platform with the data in a DataFrame.

        Args:
            workspace_name (str): The name of the workspace.
            table_name (str): The name of the table to be replaced.
            table_df (pd.DataFrame): The DataFrame containing the new data.
            client (AuthenticatedClient): The authenticated client for platform interaction.

        Returns:
            bool: True if the table is successfully replaced, False otherwise.

        Raises:
            UnexpectedStatus: If an unexpected status code is received during replacement.
            PlatformException: If an unexpected platform error occurs.
        """
        try:
            if len(table_df) == 0:
                return False
            csv_buffer = StringIO()
            table_df.to_csv(csv_buffer, index=False)

            import_job = create_csv_import_job.sync(
                workspace_name,
                table_name,
                mode=import_mode,
                client=client,
            )
            if import_job is None:
                raise PlatformException
            response = requests.put(
                import_job.put_url,
                data=csv_buffer.getvalue().encode("utf-8"),
            )

            if response.status_code == HTTPStatus.OK:
                return True
        except UnexpectedStatus as e:
            if e.status_code < 500:
                raise
            else:
                raise PlatformException

    @staticmethod
    def patch_table(
        workspace_name: str,
        table_name: str,
        table_df: pd.DataFrame,
        client: AuthenticatedClient,
        mode: PatchMode,
        *,
        match_on_columns: List[str] = [],
        data_columns: List[str] = [],
    ) -> Any:
        """
        Patch a table in the specified workspace with the provided DataFrame.

        Parameters:
        - table_name (str): The name of the table to be patched.
        - workspace_name (str): The name of the workspace containing the table.
        - table_df (pd.DataFrame): The DataFrame containing the data to be patched.
        - client (AuthenticatedClient): An authenticated client for making API requests.
        - mode (PatchMode): The patch mode specifying the type of patch operation to be performed.
        - match_on_columns (List[str], optional): List of column names to use for matching rows during patching.
        Defaults to an empty list.
        - data_columns (List[str], optional): List of column names to be included in the patch data.
        Defaults to an empty list.

        Returns:
        - Any: Returns True if the patch operation is successful.

        Raises:
        - UnexpectedStatus: If an unexpected HTTP status code is received during the patch operation,
        and the status code is not less than 500.
        - PlatformException: If an unexpected platform error occurs during the patch operation.

        PatchMode enum values:
        - PatchMode.Append: Append data to the table (no matching is performed).
        - PatchMode.Delete: Delete rows from the table based on specified columns.
        - PatchMode.InsertOnConflictFail: Insert data into the table with a fail conflict resolution strategy.
        - PatchMode.InsertOnConflictIgnore: Insert data into the table with an ignore conflict resolution strategy.
        - PatchMode.InsertOnConflictUpdate: Insert data into the table with an update conflict resolution strategy.
        - PatchMode.Update: Update existing rows in the table based on specified columns.
        """
        json_body: List[Append | Delete | Insert| Update]  = []
        match mode:
            case PatchMode.Append:
                json_body.append(TableUtils.get_patch_append(data_columns, table_df))
            case PatchMode.Delete:
                json_body.append(TableUtils.get_patch_delete(match_on_columns, "delete_matching", table_df))
            case PatchMode.InsertOnConflictFail:
                json_body.append(TableUtils.get_patch_insert(match_on_columns, data_columns, table_df, "fail"))
            case PatchMode.InsertOnConflictIgnore:
                json_body.append(TableUtils.get_patch_insert(match_on_columns, data_columns, table_df, "ignore"))
            case PatchMode.InsertOnConflictUpdate:
                json_body.append(TableUtils.get_patch_insert(match_on_columns, data_columns, table_df, "update"))
            case PatchMode.Update:
                json_body.append(TableUtils.get_patch_update(match_on_columns, data_columns, table_df))
        
        try:
            request = patch_table_data.sync_detailed(
                workspace=workspace_name, table=table_name, client=client, json_body=json_body
            )
            if request.status_code == 200:
                return True
        except UnexpectedStatus as e:
            if e.status_code < 500:
                raise
            else:
                raise PlatformException

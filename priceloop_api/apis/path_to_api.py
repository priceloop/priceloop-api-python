import typing_extensions

from priceloop_api.paths import PathValues
from priceloop_api.apis.paths.api_v1_0_hello import ApiV10Hello
from priceloop_api.apis.paths.api_v1_0_hello_auth import ApiV10HelloAuth
from priceloop_api.apis.paths.api_v1_0_workspaces import ApiV10Workspaces
from priceloop_api.apis.paths.api_v1_0_workspaces_workspace import ApiV10WorkspacesWorkspace
from priceloop_api.apis.paths.api_v1_0_workspaces_workspace_external_functions_function import ApiV10WorkspacesWorkspaceExternalFunctionsFunction
from priceloop_api.apis.paths.api_v1_0_workspaces_workspace_tables_table import ApiV10WorkspacesWorkspaceTablesTable
from priceloop_api.apis.paths.api_v1_0_workspaces_workspace_tables_table_columns_column import ApiV10WorkspacesWorkspaceTablesTableColumnsColumn
from priceloop_api.apis.paths.api_v1_0_workspaces_workspace_tables_table_columns_column_data import ApiV10WorkspacesWorkspaceTablesTableColumnsColumnData
from priceloop_api.apis.paths.api_v1_0_workspaces_workspace_tables_table_columns_column_expression import ApiV10WorkspacesWorkspaceTablesTableColumnsColumnExpression
from priceloop_api.apis.paths.api_v1_0_workspaces_workspace_tables_table_data import ApiV10WorkspacesWorkspaceTablesTableData
from priceloop_api.apis.paths.api_v1_0_workspaces_workspace_tables_table_upload_csv_url import ApiV10WorkspacesWorkspaceTablesTableUploadCsvUrl

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V1_0_HELLO: ApiV10Hello,
        PathValues.API_V1_0_HELLOAUTH: ApiV10HelloAuth,
        PathValues.API_V1_0_WORKSPACES: ApiV10Workspaces,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE: ApiV10WorkspacesWorkspace,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_EXTERNALFUNCTIONS_FUNCTION: ApiV10WorkspacesWorkspaceExternalFunctionsFunction,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE: ApiV10WorkspacesWorkspaceTablesTable,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_COLUMNS_COLUMN: ApiV10WorkspacesWorkspaceTablesTableColumnsColumn,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_COLUMNS_COLUMN_DATA: ApiV10WorkspacesWorkspaceTablesTableColumnsColumnData,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_COLUMNS_COLUMN_EXPRESSION: ApiV10WorkspacesWorkspaceTablesTableColumnsColumnExpression,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_DATA: ApiV10WorkspacesWorkspaceTablesTableData,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_UPLOADCSVURL: ApiV10WorkspacesWorkspaceTablesTableUploadCsvUrl,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V1_0_HELLO: ApiV10Hello,
        PathValues.API_V1_0_HELLOAUTH: ApiV10HelloAuth,
        PathValues.API_V1_0_WORKSPACES: ApiV10Workspaces,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE: ApiV10WorkspacesWorkspace,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_EXTERNALFUNCTIONS_FUNCTION: ApiV10WorkspacesWorkspaceExternalFunctionsFunction,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE: ApiV10WorkspacesWorkspaceTablesTable,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_COLUMNS_COLUMN: ApiV10WorkspacesWorkspaceTablesTableColumnsColumn,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_COLUMNS_COLUMN_DATA: ApiV10WorkspacesWorkspaceTablesTableColumnsColumnData,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_COLUMNS_COLUMN_EXPRESSION: ApiV10WorkspacesWorkspaceTablesTableColumnsColumnExpression,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_DATA: ApiV10WorkspacesWorkspaceTablesTableData,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_UPLOADCSVURL: ApiV10WorkspacesWorkspaceTablesTableUploadCsvUrl,
    }
)

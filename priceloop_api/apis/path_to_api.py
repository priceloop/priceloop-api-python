import typing_extensions

from priceloop_api.paths import PathValues
from priceloop_api.apis.paths.api_v1_0_workspaces import ApiV10Workspaces
from priceloop_api.apis.paths.api_v1_0_workspaces_workspace import ApiV10WorkspacesWorkspace
from priceloop_api.apis.paths.api_v1_0_workspaces_workspace_tables_table import ApiV10WorkspacesWorkspaceTablesTable
from priceloop_api.apis.paths.api_v1_0_workspaces_workspace_tables_table_data import ApiV10WorkspacesWorkspaceTablesTableData
from priceloop_api.apis.paths.api_v1_0_workspaces_workspace_tables_table_upload_csv_url import ApiV10WorkspacesWorkspaceTablesTableUploadCsvUrl

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V1_0_WORKSPACES: ApiV10Workspaces,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE: ApiV10WorkspacesWorkspace,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE: ApiV10WorkspacesWorkspaceTablesTable,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_DATA: ApiV10WorkspacesWorkspaceTablesTableData,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_UPLOADCSVURL: ApiV10WorkspacesWorkspaceTablesTableUploadCsvUrl,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V1_0_WORKSPACES: ApiV10Workspaces,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE: ApiV10WorkspacesWorkspace,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE: ApiV10WorkspacesWorkspaceTablesTable,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_DATA: ApiV10WorkspacesWorkspaceTablesTableData,
        PathValues.API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_UPLOADCSVURL: ApiV10WorkspacesWorkspaceTablesTableUploadCsvUrl,
    }
)

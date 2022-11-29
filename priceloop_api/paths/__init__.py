# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from priceloop_api.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V1_0_HELLO = "/api/v1.0/hello"
    API_V1_0_HELLOAUTH = "/api/v1.0/hello-auth"
    API_V1_0_WORKSPACES = "/api/v1.0/workspaces"
    API_V1_0_WORKSPACES_WORKSPACE = "/api/v1.0/workspaces/{workspace}"
    API_V1_0_WORKSPACES_WORKSPACE_EXTERNALFUNCTIONS_FUNCTION = "/api/v1.0/workspaces/{workspace}/external-functions/{function}"
    API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE = "/api/v1.0/workspaces/{workspace}/tables/{table}"
    API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_COLUMNS_COLUMN = "/api/v1.0/workspaces/{workspace}/tables/{table}/columns/{column}"
    API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_COLUMNS_COLUMN_DATA = "/api/v1.0/workspaces/{workspace}/tables/{table}/columns/{column}/data"
    API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_COLUMNS_COLUMN_EXPRESSION = "/api/v1.0/workspaces/{workspace}/tables/{table}/columns/{column}/expression"
    API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_DATA = "/api/v1.0/workspaces/{workspace}/tables/{table}/data"
    API_V1_0_WORKSPACES_WORKSPACE_TABLES_TABLE_UPLOADCSVURL = "/api/v1.0/workspaces/{workspace}/tables/{table}/upload-csv-url"

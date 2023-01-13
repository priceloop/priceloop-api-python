import requests
import pandas as pd
from io import StringIO

from priceloop_api.models.get_table_upload_csv_url_mode import GetTableUploadCsvUrlMode
from priceloop_api.client import AuthenticatedClient
from priceloop_api.api.default import (
    list_workspaces,
    get_workspace,
    get_table_upload_csv_url,
    get_table,
    get_table_data,
)


def to_nocode(
    df: pd.DataFrame,
    table_name: str,
    client: AuthenticatedClient,
    mode: GetTableUploadCsvUrlMode = GetTableUploadCsvUrlMode.DELETE_AND_RECREATE,
    workspace_name: str = None,
) -> None:
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=None)

    if workspace_name is None:
        workspaces = list_workspaces.sync(client=client)
        workspace = get_workspace.sync(workspaces[0], client=client)
        workspace_name = workspace.name

    url = get_table_upload_csv_url.sync(workspace_name, table_name, mode=mode, client=client)

    requests.put(url.put_url, data=csv_buffer.getvalue().encode("utf-8"))
    print("Upload Successful, please wait a moment for the changes to appear")


def read_nocode(
    table_name: str, client: AuthenticatedClient, limit: int, offset: int, workspace_name: str = None
) -> pd.DataFrame:
    csv_buffer = StringIO()

    if workspace_name is None:
        workspaces = list_workspaces.sync(client=client)
        workspace = get_workspace.sync(workspaces[0], client=client)

        workspace_name = workspace.name

    raw_header = get_table.sync(workspace_name, table_name, client=client)

    header = [i.name for i in raw_header.columns]
    raw_table_data = get_table_data.sync(workspace_name, table_name, client=client, limit=limit, offset=offset)

    table_data = pd.DataFrame([v.values for v in raw_table_data.rows], columns=header)
    # To-do: infer type from nocode
    table_data.to_csv(csv_buffer, index=None)
    csv_buffer.seek(0)
    table_data_type_inferred = pd.read_csv(csv_buffer)
    return table_data_type_inferred

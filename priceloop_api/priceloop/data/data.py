import requests
import pandas as pd
from io import StringIO
from typing import List, Optional

from priceloop_api.types import Unset
from priceloop_api.models import TableImportMode
from priceloop_api.client import AuthenticatedClient
from priceloop_api.api.workspace_api import (
    list_workspaces,
    get_workspace,
)
from priceloop_api.api.table_api import (
    get_table,
    get_table_data,
)
from priceloop_api.api.import_api import (
    create_csv_import_job,
)

d = {"t": True, "f": False}


def to_nocode(
    df: pd.DataFrame,
    table_name: str,
    client: AuthenticatedClient,
    mode: TableImportMode = TableImportMode.DELETE_AND_RECREATE,
    workspace_name: Optional[str] = None,
) -> Optional[int]:
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    if workspace_name is None:
        workspaces = list_workspaces.sync(client=client)
        if workspaces is None:
            return None
        workspace = get_workspace.sync(workspaces[0], client=client)
        if workspace is None:
            return None
        workspace_name = workspace.name

    import_job = create_csv_import_job.sync(workspace_name, table_name, mode=mode, client=client)
    if import_job is None:
        return None

    requests.put(import_job.put_url, data=csv_buffer.getvalue().encode("utf-8"))
    print("Upload Successful, please wait a moment for the changes to appear")
    return import_job.import_job_id


def read_nocode(
    table_name: str, client: AuthenticatedClient, limit: int, offset: int, workspace_name: Optional[str] = None
) -> Optional[pd.DataFrame]:
    csv_buffer = StringIO()

    if workspace_name is None:
        workspaces = list_workspaces.sync(client=client)
        if workspaces is None:
            return None
        workspace = get_workspace.sync(workspaces[0], client=client)
        if workspace is None:
            return None
        workspace_name = workspace.name

    raw_header = get_table.sync(workspace_name, table_name, client=client)
    raw_table_data = get_table_data.sync(workspace_name, table_name, client=client, limit=limit, offset=offset)

    if raw_header is None:
        return None
    if raw_table_data is None:
        return None
    # columns = raw_header.columns
    if isinstance(raw_header.columns, Unset):
        return None
    if isinstance(raw_table_data.rows, Unset):
        return None

    header = [i.name for i in raw_header.columns]
    boolean_cols = [i.name for i in raw_header.columns if i.tpe == "boolean"]
    table_data = pd.DataFrame([v.values for v in raw_table_data.rows], columns=header)
    for col in boolean_cols:
        table_data[col] = table_data[col].map(d)
    # To-do: infer type from nocode
    table_data.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    table_data_type_inferred = pd.read_csv(csv_buffer)
    return table_data_type_inferred


def create_table_from_schema(schema: str, client: AuthenticatedClient, workspace_name: Optional[str] = None) -> None:
    if workspace_name is None:
        workspaces = list_workspaces.sync(client=client)
        if workspaces is None:
            return
        workspace = get_workspace.sync(workspaces[0], client=client)
        if workspace is None:
            return
        workspace_name = workspace.name

    url = "{}/api/v1.0/workspaces/{workspace}/create-tables".format(client.base_url, workspace=workspace_name)

    headers = client.get_headers()
    headers["Content-Type"] = "application/json"
    requests.post(url, headers=client.get_headers(), data=schema)

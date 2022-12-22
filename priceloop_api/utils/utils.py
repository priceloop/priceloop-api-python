import requests
import pandas as pd
from io import StringIO
from priceloop_api import ApiClient
from priceloop_api.apis.tags.default_api import DefaultApi


def to_nocode(
    df: pd.DataFrame,
    table_name: str,
    configuration,
    mode = "delete_and_recreate",
    workspace_name: str = None,
) -> None:
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index = None)
    with ApiClient(configuration) as api_client:
        api_instance = DefaultApi(api_client)
        if workspace_name is None:
            workspaces = api_instance.list_workspaces().body
            workspace = api_instance.get_workspace(
                path_params = {"workspace": workspaces[0]}
            ).body
            workspace_name = workspace.name

        url = api_instance.get_table_upload_csv_url(
            path_params = {"workspace": workspace_name, "table": table_name},
            query_params = {"mode": mode},
        ).body
        requests.put(url.putUrl, data = csv_buffer.getvalue().encode("utf-8"))
        print("Upload Successful, please wait a moment for the changes to appear")


def read_nocode(
    table_name: str, configuration, limit: int, offset: int, workspace_name: str = None
):
    csv_buffer = StringIO()
    with ApiClient(configuration) as api_client:
        api_instance = DefaultApi(api_client)
        if workspace_name is None:
            workspaces = api_instance.list_workspaces().body
            workspace = api_instance.get_workspace(
                path_params = {"workspace": workspaces[0]}
            ).body
            workspace_name = workspace.name

        raw_header = api_instance.get_table(
            path_params = {"workspace": workspace_name, "table": table_name}
        ).body
        header = [i["name"] for i in raw_header["columns"]]
        raw_table_data = api_instance.get_table_data(
            query_params = {"limit": limit, "offset": offset},
            path_params = {
                "workspace": workspace_name,
                "table": table_name,
            },
        ).body
        table_data = pd.DataFrame([v["values"] for v in raw_table_data["rows"]], columns = header)
        # To-do: infer type from nocode
        table_data.to_csv(csv_buffer, index = None)
        csv_buffer.seek(0)
        table_data_type_inferred = pd.read_csv(csv_buffer)
    return table_data_type_inferred

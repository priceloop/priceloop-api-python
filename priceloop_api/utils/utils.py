import requests
import pandas as pd
from io import StringIO
from priceloop_api import ApiClient
from priceloop_api.api.default_api import DefaultApi

def to_nocode(df: pd.DataFrame, table_name: str, configuration, mode='delete_and_recreate') -> None:
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=None)
    with ApiClient(configuration) as api_client:
        api_instance = DefaultApi(api_client)
        workspaces = api_instance.list_workspaces()
        workspace = api_instance.get_workspace(workspaces[0])
        url = api_instance.get_table_upload_csv_url(workspace.name, table_name, mode=mode)
        requests.put(url, data=csv_buffer.getvalue().encode('utf-8'))
        print('Upload Successful, please wait a moment for the changes to appear')

def read_nocode(table_name: str, configuration, limit: int, offset: int):
    with ApiClient(configuration) as api_client:
        api_instance = DefaultApi(api_client)
        workspaces = api_instance.list_workspaces()
        workspace = api_instance.get_workspace(workspaces[0])
        raw_header = api_instance.get_table(workspace.name, table_name)
        header = ['index'] + [i['name'] for i in raw_header['columns']]
        raw_table_data = api_instance.get_table_data(workspace.name, table_name, limit=limit, offset=offset)
        table_data = pd.DataFrame(raw_table_data['rows'], columns=header).drop(columns='index')
    return table_data
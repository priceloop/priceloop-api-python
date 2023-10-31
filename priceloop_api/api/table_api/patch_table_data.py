from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.append import Append
from ...models.delete import Delete
from ...models.insert import Insert
from ...models.update import Update
from ...types import Response


def _get_kwargs(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    json_body: List[Union["Append", "Delete", "Insert", "Update"]],
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/tables/{table}/data".format(
        client.base_url, workspace=workspace, table=table
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item: Dict[str, Any]

        if isinstance(json_body_item_data, Append):
            json_body_item = json_body_item_data.to_dict()

        elif isinstance(json_body_item_data, Delete):
            json_body_item = json_body_item_data.to_dict()

        elif isinstance(json_body_item_data, Insert):
            json_body_item = json_body_item_data.to_dict()

        else:
            json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    json_body: List[Union["Append", "Delete", "Insert", "Update"]],
) -> Response[Any]:
    """Patch the data of a table.

     Specify columns and values to match on, and specify which columns should be set to which value for
    matched columns

    Args:
        workspace (str):  Example: workspace-name.
        table (str):  Example: table-name.
        json_body (List[Union['Append', 'Delete', 'Insert', 'Update']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        table=table,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    json_body: List[Union["Append", "Delete", "Insert", "Update"]],
) -> Response[Any]:
    """Patch the data of a table.

     Specify columns and values to match on, and specify which columns should be set to which value for
    matched columns

    Args:
        workspace (str):  Example: workspace-name.
        table (str):  Example: table-name.
        json_body (List[Union['Append', 'Delete', 'Insert', 'Update']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        table=table,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)

from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.export_format_type_0 import ExportFormatType0
from ...models.export_info import ExportInfo
from ...types import Response


def _get_kwargs(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    json_body: "ExportFormatType0",
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/tables/{table}/exports".format(
        client.base_url, workspace=workspace, table=table
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body: Dict[str, Any]

    if isinstance(json_body, ExportFormatType0):
        json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ExportInfo]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ExportInfo.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ExportInfo]:
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
    json_body: "ExportFormatType0",
) -> Response[ExportInfo]:
    """Export a table to a file

     This API endpoint returns a url, from which you can download the exported csv file. This download
    url will be valid for up to `.expiresInSeconds` seconds. Exported files are kept available until
    `.exportJob.availableUntil`.

    Args:
        workspace (str):  Example: workspace-name.
        table (str):  Example: table-name.
        json_body ('ExportFormatType0'):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportInfo]
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


def sync(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    json_body: "ExportFormatType0",
) -> Optional[ExportInfo]:
    """Export a table to a file

     This API endpoint returns a url, from which you can download the exported csv file. This download
    url will be valid for up to `.expiresInSeconds` seconds. Exported files are kept available until
    `.exportJob.availableUntil`.

    Args:
        workspace (str):  Example: workspace-name.
        table (str):  Example: table-name.
        json_body ('ExportFormatType0'):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportInfo
    """

    return sync_detailed(
        workspace=workspace,
        table=table,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    json_body: "ExportFormatType0",
) -> Response[ExportInfo]:
    """Export a table to a file

     This API endpoint returns a url, from which you can download the exported csv file. This download
    url will be valid for up to `.expiresInSeconds` seconds. Exported files are kept available until
    `.exportJob.availableUntil`.

    Args:
        workspace (str):  Example: workspace-name.
        table (str):  Example: table-name.
        json_body ('ExportFormatType0'):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportInfo]
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


async def asyncio(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    json_body: "ExportFormatType0",
) -> Optional[ExportInfo]:
    """Export a table to a file

     This API endpoint returns a url, from which you can download the exported csv file. This download
    url will be valid for up to `.expiresInSeconds` seconds. Exported files are kept available until
    `.exportJob.availableUntil`.

    Args:
        workspace (str):  Example: workspace-name.
        table (str):  Example: table-name.
        json_body ('ExportFormatType0'):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportInfo
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            table=table,
            client=client,
            json_body=json_body,
        )
    ).parsed
